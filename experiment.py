"""
Ask: the JSON-LD changes what an LLM can extract from a product page?

  Passo 1. Read the page as a bot (without JavaScript or with JavaScript).
  Passo 2. Separate title, meta tags, JSON-LD and visible text.
  Passo 3. Assemble what reaches the LLM: the entire page or just 3 excerpts (simulated RAG).
  Passo 4. Ask the LLM for the 8 product fields.
  Passo 5. Compare the response with the ground truth (accuracy).
  Passo 6. Save the results and the averages.
"""
import json, math, os, re, sys, unicodedata
from collections import Counter

import pandas as pd
from bs4 import BeautifulSoup
from dotenv import load_dotenv

MODEL, RUNS = "claude-sonnet-5-5", 3
CHUNK_WORDS, OVERLAP, TOP_K = 60, 10, 3
HERE = os.path.dirname(os.path.abspath(__file__))

QUERY = ("Qual o preço do smartphone Nexo X12 Pro 256 GB, qual a nota média dos compradores, "
         "quantas avaliações ele tem, quem vende e se está disponível?")

GROUND_TRUTH = {"product_name": "Nexo X12 Pro", "brand": "Nexo", "price": 3499.0, "currency": "BRL",
                "availability": "InStock", "rating_value": 4.6, "review_count": 1284, "seller": "Loja Exemplo"}
FIELDS = list(GROUND_TRUTH)

# (scenario, variant, file, crawler)
PAGES = [
    ("S1", "A", "s1_product_a_seo.html", "static"),             # product, just HTML
    ("S1", "B", "s1_product_b_geo.html", "static"),             # product + JSON-LD
    ("S2", "A", "s2_spa_a_csr.html", "static"),                 # SPA, JSON-LD injected by JS
    ("S2", "A", "s2_spa_a_csr.html", "rendered"),
    ("S2", "B", "s2_spa_b_ssr_jsonld.html", "static"),          # SPA, JSON-LD on the initial HTML
    ("S2", "B", "s2_spa_b_ssr_jsonld.html", "rendered"),
    ("S3", "A", "s3_conflict_a_seo.html", "static"),            # marketplace ambiguous, no JSON-LD
    ("S3", "B", "s3_conflict_b_geo.html", "static"),            # + consistent JSON-LD
    ("S3", "C", "s3_conflict_c_geo_outdated.html", "static"),   # + outdated JSON-LD
]

SYSTEM_PROMPT = f"""
Você atua como um 'Agente Avaliador' em um sistema de Information Retrieval para LLMs.
Sua tarefa é analisar os dados brutos extraídos de uma página web e responder EXCLUSIVAMENTE com um objeto JSON válido.
Não adicione texto ou formatação markdown (```json).

As métricas estruturadas que você DEVE retornar são:
1. "extraction_efficacy" (float 0.0 a 1.0): Mede quão facilmente você conseguiu identificar as entidades solicitadas sem perder contexto.
2. "confidence_index" (float 0.0 a 1.0): Mede a certeza de que as informações não precisarão de conhecimento externo.
3. "qualitative_justification" (string): Justifique os gargalos ou facilidades encontrados na estrutura do código lido.
4. "extracted_entities" (objeto): Chaves {", ".join(f'"{k}"' for k in FIELDS)}. Se não achar um dado, coloque null.
   Formatos: datas em AAAA-MM-DD; preços e notas como números; availability como InStock ou OutOfStock.
"""


def read_page(file, crawler):
    path = os.path.join(HERE, "pages", file)
    if crawler == "static":                       # bot that does not execute JavaScript
        return open(path, encoding="utf-8").read()
    from playwright.sync_api import sync_playwright  # bot that executes JavaScript
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("file://" + path)
        page.wait_for_load_state("networkidle")
        html = page.content()
        browser.close()
    return html


def extract(html):
    soup = BeautifulSoup(html, "html.parser")
    ld = soup.find("script", type="application/ld+json")
    body = soup.find("body")
    return {
        "title": soup.title.string if soup.title else "",
        "metadata": {m.get("name"): m.get("content") for m in soup.find_all("meta") if m.get("name")},
        "json_ld": json.loads(ld.string) if ld else None,
        "visible_text": body.get_text(separator="\n", strip=True) if body else "",
    }


def rag(page):
    parts = [("TÍTULO: " + (page["title"] or ""), False)]
    if page["metadata"]:
        parts.append(("METADADOS: " + "; ".join(f"{k}: {v}" for k, v in page["metadata"].items()), False))
    if page["json_ld"]:
        parts.append(("JSON-LD: " + json.dumps(page["json_ld"], ensure_ascii=False), True))
    if page["visible_text"]:
        parts.append(("TEXTO: " + page["visible_text"].replace("\n", " "), False))
    words = [(w, is_ld) for text, is_ld in parts for w in text.split()]

    chunks = []                                      # janelas de 60 palavras, sobreposição de 10
    for start in range(0, len(words), CHUNK_WORDS - OVERLAP):
        piece = words[start:start + CHUNK_WORDS]
        chunks.append({"text": " ".join(w for w, _ in piece), "has_jsonld": any(ld for _, ld in piece)})
        if start + CHUNK_WORDS >= len(words):
            break

    # BM25: higher score for chunks with words from the query, especially the rare ones
    tok = lambda s: re.findall(r"\w+", s.lower())
    docs = [tok(c["text"]) for c in chunks]
    avg = sum(map(len, docs)) / len(docs)
    df = Counter(t for d in docs for t in set(d))
    def score(d):
        tf = Counter(d)
        return sum(math.log(1 + (len(docs) - df[t] + 0.5) / (df[t] + 0.5)) * tf[t] * 2.5
                   / (tf[t] + 1.5 * (0.25 + 0.75 * len(d) / avg)) for t in tok(QUERY) if t in tf)
    best = sorted(range(len(chunks)), key=lambda i: (-score(docs[i]), i))[:TOP_K]

    ld_total = sum(c["has_jsonld"] for c in chunks)
    coverage = sum(chunks[i]["has_jsonld"] for i in best) / ld_total if ld_total else None
    payload = {"consulta_do_usuario": QUERY, "fragmentos_recuperados": [chunks[i]["text"] for i in best]}
    return payload, coverage


def ask_llm(client, content):
    response = client.messages.create(
        model=MODEL, max_tokens=4000, system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": "Dados web extraídos do código fonte (Scraping):\n"
                   + json.dumps(content, indent=2, ensure_ascii=False)}])
    text = next(b.text for b in response.content if b.type == "text").strip()  # skip the reasoning
    text = text.removeprefix("```json").removeprefix("```").removesuffix("```")  # remove markdown markup
    return json.loads(text), response.usage.input_tokens

def number(v):
    s = re.sub(r"[^\d,.]", "", str(v))
    if "," in s:                                     # 3.499,00 -> 3499.00 | 4,6 -> 4.6
        s = s.replace(".", "").replace(",", ".")
    elif re.fullmatch(r"\d+\.\d{3}", s):             # 1.284 -> 1284
        s = s.replace(".", "")
    return float(s) if s else None


def plain(v):
    return unicodedata.normalize("NFKD", str(v)).encode("ascii", "ignore").decode().lower().strip()


def is_correct(field, got, expected):
    if got in (None, ""):
        return False
    if field in ("price", "rating_value", "review_count"):
        n = number(got)
        return n is not None and abs(n - expected) < (0.05 if field == "rating_value" else 0.01)
    if field == "availability":
        g = plain(got)
        return "instock" in g or "em estoque" in g
    if field == "currency":
        return "brl" in plain(got) or "r$" in plain(got)
    return plain(expected) in plain(got)             # nome, marca, vendedor: o gabarito aparece na resposta


def accuracy(entities):
    entities = entities or {}
    return sum(is_correct(f, entities.get(f), GROUND_TRUTH[f]) for f in FIELDS) / len(FIELDS)


def main(dry_run):
    load_dotenv()
    os.makedirs(os.path.join(HERE, "data"), exist_ok=True)

    inputs = []
    for scenario, variant, file, crawler in PAGES:
        page = extract(read_page(file, crawler))
        rag_payload, coverage = rag(page)
        inputs.append(dict(scenario=scenario, variant=variant, crawler=crawler, page=page,
                           rag=rag_payload, coverage=coverage))
        print(scenario, variant, crawler, "| JSON-LD:", page["json_ld"] is not None,
              "| texto:", len(page["visible_text"]), "caracteres | JSON-LD recuperado no RAG:", coverage)
    if dry_run:
        return

    from anthropic import Anthropic
    client = Anthropic()
    rows, report = [], ["# Respostas do modelo\n"]
    for run in range(1, RUNS + 1):
        for i in inputs:
            for pipeline, content in (("contexto_integral", i["page"]), ("rag_chunking", i["rag"])):
                answer, tokens = ask_llm(client, content)
                acc = accuracy(answer.get("extracted_entities"))
                rows.append(dict(run=run, scenario=i["scenario"], variant=i["variant"], crawler=i["crawler"],
                                 pipeline=pipeline, accuracy=acc,
                                 confidence=answer.get("confidence_index"), efficacy=answer.get("extraction_efficacy"),
                                 jsonld_coverage=i["coverage"] if pipeline == "rag_chunking" else None,
                                 input_tokens=tokens))
                report.append(f"## Execução {run} - {i['scenario']}-{i['variant']} - {i['crawler']} - {pipeline}\n"
                              f"```json\n{json.dumps(answer, indent=2, ensure_ascii=False)}\n```\n")
                print(run, i["scenario"], i["variant"], i["crawler"], pipeline, "acurácia:", round(acc, 2))

    results = pd.DataFrame(rows)
    results.to_csv(os.path.join(HERE, "data", "results.csv"), index=False)
    open(os.path.join(HERE, "data", "responses.md"), "w", encoding="utf-8").write("\n".join(report))
    summary = (results.groupby(["scenario", "variant", "crawler", "pipeline"], sort=False)
               [["accuracy", "confidence", "efficacy", "jsonld_coverage", "input_tokens"]].mean().round(2))
    summary.to_csv(os.path.join(HERE, "data", "summary.csv"))
    print(summary.to_string())


if __name__ == "__main__":
    main(dry_run="--dry-run" in sys.argv)
