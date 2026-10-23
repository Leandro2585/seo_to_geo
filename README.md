# Do SEO ao GEO — Experimento

Experimento do TCC **"Do SEO ao GEO: estratégias de otimização para recomendação de websites por LLMs"**.

**Pergunta:** o JSON-LD (Schema.org) muda o que um LLM consegue extrair de uma página de produto?

Todo o experimento está em um único arquivo, `experiment.py`, organizado em 6 passos:

| Passo | O que faz | Função |
|---|---|---|
| 1 | Lê a página como um robô que não executa JavaScript (*estático*) ou que executa (*renderizado*, via Playwright) | `read_page` |
| 2 | Separa título, meta tags, bloco JSON-LD e texto visível (BeautifulSoup) | `extract` |
| 3 | Monta o que chega ao LLM: a página inteira (*contexto integral*) ou só os 3 trechos de 60 palavras mais parecidos com a pergunta do usuário (*RAG simulado*, ranqueados por BM25) | `rag` |
| 4 | Pede ao LLM (`claude-sonnet-5-5`) os 8 campos do produto e duas notas autodeclaradas (eficácia e confiança) | `ask_llm` |
| 5 | Compara cada campo com o gabarito (o que o usuário vê na página) e calcula a acurácia | `accuracy` |
| 6 | Repete 3 vezes, salva os resultados e calcula as médias com pandas | `main` |

## Páginas testadas (`pages/`)

Todas descrevem o mesmo produto fictício (Nexo X12 Pro, R$ 3.499,00, nota 4,6, 1.284 avaliações, vendido pela Loja Exemplo).

| Cenário | Arquivos | O que testa |
|---|---|---|
| S1 – Produto | `s1_product_a_seo.html` (só HTML) · `s1_product_b_geo.html` (+ JSON-LD) | Efeito direto do JSON-LD |
| S2 – SPA | `s2_spa_a_csr.html` (JSON-LD injetado por JavaScript) · `s2_spa_b_ssr_jsonld.html` (JSON-LD no HTML inicial) · `s2_spa_app.js` | Página montada no navegador |
| S3 – Marketplace | `s3_conflict_a_seo.html` (sem JSON-LD) · `s3_conflict_b_geo.html` (JSON-LD correto) · `s3_conflict_c_geo_outdated.html` (JSON-LD desatualizado) | Preços e notas concorrentes na mesma página |

## Como executar

```bash
pip install -r requirements.txt
python -m playwright install chromium
# ANTHROPIC_API_KEY=... no arquivo .env
python experiment.py --dry-run   # só os passos 1 a 3, sem custo
python experiment.py             # 9 páginas × 2 formas de leitura × 3 execuções = 54 chamadas
```

## Resultados (`data/`)

- `results.csv`: uma linha por chamada (acurácia, confiança, eficácia, cobertura do JSON-LD no RAG, tokens);
- `summary.csv`: médias por cenário, variante, rastreador e forma de leitura;
- `responses.md`: resposta bruta do modelo em cada chamada.

Principais achados da execução de 23/10/2026:

- Com a página inteira, o modelo acertou todos os campos **com ou sem** JSON-LD; o JSON-LD só elevou as notas autodeclaradas (confiança 0,92 → 0,97 no S1).
- Na SPA lida sem JavaScript, a página sem JSON-LD no HTML inicial teve acurácia **0**; com JSON-LD no HTML inicial, **1,00**.
- No RAG simulado, o JSON-LD foi recuperado só em parte (67% no S1, 50% no S3); no marketplace, o trecho com o vendedor não foi recuperado, o modelo deixou o vendedor nulo e a acurácia caiu para 0,88 nas três variantes.
- A acurácia foi idêntica nas 3 execuções; só as notas autodeclaradas variaram (até 0,12).

> Os resultados dependem da versão do modelo. Para repetir o experimento com outro modelo, troque `MODEL` no início do script. O `claude-sonnet-5-5` não aceita o parâmetro `temperature`, por isso a chamada usa a amostragem padrão da API.
