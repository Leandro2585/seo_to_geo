# Devolutiva da pesquisa "O Futuro das Buscas na Internet e a Inteligência Artificial"

Esta página apresenta os resultados do Trabalho de Conclusão de Curso **"Do SEO ao GEO: estratégias de otimização para recomendação de websites por LLMs"** (Sistemas de Informação, Faculdade Impacta, 2026).

A página tem duas partes:

- **Parte 1 – Para todos:** o que descobrimos, em linguagem simples, e uma dica para quem compra pela internet.
- **Parte 2 – Para quem trabalha com tecnologia:** resultados detalhados, exemplos de código e como reproduzir o experimento.

> A pesquisa foi anônima. Aqui só aparecem números agregados das 31 respostas. Nenhum dado permite identificar quem respondeu.

---

## Parte 1 – Para todos

### O que vocês nos contaram (31 respostas)

| | |
|---|---|
| **58%** | já leem a resposta pronta do buscador ou de uma IA, sem abrir o site de origem |
| **87%** | já usam IA, em algum grau, para ajudar a decidir uma compra |
| **48%** | quase sempre visitam o site que a IA indica, para conferir detalhes |
| **52%** | se preocupam com sites que perdem visitas por causa das respostas de IA |

Ou seja: cada vez mais gente recebe a resposta "pronta", e quem não aparece nessas respostas corre o risco de ficar invisível.

### O que testamos

Criamos páginas de uma loja virtual fictícia e pedimos a uma IA que fizesse a leitura delas o **preço**, a **nota**, o **número de avaliações**, o **vendedor** e se o produto estava **disponível**. Depois conferimos se ela acertou.

### O que descobrimos

1. **Quando a informação está escrita de forma clara na página, a IA acerta.** Uma "etiqueta" escondida no código com os dados do produto (chamada JSON-LD) deixou a IA mais segura da resposta, mas não mudou os acertos.
2. **Quando o site só aparece depois de carregar no navegador, a IA pode não enxergar nada.** Nesse caso, a etiqueta com os dados foi a única coisa que a IA conseguiu ler.
3. **A IA às vezes lê a página "em pedaços".** Quando o pedaço com o nome do vendedor ficou de fora, ela não soube dizer quem vendia o produto.
4. **Dados desatualizados confundem.** Numa página em que a etiqueta dizia um preço e o texto mostrava outro, a IA percebeu a diferença e ficou bem menos confiante.

### Dica para quem compra

Antes de fechar uma compra recomendada por uma IA, **confira no site da loja o preço, a disponibilidade e quem é o vendedor**. A resposta da IA pode estar incompleta ou desatualizada.

---

## Parte 2 – Para quem trabalha com tecnologia

### Como o experimento funciona

Tudo está em um único script, [`experiment.py`](experiment.py):

1. Lê a página como um rastreador **estático** (só o HTML inicial) ou **renderizado** (executa o JavaScript com Playwright).
2. Separa título, *meta tags*, bloco JSON-LD e texto visível (BeautifulSoup).
3. Monta o que chega ao LLM: a página inteira (**contexto integral**) ou só os 3 trechos de 60 palavras mais relevantes para a pergunta do usuário (**RAG simulado**, com BM25).
4. Pede ao modelo (`claude-sonnet-5-5`) os 8 campos do produto e duas notas que ele dá a si mesmo (eficácia e confiança).
5. Compara cada campo com o gabarito e calcula a **acurácia objetiva**.
6. Repete 3 vezes e consolida as médias com pandas.

As páginas testadas estão em [`pages/`](pages/) e os resultados brutos, em [`data/`](data/).

### Resultados (médias de 3 execuções)

| Configuração | Acurácia (página inteira) | Confiança (página inteira) | Acurácia (RAG) | Confiança (RAG) | JSON-LD recuperado no RAG |
|---|---|---|---|---|---|
| S1-A produto, só HTML | 1,00 | 0,92 | 1,00 | 0,90 | — |
| S1-B produto + JSON-LD | 1,00 | 0,97 | 1,00 | 0,95 | 67% |
| S2-A SPA, JSON-LD via JS (estático) | **0,00** | 0,00 | **0,00** | 0,00 | — |
| S2-A SPA, JSON-LD via JS (renderizado) | 1,00 | 0,97 | 1,00 | 0,96 | 100% |
| S2-B SPA, JSON-LD no HTML inicial (estático) | **1,00** | 0,94 | **1,00** | 0,94 | 100% |
| S2-B SPA, JSON-LD no HTML inicial (renderizado) | 1,00 | 0,97 | 1,00 | 0,96 | 100% |
| S3-A marketplace, sem JSON-LD | 1,00 | 0,86 | 0,88 | 0,68 | — |
| S3-B marketplace, JSON-LD consistente | 1,00 | 0,93 | 0,88 | 0,69 | 50% |
| S3-C marketplace, JSON-LD desatualizado | 1,00 | **0,55** | 0,88 | 0,62 | 50% |

### Exemplo de JSON-LD usado (Schema.org `Product`)

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Smartphone Nexo X12 Pro 256 GB - Grafite",
  "brand": { "@type": "Brand", "name": "Nexo" },
  "aggregateRating": { "@type": "AggregateRating", "ratingValue": 4.6, "bestRating": 5, "reviewCount": 1284 },
  "offers": {
    "@type": "Offer",
    "price": 3499.00,
    "priceCurrency": "BRL",
    "availability": "https://schema.org/InStock",
    "seller": { "@type": "Organization", "name": "Loja Exemplo" }
  }
}
</script>
```

### Diretrizes para aplicações web

1. **Entregue o JSON-LD no HTML inicial** (SSR, pré-renderização ou geração estática), sobretudo em SPAs. Injetado só via JavaScript, ele pode não existir para rastreadores que não executam JS (cenário S2-A).
2. **Gere o JSON-LD da mesma fonte de dados** que alimenta o preço e o estoque exibidos, para evitar divergências (cenário S3-C).
3. **Mantenha o bloco enxuto, com os atributos críticos no início** (preço, disponibilidade, vendedor, avaliação), para reduzir o risco de a fragmentação descartá-los (cenário S3, RAG).
4. **Repita no texto visível, de forma explícita, os mesmos fatos** declarados nos dados estruturados. Na maioria dos cenários, o texto visível foi suficiente para a extração correta.

### Como verificar o seu site

- **O JSON-LD está no HTML inicial?** Veja o código-fonte sem executar JavaScript:
  ```bash
  curl -s https://seu-site.com.br/produto | grep -A 20 'application/ld+json'
  ```
  Se nada aparecer, o bloco só existe depois que o navegador executa o JavaScript.
- **O JSON-LD é válido?** Teste a URL no [Schema Markup Validator](https://validator.schema.org/) ou no [Teste de pesquisa aprimorada do Google](https://search.google.com/test/rich-results).

### Reproduzir o experimento

```bash
cd pip install -r requirements.txt
python -m playwright install chromium
# coloque ANTHROPIC_API_KEY=... em um arquivo .env
python experiment.py --dry-run   # só leitura e fragmentação, sem custo de API
python experiment.py             # 54 chamadas ao modelo
```

Para testar outro modelo, troque `MODEL` no início do script.

### Limitações

Páginas sintéticas e de pequeno porte, um único modelo avaliado de forma *offline*, recuperação lexical (BM25) com parâmetros fixos e amostra de 31 respondentes, não probabilística. Os resultados são indicativos, não generalizáveis.

---

## Registro da devolutiva

Esta devolutiva foi enviada individualmente, pelo mesmo canal privado do convite, às pessoas convidadas a responder ao formulário.

| Item | Valor |
|---|---|
| Data de envio | 23 out. 2026 |
| Pessoas convidadas que receberam o link | 3 |
| Retornos recebidos | 3 |
| Nota de utilidade (1 a 5) | 5, 5, 4 |
| Nota média de utilidade (1 a 5) ||

*Retornos registrados até: _preencher_.*
