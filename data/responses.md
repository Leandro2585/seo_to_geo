# Respostas do modelo

## Execução 1 - S1-A - static - contexto_integral
```json
{
  "extraction_efficacy": 0.9,
  "confidence_index": 0.92,
  "qualitative_justification": "Não há JSON-LD (json_ld é null), então toda a extração depende do texto visível, que está bem organizado e sem ambiguidade para o produto principal. O nome do produto aparece no título da página e no cabeçalho do texto. A marca está explícita em 'Marca: Nexo' e no breadcrumb. O preço à vista (R$ 3.499,00) está separado do valor parcelado (12x de R$ 291,58), o que evita confusão. A disponibilidade ('Em estoque - envio imediato') e o vendedor ('Vendido e entregue por Loja Exemplo') estão em frases claras. A nota (4,6 de 5) e o total de avaliações (1.284) aparecem juntos na mesma linha. Os gargalos são: (1) ausência de dados estruturados, sem schema.org, o que obriga a interpretação de linguagem natural; (2) a moeda só é inferida pelo símbolo 'R$', sem código ISO explícito (BRL); (3) a seção 'Quem viu este produto também viu' traz outros produtos com preços, notas e vendedores que poderiam contaminar a extração se o escopo não fosse bem delimitado, inclusive um vendedor também chamado Loja Exemplo; (4) o review_count de 1.284 vem do resumo, e só três avaliações individuais estão visíveis, então o valor não pode ser verificado por contagem. Nenhum conhecimento externo foi necessário, apenas a conversão de 'R$' para BRL e de 'Em estoque' para InStock.",
  "extracted_entities": {
    "product_name": "Smartphone Nexo X12 Pro 256 GB - Grafite",
    "brand": "Nexo",
    "price": 3499.0,
    "currency": "BRL",
    "availability": "InStock",
    "rating_value": 4.6,
    "review_count": 1284,
    "seller": "Loja Exemplo"
  }
}
```

## Execução 1 - S1-A - static - rag_chunking
```json
{
  "extraction_efficacy": 0.93,
  "confidence_index": 0.9,
  "qualitative_justification": "Os dados necessários estão concentrados em um único fragmento de texto limpo e sequencial (nome do produto, marca, nota, número de avaliações, preço, disponibilidade e vendedor), o que facilitou muito a extração sem perda de contexto. Pontos de atenção: (1) não há marcação estruturada (JSON-LD/schema.org) nos fragmentos, então a extração depende de interpretação de texto livre, como 'Em estoque - envio imediato' para InStock; (2) o fragmento começa com um ruído ('200 MP') que não afeta a extração; (3) o preço à vista (R$ 3.499,00) foi distinguido do valor parcelado (12x de R$ 291,58), e a moeda BRL foi inferida a partir do símbolo 'R$'; (4) o vendedor 'Loja Exemplo' aparece em 'Vendido e entregue por' e é corroborado pelo título da página; (5) a nota e o número de avaliações estão em formato textual brasileiro (vírgula decimal, ponto de milhar), exigindo normalização, mas sem ambiguidade. Nenhum conhecimento externo foi necessário.",
  "extracted_entities": {
    "product_name": "Smartphone Nexo X12 Pro 256 GB - Grafite",
    "brand": "Nexo",
    "price": 3499.0,
    "currency": "BRL",
    "availability": "InStock",
    "rating_value": 4.6,
    "review_count": 1284,
    "seller": "Loja Exemplo"
  }
}
```

## Execução 1 - S1-B - static - contexto_integral
```json
{
  "extraction_efficacy": 0.97,
  "confidence_index": 0.98,
  "qualitative_justification": "A extração foi muito fácil porque a página traz um bloco JSON-LD schema.org do tipo Product completo e bem estruturado (name, brand, aggregateRating, offers com price, priceCurrency, availability e seller). O texto visível confirma todos os valores do JSON-LD: preço R$ 3.499,00, nota 4,6 de 5, 1.284 avaliações, 'Em estoque' e 'Vendido e entregue por Loja Exemplo'. Não há conflito entre as fontes. O único risco de ambiguidade está na seção 'Quem viu este produto também viu', que traz outros produtos com preços, notas e vendedores distintos (Nexo X10, Orbi S8, TechMais), mas o JSON-LD e o cabeçalho do produto permitem isolar a entidade principal sem dificuldade. O title e a meta description são mais genéricos (omitem a cor Grafite), então foi usado o nome do JSON-LD, mais específico. O preço parcelado (12x de R$ 291,58) não foi confundido com o preço à vista. Não foi necessário conhecimento externo.",
  "extracted_entities": {
    "product_name": "Smartphone Nexo X12 Pro 256 GB - Grafite",
    "brand": "Nexo",
    "price": 3499.0,
    "currency": "BRL",
    "availability": "InStock",
    "rating_value": 4.6,
    "review_count": 1284,
    "seller": "Loja Exemplo"
  }
}
```

## Execução 1 - S1-B - static - rag_chunking
```json
{
  "extraction_efficacy": 0.97,
  "confidence_index": 0.96,
  "qualitative_justification": "A extração foi muito fácil porque os dados aparecem em duas fontes que concordam entre si: o JSON-LD schema.org (Product, AggregateRating, Offer) e o texto visível da página. Preço (3499.0 / R$ 3.499,00), moeda (BRL), nota (4,6), quantidade de avaliações (1284), disponibilidade (schema.org/InStock, 'Em estoque - envio imediato') e vendedor (Organization 'Loja Exemplo', 'Vendido e entregue por Loja Exemplo') são consistentes entre as fontes. O nome do produto vem do título ('Smartphone Nexo X12 Pro 256 GB') e do breadcrumb, e a marca 'Nexo' aparece no texto ('Marca: Nexo'). Os gargalos são pequenos: o JSON-LD está fragmentado entre chunks, e o campo 'name' do Product está truncado em 'Smartphone Nexo', o que exigiu completar o nome com o título da página e o breadcrumb. O texto também menciona a cor Grafite, que não faz parte do título principal. O JSON-LD não traz o campo 'brand' explicitamente nos trechos disponíveis, mas a marca é confirmada no texto. O preço parcelado (12x de R$ 291,58) foi ignorado em favor do preço à vista, que coincide com o JSON-LD. Não foi necessário conhecimento externo.",
  "extracted_entities": {
    "product_name": "Smartphone Nexo X12 Pro 256 GB",
    "brand": "Nexo",
    "price": 3499.0,
    "currency": "BRL",
    "availability": "InStock",
    "rating_value": 4.6,
    "review_count": 1284,
    "seller": "Loja Exemplo"
  }
}
```

## Execução 1 - S2-A - static - contexto_integral
```json
{
  "extraction_efficacy": 0.0,
  "confidence_index": 0.0,
  "qualitative_justification": "A página extraída não contém nenhum dado de produto. O campo json_ld é nulo, não há metadados relevantes além do viewport (sem Open Graph, schema.org ou meta tags de produto), e o texto visível é apenas um aviso pedindo a habilitação do JavaScript. Isso indica que o conteúdo é renderizado no lado do cliente (SPA/CSR) e o scraping capturou somente o shell HTML inicial, sem a hidratação. O título 'Loja Exemplo' identifica apenas o nome do site, não um produto, e não é possível inferir com segurança o vendedor a partir dele. Nenhuma das entidades solicitadas (nome do produto, marca, preço, moeda, disponibilidade, avaliação, número de avaliações) pôde ser identificada sem recorrer a suposições ou conhecimento externo. Para viabilizar a extração, seria necessário renderizar a página com um navegador headless (executando JavaScript), aguardar o carregamento dinâmico ou acessar APIs/endpoints de dados que alimentam o front-end.",
  "extracted_entities": {
    "product_name": null,
    "brand": null,
    "price": null,
    "currency": null,
    "availability": null,
    "rating_value": null,
    "review_count": null,
    "seller": null
  }
}
```

## Execução 1 - S2-A - static - rag_chunking
```json
{
  "extraction_efficacy": 0.0,
  "confidence_index": 0.0,
  "qualitative_justification": "O único fragmento recuperado corresponde a uma página 'casca' (shell) que exige JavaScript: contém apenas o título genérico 'Loja Exemplo', uma meta tag de viewport e a mensagem 'Habilite o JavaScript para utilizar a Loja Exemplo'. Isso indica uma aplicação renderizada no cliente (SPA/CSR), em que o conteúdo do produto é injetado dinamicamente após a execução de scripts, e o scraper capturou apenas o HTML estático inicial. Não há nenhuma menção ao produto 'Nexo X12 Pro 256 GB', nem preço, moeda, disponibilidade, nota, número de avaliações ou vendedor. Também não há dados estruturados (JSON-LD, schema.org, Open Graph ou microdados) que pudessem servir de alternativa. O principal gargalo é a ausência total de conteúdo renderizado. Para obter os dados seria necessário usar renderização com navegador headless, interceptar as chamadas de API/XHR da página ou acessar um feed de produtos. Inferir qualquer valor exigiria conhecimento externo ou invenção, então todas as entidades foram retornadas como null.",
  "extracted_entities": {
    "product_name": null,
    "brand": null,
    "price": null,
    "currency": null,
    "availability": null,
    "rating_value": null,
    "review_count": null,
    "seller": null
  }
}
```

## Execução 1 - S2-A - rendered - contexto_integral
```json
{
  "extraction_efficacy": 0.98,
  "confidence_index": 0.97,
  "qualitative_justification": "A extração foi muito fácil porque o JSON-LD segue o schema.org (Product, Brand, AggregateRating, Offer e Organization) e traz todas as entidades solicitadas em campos explícitos e tipados: nome, marca, preço numérico (3499), moeda (BRL), disponibilidade (InStock), nota (4.6), número de avaliações (1284) e vendedor (Loja Exemplo). O texto visível confirma todos os valores (R$ 3.499,00 à vista, 4,6 de 5 estrelas, 1.284 avaliações, 'Em estoque', 'Vendido e entregue por Loja Exemplo'), sem divergência entre as fontes. O principal gargalo é o ruído no texto visível: a seção 'Quem viu este produto também viu' traz produtos concorrentes com preços, notas e vendedores diferentes (Nexo X10, Orbi S8, TechMais), o que poderia contaminar a extração se fosse feita só pelo texto. O aviso 'Habilite o JavaScript' sugere renderização dependente de JS, mas os dados estruturados já estavam no HTML inicial. O preço de 12x de R$ 291,58 é apenas parcelamento e não deve ser confundido com o preço principal. As avaliações individuais (5, 4 e 3 estrelas) são uma amostra e não alteram a média agregada. Não foi preciso conhecimento externo.",
  "extracted_entities": {
    "product_name": "Smartphone Nexo X12 Pro 256 GB - Grafite",
    "brand": "Nexo",
    "price": 3499,
    "currency": "BRL",
    "availability": "InStock",
    "rating_value": 4.6,
    "review_count": 1284,
    "seller": "Loja Exemplo"
  }
}
```

## Execução 1 - S2-A - rendered - rag_chunking
```json
{
  "extraction_efficacy": 0.97,
  "confidence_index": 0.96,
  "qualitative_justification": "Os fragmentos, embora recuperados fora de ordem e truncados, trazem informações redundantes e consistentes entre o JSON-LD (schema.org Product/Offer/AggregateRating) e o texto visível da página. Facilidades: o JSON-LD fornece valores tipados e sem ambiguidade (price 3499, priceCurrency BRL, availability schema.org/InStock, ratingValue 4.6, reviewCount 1284, seller Loja Exemplo, brand Nexo), e o texto visível confirma tudo (R$ 3.499,00, 4,6 de 5 estrelas, 1.284 avaliações, 'Em estoque - envio imediato', 'Vendido e entregue por Loja Exemplo'). Gargalos: o JSON-LD está dividido entre dois fragmentos (o ratingValue é cortado no fragmento 3 e continua no 2), exigindo remontagem; o nome do produto no JSON-LD aparece completo apenas no fragmento 3 e a variante de cor (Grafite) faz parte do nome. O preço parcelado (12x de R$ 291,58) é ruído potencial, mas é claramente distinguível do preço à vista. Há também o ruído 'Habilite o JavaScript', irrelevante. Nenhum conhecimento externo foi necessário; a pequena redução na confiança se deve à truncagem dos fragmentos e à ausência de data de validade do preço.",
  "extracted_entities": {
    "product_name": "Smartphone Nexo X12 Pro 256 GB - Grafite",
    "brand": "Nexo",
    "price": 3499,
    "currency": "BRL",
    "availability": "InStock",
    "rating_value": 4.6,
    "review_count": 1284,
    "seller": "Loja Exemplo"
  }
}
```

## Execução 1 - S2-B - static - contexto_integral
```json
{
  "extraction_efficacy": 0.97,
  "confidence_index": 0.93,
  "qualitative_justification": "A extração foi muito facilitada pelo bloco JSON-LD com schema.org (@type Product), que traz todas as entidades solicitadas em campos explícitos e tipados: name, brand.name, offers.price (numérico), priceCurrency (BRL), availability (URL schema.org/InStock), aggregateRating (ratingValue e reviewCount) e offers.seller.name. Não houve ambiguidade nem necessidade de inferência ou conhecimento externo. O principal gargalo é que o visible_text contém apenas um aviso de JavaScript desabilitado, então não foi possível validar os dados contra o conteúdo renderizado da página (por exemplo, se preço e estoque exibidos coincidem com o JSON-LD). Os metadados também são mínimos (apenas viewport, sem description ou Open Graph), o que reduz a possibilidade de verificação cruzada e justifica uma pequena redução na confiança. Ainda assim, a estrutura é consistente e coerente internamente (título da loja coincide com o seller, URL da oferta coerente com o produto).",
  "extracted_entities": {
    "product_name": "Smartphone Nexo X12 Pro 256 GB - Grafite",
    "brand": "Nexo",
    "price": 3499.0,
    "currency": "BRL",
    "availability": "InStock",
    "rating_value": 4.6,
    "review_count": 1284,
    "seller": "Loja Exemplo"
  }
}
```

## Execução 1 - S2-B - static - rag_chunking
```json
{
  "extraction_efficacy": 0.95,
  "confidence_index": 0.93,
  "qualitative_justification": "A extração foi facilitada pela presença de um bloco JSON-LD schema.org do tipo Product, que traz todas as entidades solicitadas de forma estruturada e com tipos corretos (price como número 3499.0, priceCurrency 'BRL', availability como URL schema.org/InStock, ratingValue 4.6, reviewCount 1284 e seller como Organization 'Loja Exemplo'). O principal gargalo foi o fatiamento (chunking): o objeto JSON-LD foi cortado no meio do campo 'ratingValue' entre o primeiro e o segundo fragmento, e foi necessário reconstruir o objeto usando a sobreposição de texto ('armazenamento e bateria de 5.000 mAh') para recuperar a nota sem perder contexto. Pontos de atenção: o texto visível da página contém apenas o aviso 'Habilite o JavaScript', indicando que a página é renderizada via JavaScript e que não há conteúdo HTML visível para validação cruzada do preço ou da disponibilidade. O nome do produto no JSON-LD ('Smartphone Nexo X12 Pro 256 GB - Grafite') corresponde à consulta, com a variante de cor Grafite como detalhe adicional. A confiança é alta porque nenhum conhecimento externo foi necessário, mas não é máxima, pois os dados dependem exclusivamente dos metadados, sem confirmação no conteúdo renderizado nem data de atualização do preço.",
  "extracted_entities": {
    "product_name": "Smartphone Nexo X12 Pro 256 GB - Grafite",
    "brand": "Nexo",
    "price": 3499.0,
    "currency": "BRL",
    "availability": "InStock",
    "rating_value": 4.6,
    "review_count": 1284,
    "seller": "Loja Exemplo"
  }
}
```

## Execução 1 - S2-B - rendered - contexto_integral
```json
{
  "extraction_efficacy": 0.98,
  "confidence_index": 0.97,
  "qualitative_justification": "A extração foi muito fácil graças ao JSON-LD schema.org do tipo Product, que traz todas as entidades solicitadas em campos explícitos e tipados: name, brand.name, offers.price (número 3499.0), priceCurrency (BRL), availability (URL schema.org/InStock), aggregateRating.ratingValue (4.6), reviewCount (1284) e offers.seller.name. O texto visível confirma todos os valores (R$ 3.499,00, 'Em estoque', 4,6 de 5 estrelas, 1.284 avaliações, 'Vendido e entregue por Loja Exemplo'), sem divergências entre as fontes. Não houve necessidade de conhecimento externo. Pontos de atenção menores: o texto visível traz a mensagem 'Habilite o JavaScript', o que sugere renderização parcial por JS, mas isso não afetou os dados, já presentes no JSON-LD; a seção 'Quem viu este produto também viu' contém outros produtos, preços, notas e vendedores (Nexo X10, Orbi S8, TechMais) que poderiam gerar ambiguidade se o parser lesse apenas o texto, mas foram descartados por estarem fora do escopo do produto principal. O metadado de página é pobre (apenas viewport, sem description ou Open Graph), e o título da página ('Loja Exemplo') não identifica o produto, então o JSON-LD é a fonte mais confiável.",
  "extracted_entities": {
    "product_name": "Smartphone Nexo X12 Pro 256 GB - Grafite",
    "brand": "Nexo",
    "price": 3499.0,
    "currency": "BRL",
    "availability": "InStock",
    "rating_value": 4.6,
    "review_count": 1284,
    "seller": "Loja Exemplo"
  }
}
```

## Execução 1 - S2-B - rendered - rag_chunking
```json
{
  "extraction_efficacy": 0.97,
  "confidence_index": 0.96,
  "qualitative_justification": "A extração foi muito fácil porque os dados aparecem em duas fontes que concordam entre si: o JSON-LD (schema.org Product, com AggregateRating e Offer) e o texto visível da página. Preço (3499.0 / R$ 3.499,00), moeda (BRL), nota (4.6), contagem de avaliações (1284), disponibilidade (schema.org/InStock, 'Em estoque - envio imediato') e vendedor (Loja Exemplo) coincidem nas duas fontes. O nome do produto e a marca também são consistentes (JSON-LD e texto). Os gargalos são pequenos: o JSON-LD está fragmentado entre os trechos, e o ratingValue aparece cortado no terceiro fragmento, mas o valor é recuperado no segundo. O texto de 'Habilite o JavaScript' é ruído irrelevante. O preço de 12x de R$ 291,58 é parcelamento, não o preço principal, e não gera ambiguidade. Nenhum conhecimento externo foi necessário. A confiança não chega a 1.0 porque a reconstrução do JSON-LD depende da junção de fragmentos e nenhum deles mostra o objeto completo.",
  "extracted_entities": {
    "product_name": "Smartphone Nexo X12 Pro 256 GB - Grafite",
    "brand": "Nexo",
    "price": 3499.0,
    "currency": "BRL",
    "availability": "InStock",
    "rating_value": 4.6,
    "review_count": 1284,
    "seller": "Loja Exemplo"
  }
}
```

## Execução 1 - S3-A - static - contexto_integral
```json
{
  "extraction_efficacy": 0.82,
  "confidence_index": 0.85,
  "qualitative_justification": "Não há JSON-LD (json_ld é null), então toda a extração dependeu do texto visível, que é razoavelmente bem estruturado e em linguagem natural. Facilidades: o nome do produto, a marca ('Marca: Nexo'), o preço atual ('por R$ 3.499,00'), a disponibilidade ('Em estoque'), a nota do produto (4,6) e o número de avaliações (1.284) aparecem de forma explícita e próximos entre si. O vendedor principal ('Vendido e entregue por Loja Exemplo') também está claro. Gargalos: (1) há múltiplos preços concorrentes no mesmo texto (preço 'De' R$ 3.999,00, preço à vista no PIX R$ 3.324,05, parcelas de R$ 349,90, ofertas de outros vendedores como TechMais e MegaCell, e o preço de entrada R$ 899,00 do banner promocional, que não se refere a este produto), exigindo desambiguação semântica e sem marcação estruturada; escolhi o preço promocional regular como preço principal. (2) Existem duas notas distintas, a do produto (4,6 com 1.284 avaliações) e a reputação da loja (4,8 com 25.390 avaliações), o que gera risco de confusão; usei a do produto. (3) A moeda não está em campo próprio, mas é inferida do símbolo 'R$' (BRL). (4) Ofertas de outros vendedores, incluindo um item recondicionado, e as Q&A/avaliações de clientes poluem o contexto, e o comentário de 'outro vendedor' sugere possível mistura de avaliações entre vendedores. (5) A descrição meta menciona 'até 12% de desconto', que é só marketing e não corresponde a um valor de preço. Nenhum conhecimento externo foi necessário, mas a ausência de dados estruturados reduz a confiança.",
  "extracted_entities": {
    "product_name": "Nexo X12 Pro 256GB 12GB RAM Câmera 200MP Tela 6.7\" - Grafite",
    "brand": "Nexo",
    "price": 3499.0,
    "currency": "BRL",
    "availability": "InStock",
    "rating_value": 4.6,
    "review_count": 1284,
    "seller": "Loja Exemplo"
  }
}
```

## Execução 1 - S3-A - static - rag_chunking
```json
{
  "extraction_efficacy": 0.82,
  "confidence_index": 0.72,
  "qualitative_justification": "Facilidades: o segundo fragmento traz em texto corrido quase todos os dados pedidos, com rótulos claros: nome do produto, 'Marca: Nexo', 'Nota do produto: 4,6 (1.284 avaliações de compradores)', preço promocional R$ 3.499,00 e 'Em estoque'. O fragmento de perguntas e respostas confirma que a versão de 256 GB está disponível e que a de 512 GB está esgotada, o que reforça a disponibilidade da variante pedida. Gargalos: (1) Não há JSON-LD nem microdados schema.org (Product/Offer/AggregateRating), então tudo depende da interpretação de texto solto, sem marcação semântica. (2) O vendedor não aparece de forma explícita. 'Loja Exemplo Marketplace' é o nome do marketplace, e a meta description diz 'ofertas de vários vendedores', então o vendedor real do anúncio não pode ser identificado sem inferência. Por isso seller = null. (3) Há vários valores monetários concorrentes (R$ 899,00 do banner, R$ 3.999,00 riscado, R$ 3.499,00 vigente, R$ 3.324,05 no PIX, parcelas de R$ 349,90). Escolhi R$ 3.499,00 como preço base, por ser o 'por' da promoção; o preço no PIX é condicional. (4) Os fragmentos estão truncados (a avaliação de 'Rafael T.' está cortada) e há inconsistência leve entre o '12% de desconto' da meta description e o desconto real de cerca de 12,5% (3.999 → 3.499). Isso não afeta os campos extraídos. (5) O ano '2026' e a cor 'Grafite' vêm apenas do texto, sem validação estruturada.",
  "extracted_entities": {
    "product_name": "Nexo X12 Pro 256GB 12GB RAM Câmera 200MP Tela 6.7\" Grafite",
    "brand": "Nexo",
    "price": 3499.0,
    "currency": "BRL",
    "availability": "InStock",
    "rating_value": 4.6,
    "review_count": 1284,
    "seller": null
  }
}
```

## Execução 1 - S3-B - static - contexto_integral
```json
{
  "extraction_efficacy": 0.95,
  "confidence_index": 0.93,
  "qualitative_justification": "Facilidades: o bloco JSON-LD (schema.org/Product) está completo e traz nome, marca, preço, moeda, disponibilidade, nota, número de avaliações e vendedor em campos tipados, sem ambiguidade de formato. O texto visível confirma todos esses valores (R$ 3.499,00, nota 4,6, 1.284 avaliações, 'Em estoque', 'Vendido e entregue por Loja Exemplo'), o que dá consistência entre as duas fontes. Gargalos: (1) o texto visível contém ruído que poderia gerar confusão, como o preço antigo (R$ 3.999,00), o preço no PIX (R$ 3.324,05), o preço de entrada da campanha (R$ 899,00) e ofertas de outros vendedores (TechMais R$ 3.459,00; MegaCell recondicionado R$ 2.799,00); (2) existem várias notas (produto 4,6, loja 4,8 com 25.390 avaliações, vendedor TechMais 4,1), e só a nota do produto deve ser usada; (3) o título e a descrição meta falam em 'até 12% de desconto', o que não corresponde a um valor de preço; (4) há divergência leve de nomenclatura entre o JSON-LD ('Smartphone Nexo X12 Pro 256 GB - Grafite') e o texto visível ('Nexo X12 Pro 256GB 12GB RAM Câmera 200MP Tela 6.7\" - Grafite'). Optei pelo nome do JSON-LD por ser estruturado e canônico. O JSON-LD só declara a oferta da Loja Exemplo, sem os demais vendedores, o que reduz o risco de mistura. Nenhum conhecimento externo foi necessário.",
  "extracted_entities": {
    "product_name": "Smartphone Nexo X12 Pro 256 GB - Grafite",
    "brand": "Nexo",
    "price": 3499.0,
    "currency": "BRL",
    "availability": "InStock",
    "rating_value": 4.6,
    "review_count": 1284,
    "seller": "Loja Exemplo"
  }
}
```

## Execução 1 - S3-B - static - rag_chunking
```json
{
  "extraction_efficacy": 0.72,
  "confidence_index": 0.68,
  "qualitative_justification": "Facilidades: o fragmento 2 concentra quase todas as entidades em texto corrido e com rótulos claros (marca, modelo, nota 4,6, 1.284 avaliações, preço, 'Em estoque'). O fragmento 1 confirma que a versão de 256 GB está disponível, e o fragmento 3 traz o nome do produto no JSON-LD. Gargalos: (1) o vendedor não pôde ser identificado, porque o texto termina em 'Vendido e entregue' e o nome foi cortado. 'Loja Exemplo Marketplace' aparece apenas no título e na descrição como nome da plataforma, que reúne vários vendedores, então não é prova de quem vende. Por isso seller ficou null. (2) O JSON-LD está truncado em 'brand', sem offers nem aggregateRating, então os dados estruturados não puderam validar preço, estoque ou nota. A marca 'Nexo' veio do texto livre. (3) Há vários valores de preço no mesmo trecho: 'a partir de R$ 899,00' (outros celulares), 'De R$ 3.999,00' (preço riscado), R$ 3.499,00 (preço atual), R$ 3.324,05 (PIX) e 10x de R$ 349,90. Foi escolhido R$ 3.499,00 como preço atual, por inferência da estrutura 'De... por...'. (4) A descrição fala em 'até 12% de desconto', o que não bate com o desconto exibido de cerca de 12,5% sobre o preço de lista. É compatível, mas não é um dado confiável. (5) Os fragmentos são desconexos, e o de Q&A e avaliações está cortado no início e no fim. A disponibilidade foi inferida de 'Em estoque' mais a resposta do Q&A, de forma consistente.",
  "extracted_entities": {
    "product_name": "Smartphone Nexo X12 Pro 256 GB - Grafite",
    "brand": "Nexo",
    "price": 3499.0,
    "currency": "BRL",
    "availability": "InStock",
    "rating_value": 4.6,
    "review_count": 1284,
    "seller": null
  }
}
```

## Execução 1 - S3-C - static - contexto_integral
```json
{
  "extraction_efficacy": 0.62,
  "confidence_index": 0.55,
  "qualitative_justification": "O JSON-LD está bem estruturado e traz todas as entidades pedidas, mas contradiz o texto visível em quatro campos. Preço: o JSON-LD diz 3999,00, que no texto visível é o valor riscado ('De'), e o preço vigente é R$ 3.499,00. Disponibilidade: o JSON-LD diz OutOfStock, e o texto visível diz 'Em estoque'. O Q&A confirma que a versão de 256 GB está disponível. Nota: o JSON-LD diz 4,4, e o texto visível diz 4,6. Avaliações: o JSON-LD diz 1102, e o texto visível diz 1.284. O JSON-LD parece desatualizado (cache ou dado antigo). Escolhi o texto visível, que é internamente consistente e corroborado pelo Q&A, mas isso exigiu uma inferência e reduziu a confiança. Outros pontos de atenção: há ruído de ofertas concorrentes (TechMais por R$ 3.459,00 e MegaCell recondicionado por R$ 2.799,00), do preço PIX (R$ 3.324,05), do preço de entrada da campanha (R$ 899,00) e da reputação da loja (4,8, com 25.390 avaliações), que não deve ser confundida com a nota do produto. O vendedor principal ('Loja Exemplo') é consistente nas duas fontes. A marca também é consistente (Nexo). Como o preço cobrado não é inequívoco, a extração não é totalmente livre de ambiguidade.",
  "extracted_entities": {
    "product_name": "Smartphone Nexo X12 Pro 256 GB - Grafite",
    "brand": "Nexo",
    "price": 3499.0,
    "currency": "BRL",
    "availability": "InStock",
    "rating_value": 4.6,
    "review_count": 1284,
    "seller": "Loja Exemplo"
  }
}
```

## Execução 1 - S3-C - static - rag_chunking
```json
{
  "extraction_efficacy": 0.72,
  "confidence_index": 0.66,
  "qualitative_justification": "Facilidades: o fragmento 2 traz em texto corrido quase todos os dados pedidos: marca (Nexo), modelo, nota (4,6), número de avaliações (1.284), preço atual (R$ 3.499,00) e disponibilidade (\"Em estoque\"). O fragmento 1 confirma que a versão de 256 GB está disponível, e o nome do produto é consistente entre o texto e o título/JSON-LD. Gargalos: (1) O vendedor não pôde ser extraído: o texto termina em \"Vendido e entregue\", sem o nome. O fragmento 3 indica que a página é um marketplace com vários vendedores, então inferir o seller seria especulação e ele foi marcado como null. (2) Há vários valores monetários concorrentes (R$ 899,00 de uma faixa genérica de celulares, R$ 3.999,00 riscado, R$ 3.499,00, R$ 3.324,05 no PIX e parcelas de R$ 349,90). Escolhi R$ 3.499,00 como preço vigente, mas essa escolha depende de interpretar o padrão \"De X por Y\". (3) O JSON-LD está truncado em \"brand\": {\"@type\":, então não há dados estruturados de offers, aggregateRating ou seller. Tudo vem de texto não estruturado, mais sujeito a ambiguidade. (4) Os fragmentos estão fora de ordem e cortados, o que reduz o contexto. (5) Em marketplace, o preço e a disponibilidade podem variar por vendedor, e não há como confirmar a qual oferta o bloco de texto se refere.",
  "extracted_entities": {
    "product_name": "Smartphone Nexo X12 Pro 256 GB - Grafite",
    "brand": "Nexo",
    "price": 3499.0,
    "currency": "BRL",
    "availability": "InStock",
    "rating_value": 4.6,
    "review_count": 1284,
    "seller": null
  }
}
```

## Execução 2 - S1-A - static - contexto_integral
```json
{
  "extraction_efficacy": 0.9,
  "confidence_index": 0.92,
  "qualitative_justification": "Facilidades: a ausência de JSON-LD (json_ld: null) foi compensada por um visible_text bem estruturado e semanticamente claro. Todas as entidades solicitadas aparecem em linhas rotuladas ou com padrões inequívocos: nome do produto no título/H1 ('Smartphone Nexo X12 Pro 256 GB - Grafite'), marca explícita ('Marca: Nexo'), preço à vista com símbolo de moeda (R$ 3.499,00), disponibilidade ('Em estoque - envio imediato'), nota e contagem de avaliações ('4,6 de 5 estrelas (1.284 avaliações)') e vendedor ('Vendido e entregue por Loja Exemplo'). Gargalos: (1) sem dados estruturados, a extração depende de heurísticas de texto e não de um schema validável; (2) o formato numérico brasileiro (vírgula decimal, ponto de milhar) exige normalização cuidadosa; (3) há preços e avaliações de produtos relacionados (Nexo X10, Orbi S8) no mesmo texto, o que cria risco de contaminação, mas o contexto de seção ('Quem viu este produto também viu') permite descartá-los; (4) existem dois valores de preço (à vista e parcelado 12x de R$ 291,58), sendo escolhido o preço à vista como principal; (5) o nome do produto inclui a cor 'Grafite' no texto visível, mas não no title, e optou-se pelo nome mais completo; (6) as 3 opiniões individuais não refletem a média, e a nota agregada foi usada corretamente. Nenhum conhecimento externo foi necessário.",
  "extracted_entities": {
    "product_name": "Smartphone Nexo X12 Pro 256 GB - Grafite",
    "brand": "Nexo",
    "price": 3499.0,
    "currency": "BRL",
    "availability": "InStock",
    "rating_value": 4.6,
    "review_count": 1284,
    "seller": "Loja Exemplo"
  }
}
```

## Execução 2 - S1-A - static - rag_chunking
```json
{
  "extraction_efficacy": 0.93,
  "confidence_index": 0.9,
  "qualitative_justification": "As entidades pedidas aparecem de forma clara e contígua no primeiro fragmento, em texto corrido legível: nome do produto com capacidade e cor ('Smartphone Nexo X12 Pro 256 GB - Grafite'), marca ('Marca: Nexo'), nota e contagem de avaliações ('4,6 de 5 estrelas (1.284 avaliações)'), preço à vista ('R$ 3.499,00'), disponibilidade ('Em estoque - envio imediato') e vendedor ('Vendido e entregue por Loja Exemplo'). O título e o terceiro fragmento corroboram o nome do produto e o vendedor. Os gargalos são: (1) ausência de dados estruturados (JSON-LD/schema.org, microdados), o que obriga a inferir a moeda a partir do símbolo 'R$' e a mapear 'Em estoque' para InStock; (2) o número '200 MP' no início do primeiro fragmento é um ruído de truncamento, sem prejuízo para as entidades; (3) o preço parcelado (12x de R$ 291,58) poderia gerar ambiguidade, mas o rótulo 'à vista' a resolve; (4) formatos numéricos brasileiros (vírgula decimal, ponto de milhar) exigem normalização cuidadosa; (5) 'Loja Exemplo' é o único vendedor citado, sem distinguir marketplace de loja própria, e não há data de atualização do preço. Nenhum conhecimento externo foi necessário.",
  "extracted_entities": {
    "product_name": "Smartphone Nexo X12 Pro 256 GB - Grafite",
    "brand": "Nexo",
    "price": 3499.0,
    "currency": "BRL",
    "availability": "InStock",
    "rating_value": 4.6,
    "review_count": 1284,
    "seller": "Loja Exemplo"
  }
}
```

## Execução 2 - S1-B - static - contexto_integral
```json
{
  "extraction_efficacy": 0.98,
  "confidence_index": 0.97,
  "qualitative_justification": "A extração foi muito fácil porque a página traz um bloco JSON-LD schema.org do tipo Product, completo e bem estruturado, com name, brand, aggregateRating (ratingValue e reviewCount), offers (price, priceCurrency, availability, seller). Todos os campos solicitados estão em formatos tipados: preço como número (3499.0), moeda em código ISO (BRL), disponibilidade como URL schema.org/InStock. O texto visível confirma os mesmos valores (R$ 3.499,00, 4,6 de 5, 1.284 avaliações, 'Em estoque', 'Vendido e entregue por Loja Exemplo'), sem divergência entre as fontes, o que dispensa conhecimento externo. Os únicos pontos de atenção são o ruído dos produtos relacionados na seção 'Quem viu este produto também viu' (Nexo X10 e Orbi S8, com preços, notas e vendedores diferentes), que poderia causar confusão em um extrator baseado apenas em texto, e a pequena diferença entre o título da página ('Nexo X12 Pro 256 GB') e o nome no JSON-LD, que inclui a cor ('- Grafite'). Também há variações de formatação numérica (vírgula decimal e ponto de milhar no texto visível) e preço parcelado (12x de R$ 291,58) que não deve ser confundido com o preço à vista. Nenhum desses pontos compromete a identificação, pois o JSON-LD é inequívoco.",
  "extracted_entities": {
    "product_name": "Smartphone Nexo X12 Pro 256 GB - Grafite",
    "brand": "Nexo",
    "price": 3499.0,
    "currency": "BRL",
    "availability": "InStock",
    "rating_value": 4.6,
    "review_count": 1284,
    "seller": "Loja Exemplo"
  }
}
```

## Execução 2 - S1-B - static - rag_chunking
```json
{
  "extraction_efficacy": 0.95,
  "confidence_index": 0.95,
  "qualitative_justification": "A extração foi facilitada pela redundância entre o JSON-LD (schema.org Product, AggregateRating e Offer) e o texto visível da página. Os valores coincidem nas duas fontes: preço R$ 3.499,00 (3499.0 BRL), nota 4,6 (ratingValue 4.6), 1.284 avaliações (reviewCount 1284), disponibilidade InStock (também 'Em estoque - envio imediato') e vendedor Loja Exemplo (seller.name e 'Vendido e entregue por Loja Exemplo'). A marca aparece em 'Marca: Nexo', no breadcrumb e no título. Os gargalos são pequenos: os fragmentos estão truncados, e o JSON-LD aparece dividido entre dois trechos, então o campo 'name' do schema não está completo. O nome do produto foi reconstruído pelo título da página e pelo texto 'Smartphone Nexo X12 Pro 256 GB - Grafite'. A variante de cor (Grafite) aparece no texto, mas não foi mencionada na consulta. O preço à vista foi usado, e não o parcelado (12x de R$ 291,58), que é só uma condição de pagamento. Nenhum conhecimento externo foi necessário.",
  "extracted_entities": {
    "product_name": "Smartphone Nexo X12 Pro 256 GB",
    "brand": "Nexo",
    "price": 3499.0,
    "currency": "BRL",
    "availability": "InStock",
    "rating_value": 4.6,
    "review_count": 1284,
    "seller": "Loja Exemplo"
  }
}
```

## Execução 2 - S2-A - static - contexto_integral
```json
{
  "extraction_efficacy": 0.0,
  "confidence_index": 0.0,
  "qualitative_justification": "A página retornou apenas um aviso solicitando a habilitação do JavaScript, o que indica uma aplicação renderizada no cliente (SPA) cujo conteúdo não estava presente no HTML estático extraído. Não há JSON-LD (json_ld é null), nem metadados relevantes (apenas viewport), nem texto visível com informações de produto. O único dado disponível é o título genérico 'Loja Exemplo', que identifica o nome da loja mas não permite inferir com segurança vendedor, marca ou produto. Nenhuma das entidades solicitadas (nome do produto, marca, preço, moeda, disponibilidade, avaliação, número de avaliações) pôde ser identificada sem recorrer a suposições ou conhecimento externo. O principal gargalo é a dependência de renderização JavaScript; seria necessário utilizar um navegador headless (por exemplo, Playwright ou Puppeteer) ou acessar uma API/endpoint de dados do site para obter o conteúdo real.",
  "extracted_entities": {
    "product_name": null,
    "brand": null,
    "price": null,
    "currency": null,
    "availability": null,
    "rating_value": null,
    "review_count": null,
    "seller": null
  }
}
```

## Execução 2 - S2-A - static - rag_chunking
```json
{
  "extraction_efficacy": 0.0,
  "confidence_index": 0.0,
  "qualitative_justification": "O único fragmento recuperado contém apenas o título genérico da página (Loja Exemplo), a meta tag viewport e o aviso 'Habilite o JavaScript para utilizar a Loja Exemplo'. Isso indica que a página é renderizada no lado do cliente (SPA) e o scraping capturou apenas o shell HTML, sem o conteúdo dinâmico. Não há nenhuma menção ao produto Nexo X12 Pro 256 GB, nem a preço, moeda, disponibilidade, nota média, número de avaliações ou vendedor. Também não há dados estruturados (JSON-LD, schema.org, Open Graph de produto) que pudessem servir de alternativa. Como o gargalo é a ausência total de conteúdo relevante, nenhuma entidade pôde ser extraída, e qualquer resposta exigiria inventar valores ou recorrer a conhecimento externo. Recomenda-se refazer a coleta com um navegador headless que execute JavaScript, ou acessar uma API ou endpoint de dados do produto.",
  "extracted_entities": {
    "product_name": null,
    "brand": null,
    "price": null,
    "currency": null,
    "availability": null,
    "rating_value": null,
    "review_count": null,
    "seller": null
  }
}
```

## Execução 2 - S2-A - rendered - contexto_integral
```json
{
  "extraction_efficacy": 0.98,
  "confidence_index": 0.97,
  "qualitative_justification": "A extração foi muito fácil porque o JSON-LD segue o schema.org Product com todas as entidades pedidas em campos explícitos e tipados: name, brand.name, offers.price (número 3499), priceCurrency (BRL), availability (URL schema.org/InStock), aggregateRating (ratingValue 4.6 e reviewCount 1284) e offers.seller.name. O texto visível confirma todos os valores (R$ 3.499,00 à vista, 4,6 de 5 estrelas, 1.284 avaliações, Em estoque, Vendido e entregue por Loja Exemplo), sem contradições entre as duas fontes. Pontos de atenção menores: (1) o texto visível traz a mensagem 'Habilite o JavaScript', indicando que parte da página pode depender de JS, mas isso não afetou os dados, já presentes no JSON-LD; (2) a seção 'Quem viu este produto também viu' contém outros produtos com preços, notas e vendedores distintos (Nexo X10, Orbi S8), que são um risco de contaminação por ruído para extratores baseados apenas em texto, mas foram desconsiderados por pertencerem a itens relacionados; (3) o preço parcelado (12x de R$ 291,58) difere do preço à vista, mas o JSON-LD deixa claro que o preço de referência é 3499. Nenhum conhecimento externo foi necessário.",
  "extracted_entities": {
    "product_name": "Smartphone Nexo X12 Pro 256 GB - Grafite",
    "brand": "Nexo",
    "price": 3499,
    "currency": "BRL",
    "availability": "InStock",
    "rating_value": 4.6,
    "review_count": 1284,
    "seller": "Loja Exemplo"
  }
}
```

## Execução 2 - S2-A - rendered - rag_chunking
```json
{
  "extraction_efficacy": 0.97,
  "confidence_index": 0.96,
  "qualitative_justification": "Facilidades: os dados aparecem em duas fontes redundantes e consistentes entre si, o JSON-LD schema.org (Product, AggregateRating, Offer, Brand) e o texto visível da página. Ambas trazem nota 4,6, 1.284 avaliações, preço de R$ 3.499,00 (3499 BRL), disponibilidade InStock e vendedor Loja Exemplo. O JSON-LD tem tipos explícitos (price numérico, priceCurrency BRL, availability como URL schema.org/InStock), o que elimina ambiguidade de formato. O texto visível confirma os valores ('Em estoque - envio imediato', 'Vendido e entregue por Loja Exemplo'). Gargalos: os fragmentos são truncados e se sobrepõem. O JSON-LD está cortado entre o primeiro fragmento (que termina em 'ratingValue':) e o segundo, que começa no meio da descrição, e o objeto Product inteiro precisa ser remontado a partir de pedaços. O nome do produto aparece completo no JSON-LD ('Smartphone Nexo X12 Pro 256 GB - Grafite') e no texto, mas a variante 'Grafite' pode ser um detalhe a mais em relação à consulta, que não especifica cor. Há ruído irrelevante, como 'Habilite o JavaScript' e metadados de viewport. O parcelamento (12x de R$ 291,58) não conflita com o preço à vista. Nenhum conhecimento externo foi necessário.",
  "extracted_entities": {
    "product_name": "Smartphone Nexo X12 Pro 256 GB - Grafite",
    "brand": "Nexo",
    "price": 3499,
    "currency": "BRL",
    "availability": "InStock",
    "rating_value": 4.6,
    "review_count": 1284,
    "seller": "Loja Exemplo"
  }
}
```

## Execução 2 - S2-B - static - contexto_integral
```json
{
  "extraction_efficacy": 0.97,
  "confidence_index": 0.93,
  "qualitative_justification": "Facilidade: o bloco JSON-LD segue o padrão schema.org (Product, Brand, AggregateRating e Offer), com campos explícitos e tipados para nome, marca, preço numérico (3499.0), moeda ISO (BRL), disponibilidade (URL do schema.org/InStock), nota (4.6), número de avaliações (1284) e vendedor (Loja Exemplo). Não foi necessário inferir nada nem usar conhecimento externo. Gargalos: o visible_text contém apenas um aviso para habilitar o JavaScript, então não há como confirmar visualmente se os dados do JSON-LD coincidem com o conteúdo renderizado na página (preço, estoque e avaliações podem ser alterados dinamicamente). Os metadados são mínimos (só viewport), sem og:title, description ou outras tags de reforço. O campo priceValidUntil está ausente, assim não se sabe até quando o preço vale. A confiança é um pouco menor por depender de uma única fonte estruturada, sem validação cruzada.",
  "extracted_entities": {
    "product_name": "Smartphone Nexo X12 Pro 256 GB - Grafite",
    "brand": "Nexo",
    "price": 3499.0,
    "currency": "BRL",
    "availability": "InStock",
    "rating_value": 4.6,
    "review_count": 1284,
    "seller": "Loja Exemplo"
  }
}
```

## Execução 2 - S2-B - static - rag_chunking
```json
{
  "extraction_efficacy": 0.95,
  "confidence_index": 0.95,
  "qualitative_justification": "Os dados estavam em JSON-LD schema.org do tipo Product, com campos padronizados e sem ambiguidade (offers.price, priceCurrency, availability, aggregateRating, seller). O principal gargalo foi o JSON-LD ter sido dividido em dois fragmentos, cortado no meio de 'ratingValue'. A sobreposição de texto entre os fragmentos ('armazenamento e bateria de 5.000 mAh...') permitiu reconstruir o objeto sem perda de contexto. O aviso de JavaScript no texto visível indica que a página depende de renderização no cliente, mas isso não afetou a extração, pois os dados estruturados já estavam no código-fonte. Pontos de atenção: o nome do produto inclui a cor 'Grafite' (variante), e o vendedor coincide com o nome da loja. Não foi preciso conhecimento externo, mas não há data de validade do preço nem confirmação visual de que o JSON-LD corresponde ao conteúdo renderizado.",
  "extracted_entities": {
    "product_name": "Smartphone Nexo X12 Pro 256 GB - Grafite",
    "brand": "Nexo",
    "price": 3499.0,
    "currency": "BRL",
    "availability": "InStock",
    "rating_value": 4.6,
    "review_count": 1284,
    "seller": "Loja Exemplo"
  }
}
```

## Execução 2 - S2-B - rendered - contexto_integral
```json
{
  "extraction_efficacy": 0.98,
  "confidence_index": 0.97,
  "qualitative_justification": "A extração foi muito facilitada pelo bloco JSON-LD do tipo Product, que traz todas as entidades solicitadas em campos estruturados e semanticamente rotulados: name, brand.name, offers.price (numérico), offers.priceCurrency (BRL), offers.availability (URL schema.org/InStock), aggregateRating.ratingValue, aggregateRating.reviewCount e offers.seller.name. O texto visível confirma os mesmos valores (R$ 3.499,00, 4,6 de 5 estrelas, 1.284 avaliações, 'Em estoque', 'Vendido e entregue por Loja Exemplo', 'Marca: Nexo'), o que elimina ambiguidades e a necessidade de conhecimento externo. Pontos de atenção menores: (1) o aviso 'Habilite o JavaScript' sugere renderização parcial via JS, mas o conteúdo relevante está presente no JSON-LD e no texto visível, então não houve perda; (2) a seção 'Quem viu este produto também viu' contém outros produtos com preços, notas e vendedores distintos (Nexo X10, Orbi S8, TechMais), que poderiam gerar contaminação em um extrator ingênuo baseado apenas em texto, mas são facilmente descartáveis pela prioridade ao JSON-LD; (3) o preço de 12x R$ 291,58 é uma condição de parcelamento, não o preço principal, e foi corretamente ignorado; (4) os metadados HTML são pobres (apenas viewport), sem meta description ou Open Graph, e o title genérico 'Loja Exemplo' não identifica o produto, mas isso é irrelevante dada a riqueza do JSON-LD.",
  "extracted_entities": {
    "product_name": "Smartphone Nexo X12 Pro 256 GB - Grafite",
    "brand": "Nexo",
    "price": 3499.0,
    "currency": "BRL",
    "availability": "InStock",
    "rating_value": 4.6,
    "review_count": 1284,
    "seller": "Loja Exemplo"
  }
}
```

## Execução 2 - S2-B - rendered - rag_chunking
```json
{
  "extraction_efficacy": 0.97,
  "confidence_index": 0.96,
  "qualitative_justification": "A extração foi facilitada pela redundância entre duas fontes consistentes: o JSON-LD (schema.org Product/Offer/AggregateRating) e o texto visível da página. O JSON-LD traz valores tipados e sem ambiguidade (price 3499.0, priceCurrency BRL, availability schema.org/InStock, ratingValue 4.6, reviewCount 1284, seller Loja Exemplo, brand Nexo), e o texto renderizado os confirma (R$ 3.499,00, 4,6 de 5 estrelas, 1.284 avaliações, 'Em estoque - envio imediato', 'Vendido e entregue por Loja Exemplo'). Os gargalos são menores: os fragmentos estão truncados e fora de ordem, e o JSON-LD aparece dividido entre o fragmento 3 (name, brand, início de aggregateRating) e o fragmento 2 (restante de aggregateRating e offers), exigindo remontagem. Há também ruído de interface ('Habilite o JavaScript') e o parcelamento (12x de R$ 291,58), que poderia ser confundido com o preço, mas o preço à vista e o campo 'price' do JSON-LD resolvem a ambiguidade. O nome do produto é o do JSON-LD ('Smartphone Nexo X12 Pro 256 GB - Grafite'), que corresponde à consulta, embora a variante de cor Grafite não tenha sido especificada pelo usuário. Nenhum conhecimento externo foi necessário.",
  "extracted_entities": {
    "product_name": "Smartphone Nexo X12 Pro 256 GB - Grafite",
    "brand": "Nexo",
    "price": 3499.0,
    "currency": "BRL",
    "availability": "InStock",
    "rating_value": 4.6,
    "review_count": 1284,
    "seller": "Loja Exemplo"
  }
}
```

## Execução 2 - S3-A - static - contexto_integral
```json
{
  "extraction_efficacy": 0.85,
  "confidence_index": 0.88,
  "qualitative_justification": "Não há JSON-LD (json_ld nulo), então toda a extração dependeu do texto visível não estruturado, o que exigiu desambiguação manual. Facilidades: o bloco principal do produto é bem delimitado e traz marca explícita ('Marca: Nexo'), nome completo, nota (4,6) e número de avaliações (1.284), preço atual ('por R$ 3.499,00'), disponibilidade ('Em estoque') e vendedor principal ('Vendido e entregue por Loja Exemplo'). Gargalos: (1) há vários preços concorrentes no texto (R$ 899,00 do banner promocional, R$ 3.999,00 riscado, R$ 3.324,05 no PIX, parcelas de R$ 349,90 e ofertas de outros vendedores como R$ 3.459,00 e R$ 2.799,00), exigindo escolher o preço principal pelo contexto 'por R$ 3.499,00' e não o preço à vista no PIX; (2) o número 4,8 (25.390) refere-se à reputação da loja, e não ao produto, e precisou ser descartado para rating_value e review_count; (3) a moeda é inferida do símbolo 'R$', sem campo explícito; (4) há ruído de Q&A e avaliações que mencionam 512 GB esgotado e vendedor diferente, mas que não alteram a oferta principal de 256 GB. O título da página e a meta description citam 'até 12% de desconto', o que é uma informação de marketing consistente com o cálculo (3.999 → 3.499), mas não é usada como preço. Nenhum conhecimento externo foi necessário, embora a conversão de 'R$' para BRL seja uma convenção implícita.",
  "extracted_entities": {
    "product_name": "Nexo X12 Pro 256GB 12GB RAM Câmera 200MP Tela 6.7\" - Grafite",
    "brand": "Nexo",
    "price": 3499.0,
    "currency": "BRL",
    "availability": "InStock",
    "rating_value": 4.6,
    "review_count": 1284,
    "seller": "Loja Exemplo"
  }
}
```

## Execução 2 - S3-A - static - rag_chunking
```json
{
  "extraction_efficacy": 0.78,
  "confidence_index": 0.72,
  "qualitative_justification": "Facilidades: o fragmento 2 concentra quase todas as entidades em texto corrido com rótulos claros ('Marca: Nexo', 'Nota do produto: 4,6 (1.284 avaliações de compradores)', 'Em estoque'). O fragmento 1 confirma que a versão de 256 GB está disponível e que a de 512 GB está esgotada, o que reforça a disponibilidade. Gargalos: (1) não há marcação estruturada (JSON-LD/schema.org), então os dados dependem de interpretar texto livre. (2) Há vários valores monetários concorrentes: R$ 899,00 (banner promocional genérico, não é do produto), R$ 3.999,00 (preço antigo), R$ 3.499,00 (preço atual), R$ 3.324,05 (PIX) e 10x de R$ 349,90 (parcelado). Escolhi R$ 3.499,00 como preço principal e descartei os demais por inferência contextual. (3) O vendedor não é identificado. O título cita apenas 'Loja Exemplo Marketplace', que é a plataforma, e a descrição fala em 'vários vendedores', então seller ficou null para evitar alucinação. (4) O fragmento 1 está truncado em 'Rafael T. - 2', mas isso não afeta nota média nem contagem, que vêm do fragmento 2. (5) 'Em estoque' é inferido como InStock, mas pode se referir à oferta exibida e não a todos os vendedores. (6) A moeda foi deduzida do símbolo 'R$' e não de um campo explícito.",
  "extracted_entities": {
    "product_name": "Nexo X12 Pro 256GB 12GB RAM Câmera 200MP Tela 6.7\" Grafite",
    "brand": "Nexo",
    "price": 3499.0,
    "currency": "BRL",
    "availability": "InStock",
    "rating_value": 4.6,
    "review_count": 1284,
    "seller": null
  }
}
```

## Execução 2 - S3-B - static - contexto_integral
```json
{
  "extraction_efficacy": 0.95,
  "confidence_index": 0.93,
  "qualitative_justification": "Facilidades: o bloco JSON-LD (schema.org/Product) está completo e bem estruturado, com name, brand, aggregateRating, e offers (price, priceCurrency, availability, seller), o que permite extrair todas as entidades solicitadas sem ambiguidade. O texto visível confirma os mesmos valores (nota 4,6; 1.284 avaliações; R$ 3.499,00; 'Em estoque'; 'Vendido e entregue por Loja Exemplo'), garantindo consistência entre as duas fontes. Gargalos: a página contém ruído potencial de contexto, como o preço original riscado (R$ 3.999,00), o preço no PIX (R$ 3.324,05), ofertas de outros vendedores (TechMais, MegaCell recondicionado), a reputação da loja (4,8 com 25.390 avaliações, que não se refere ao produto), a menção a 'a partir de R$ 899,00' (campanha geral) e o modelo de 512 GB esgotado (variante distinta). O título e o nome do produto variam levemente entre o title, o JSON-LD e o texto visível, e o JSON-LD traz a oferta principal como única, embora haja várias ofertas visíveis. Como o JSON-LD e o texto visível concordam sobre a oferta principal, o risco de erro é baixo; a desambiguação exigiu apenas distinguir o preço de oferta principal dos demais valores.",
  "extracted_entities": {
    "product_name": "Smartphone Nexo X12 Pro 256 GB - Grafite",
    "brand": "Nexo",
    "price": 3499.0,
    "currency": "BRL",
    "availability": "InStock",
    "rating_value": 4.6,
    "review_count": 1284,
    "seller": "Loja Exemplo"
  }
}
```

## Execução 2 - S3-B - static - rag_chunking
```json
{
  "extraction_efficacy": 0.72,
  "confidence_index": 0.7,
  "qualitative_justification": "Facilidades: o fragmento 2 traz quase todos os dados em texto corrido e com rótulos claros: marca (Nexo), nota (4,6), número de avaliações (1.284), preço atual (R$ 3.499,00, com o preço 'De' de R$ 3.999,00 riscado), preço no PIX (R$ 3.324,05), parcelamento em 10x de R$ 349,90 e 'Em estoque'. O fragmento 1 confirma que a versão de 256 GB está disponível, e o 3 confirma nome e marca pelo JSON-LD. Gargalos: (1) o vendedor não foi identificado, porque o texto é cortado em 'Vendido e entregue' e o nome do seller não aparece. A página é um marketplace com vários vendedores, então não dá para inferir quem vende (a 'Loja Exemplo Marketplace' do título é a plataforma, não necessariamente o vendedor). (2) O JSON-LD está truncado no campo 'brand', sem os blocos 'offers' e 'aggregateRating', que seriam a fonte estruturada e mais confiável de preço, disponibilidade e avaliações. Por isso esses dados vêm só do texto visível. (3) Há ruído e ambiguidade: 'celulares a partir de R$ 899,00' é banner de outros produtos, a meta description menciona 'até 12% de desconto' (o desconto real é cerca de 12,5%) e há três valores monetários concorrentes (3.499,00, 3.324,05 e 349,90). Escolhi R$ 3.499,00 como preço padrão, pois o PIX é condicional e o parcelado soma o mesmo valor. (4) O fragmento 1 cita uma versão de 512 GB esgotada, mas a de 256 GB está disponível, o que evita confusão na disponibilidade. A nota e o número de avaliações parecem se referir ao produto exibido, mas não há confirmação estruturada.",
  "extracted_entities": {
    "product_name": "Smartphone Nexo X12 Pro 256 GB - Grafite",
    "brand": "Nexo",
    "price": 3499.0,
    "currency": "BRL",
    "availability": "InStock",
    "rating_value": 4.6,
    "review_count": 1284,
    "seller": null
  }
}
```

## Execução 2 - S3-C - static - contexto_integral
```json
{
  "extraction_efficacy": 0.72,
  "confidence_index": 0.55,
  "qualitative_justification": "O JSON-LD é limpo e bem estruturado, o que facilita identificar nome, marca, moeda e vendedor. Porém, ele conflita com o texto visível em quatro campos. Preço: o JSON-LD diz 3999,00, mas o texto mostra 'De R$ 3.999,00 por R$ 3.499,00', ou seja, o JSON-LD parece trazer o preço antigo. Disponibilidade: o JSON-LD diz OutOfStock, mas o texto diz 'Em estoque' e o Q&A confirma que a versão de 256 GB está disponível. Nota: o JSON-LD traz 4,4, mas o texto traz 4,6. Avaliações: o JSON-LD traz 1102, mas o texto traz 1.284. Concluí que o JSON-LD está desatualizado e priorizei o texto visível, que é mais consistente internamente (oferta, parcelamento, PIX, Q&A). Essa escolha é uma inferência, o que reduz a confiança. Outros pontos de ruído: o preço PIX (3.324,05) e as ofertas de outros vendedores (TechMais, MegaCell recondicionado) podem ser confundidos com a oferta principal. A nota da loja (4,8; 25.390) não deve ser confundida com a nota do produto. A oferta principal é claramente vendida e entregue por Loja Exemplo. Não há datas relevantes.",
  "extracted_entities": {
    "product_name": "Smartphone Nexo X12 Pro 256 GB - Grafite",
    "brand": "Nexo",
    "price": 3499.0,
    "currency": "BRL",
    "availability": "InStock",
    "rating_value": 4.6,
    "review_count": 1284,
    "seller": "Loja Exemplo"
  }
}
```

## Execução 2 - S3-C - static - rag_chunking
```json
{
  "extraction_efficacy": 0.62,
  "confidence_index": 0.6,
  "qualitative_justification": "Facilidades: o segundo fragmento reúne quase todos os dados comerciais em texto corrido e legível, com nome do produto (Nexo X12 Pro 256GB), marca (Nexo), nota 4,6, 1.284 avaliações, preço de R$ 3.499,00 (de R$ 3.999,00), preço no PIX de R$ 3.324,05, parcelamento em 10x de R$ 349,90 e 'Em estoque'. O terceiro fragmento traz um JSON-LD de Product que confirma o nome e o SKU, e o primeiro fragmento corrobora que a versão de 256 GB está disponível. Gargalos: (1) o vendedor está truncado ('Vendido e entregue'), sem o nome de quem vende, e a página é um marketplace com vários vendedores, então não dá para inferir o seller; (2) o JSON-LD está cortado logo em 'brand', sem offers, aggregateRating nem price estruturados, o que obriga a depender do texto solto; (3) o preço exibe vários valores concorrentes (preço cheio, preço promocional, PIX, parcela), e a escolha do R$ 3.499,00 como preço principal é uma interpretação razoável (preço padrão e parcelado), mas ambígua; (4) o texto traz o cabeçalho 'celulares a partir de R$ 899,00', que é ruído de outra listagem; (5) a descrição fala em 'até 12% de desconto' enquanto o desconto real visível é de cerca de 12,5% (3.999→3.499), o que não afeta a extração; (6) a moeda não está em campo estruturado, mas o símbolo R$ permite inferir BRL com segurança. A disponibilidade tem sinal duplo e consistente (Em estoque e a resposta do FAQ). Há risco de incerteza porque os fragmentos podem vir de seções diferentes da página, mas a consistência entre eles é boa.",
  "extracted_entities": {
    "product_name": "Smartphone Nexo X12 Pro 256 GB - Grafite",
    "brand": "Nexo",
    "price": 3499.0,
    "currency": "BRL",
    "availability": "InStock",
    "rating_value": 4.6,
    "review_count": 1284,
    "seller": null
  }
}
```

## Execução 3 - S1-A - static - contexto_integral
```json
{
  "extraction_efficacy": 0.9,
  "confidence_index": 0.92,
  "qualitative_justification": "Não há JSON-LD (json_ld é null), então a extração dependeu inteiramente do texto visível, que é limpo, linear e bem rotulado. Facilidades: o nome do produto aparece no título e no cabeçalho do texto; a marca vem explicitamente rotulada ('Marca: Nexo') e é confirmada pelo breadcrumb; o preço ('R$ 3.499,00 à vista') traz símbolo de moeda e valor completo; a disponibilidade ('Em estoque - envio imediato') é inequívoca; a nota (4,6 de 5) e a contagem de avaliações (1.284) estão juntas na mesma linha; o vendedor está explícito ('Vendido e entregue por Loja Exemplo'). Gargalos: a ausência de dados estruturados exige inferência a partir de texto livre e formatos numéricos em padrão brasileiro (vírgula decimal, ponto de milhar), que precisam de normalização. Há risco de ambiguidade com os produtos relacionados ('Quem viu este produto também viu'), que contêm outros preços, notas e vendedores (ex.: TechMais, Orbi S8), mas estão em seção claramente separada e foram descartados. O preço parcelado (12x R$ 291,58) é diferente do preço à vista e foi ignorado, adotando-se o valor à vista. A moeda foi inferida do símbolo R$ (BRL). O nome do produto no cabeçalho inclui a cor (Grafite), o que o diferencia ligeiramente do título da página. Nenhum conhecimento externo foi necessário.",
  "extracted_entities": {
    "product_name": "Smartphone Nexo X12 Pro 256 GB - Grafite",
    "brand": "Nexo",
    "price": 3499.0,
    "currency": "BRL",
    "availability": "InStock",
    "rating_value": 4.6,
    "review_count": 1284,
    "seller": "Loja Exemplo"
  }
}
```

## Execução 3 - S1-A - static - rag_chunking
```json
{
  "extraction_efficacy": 0.92,
  "confidence_index": 0.9,
  "qualitative_justification": "Facilidades: o primeiro fragmento concentra em texto corrido quase todas as entidades pedidas (nome do produto com capacidade e cor, marca, nota 4,6 de 5, 1.284 avaliações, preço à vista de R$ 3.499,00, estoque e vendedor), com rótulos claros como 'Marca:', 'Em estoque' e 'Vendido e entregue por'. O título e o breadcrumb do segundo fragmento confirmam nome do produto, marca e loja. Gargalos: não há dados estruturados (JSON-LD/schema.org, itemprop ou meta tags de preço), então a extração depende de interpretar texto livre, e a disponibilidade 'Em estoque - envio imediato' precisou ser mapeada para InStock. O preço aparece junto com o parcelamento (12x de R$ 291,58), o que exige distinguir o preço à vista do valor da parcela. A moeda foi inferida do símbolo 'R$'. O fragmento começa truncado ('200 MP TEXTO:') e a descrição termina cortada, mas isso não afeta as entidades pedidas. O vendedor 'Loja Exemplo' é consistente entre os fragmentos 1, 2 e 3. Não há data de atualização do preço, então não é possível verificar se a informação está atual.",
  "extracted_entities": {
    "product_name": "Smartphone Nexo X12 Pro 256 GB - Grafite",
    "brand": "Nexo",
    "price": 3499.0,
    "currency": "BRL",
    "availability": "InStock",
    "rating_value": 4.6,
    "review_count": 1284,
    "seller": "Loja Exemplo"
  }
}
```

## Execução 3 - S1-B - static - contexto_integral
```json
{
  "extraction_efficacy": 0.98,
  "confidence_index": 0.97,
  "qualitative_justification": "A extração foi muito fácil porque o JSON-LD (schema.org/Product) está completo e traz todas as entidades solicitadas em campos tipados: name, brand.name, offers.price (numérico), priceCurrency (BRL), availability (URL schema.org/InStock), aggregateRating (ratingValue e reviewCount) e offers.seller.name. O texto visível confirma todos os valores: R$ 3.499,00, 'Em estoque - envio imediato', nota 4,6 de 5, 1.284 avaliações e 'Vendido e entregue por Loja Exemplo'. Não há conflito entre JSON-LD e texto visível. Os únicos pontos de atenção são pequenos: o título da página e o JSON-LD diferem levemente (o JSON-LD inclui a cor 'Grafite', usada como nome do produto por ser mais específico), e a seção 'Quem viu este produto também viu' contém outros produtos com preços, notas e vendedores distintos (Nexo X10, Orbi S8), que poderiam gerar ambiguidade em um extrator baseado apenas em texto, mas são facilmente descartados pelo contexto e pela prioridade dada ao JSON-LD. O parcelamento (12x de R$ 291,58) é uma oferta secundária e não interfere no preço principal. Nenhum conhecimento externo foi necessário.",
  "extracted_entities": {
    "product_name": "Smartphone Nexo X12 Pro 256 GB - Grafite",
    "brand": "Nexo",
    "price": 3499.0,
    "currency": "BRL",
    "availability": "InStock",
    "rating_value": 4.6,
    "review_count": 1284,
    "seller": "Loja Exemplo"
  }
}
```

## Execução 3 - S1-B - static - rag_chunking
```json
{
  "extraction_efficacy": 0.95,
  "confidence_index": 0.95,
  "qualitative_justification": "A extração foi facilitada pela redundância entre o JSON-LD (schema.org Product, AggregateRating e Offer) e o texto visível. Os dois concordam em preço (R$ 3.499,00 = 3499.0 BRL), nota (4,6 = 4.6), número de avaliações (1.284 = 1284), vendedor (Loja Exemplo) e disponibilidade (InStock = 'Em estoque - envio imediato'). O JSON-LD traz a moeda explícita (BRL) e a disponibilidade em formato padronizado. O nome completo do produto e a marca aparecem no título da página e no breadcrumb ('Marca: Nexo'). Os gargalos são pequenos: os fragmentos estão truncados, e o JSON-LD está dividido entre dois trechos, com o campo 'name' cortado em 'Smartphone Nexo'. O nome completo foi reconstruído a partir do título e do texto ('Smartphone Nexo X12 Pro 256 GB'), em que a cor 'Grafite' aparece apenas como variação. O preço parcelado (12x de R$ 291,58) não conflita com o preço à vista. Nenhum conhecimento externo foi necessário. A confiança não chega a 1.0 por causa da truncagem e da junção de fragmentos.",
  "extracted_entities": {
    "product_name": "Smartphone Nexo X12 Pro 256 GB",
    "brand": "Nexo",
    "price": 3499.0,
    "currency": "BRL",
    "availability": "InStock",
    "rating_value": 4.6,
    "review_count": 1284,
    "seller": "Loja Exemplo"
  }
}
```

## Execução 3 - S2-A - static - contexto_integral
```json
{
  "extraction_efficacy": 0.0,
  "confidence_index": 0.0,
  "qualitative_justification": "A página retornou apenas um aviso de que o JavaScript precisa estar habilitado. O conteúdo real do produto é renderizado no lado do cliente e não está presente no HTML estático capturado. O JSON-LD é nulo, os metadados se limitam ao viewport (sem Open Graph, description ou outras tags úteis) e o texto visível não contém nenhuma informação de produto. O único dado disponível é o título genérico 'Loja Exemplo', que provavelmente é o nome da loja e não de um produto, e não é suficiente para inferir marca, vendedor ou qualquer outra entidade com segurança. Para extrair os dados, seria necessário renderizar a página com um navegador headless (por exemplo Playwright ou Puppeteer) ou acessar APIs internas que alimentam o front-end.",
  "extracted_entities": {
    "product_name": null,
    "brand": null,
    "price": null,
    "currency": null,
    "availability": null,
    "rating_value": null,
    "review_count": null,
    "seller": null
  }
}
```

## Execução 3 - S2-A - static - rag_chunking
```json
{
  "extraction_efficacy": 0.0,
  "confidence_index": 0.0,
  "qualitative_justification": "O único fragmento recuperado contém apenas o título genérico da página ('Loja Exemplo'), a meta tag viewport e o aviso 'Habilite o JavaScript para utilizar a Loja Exemplo'. Isso indica que a página é renderizada no cliente (SPA/CSR) e o scraping capturou apenas o shell HTML inicial, sem o conteúdo dinâmico. Não há nenhum dado de produto, JSON-LD, microdados schema.org, Open Graph ou texto visível que mencione o Nexo X12 Pro 256 GB, preço, moeda, disponibilidade, nota média, número de avaliações ou vendedor. O gargalo principal é a dependência de JavaScript: sem renderização (headless browser) ou acesso a uma API/endpoint de dados estruturados, nenhuma entidade solicitada pode ser identificada. Responder com valores seria alucinação ou dependeria de conhecimento externo, por isso todas as entidades são null.",
  "extracted_entities": {
    "product_name": null,
    "brand": null,
    "price": null,
    "currency": null,
    "availability": null,
    "rating_value": null,
    "review_count": null,
    "seller": null
  }
}
```

## Execução 3 - S2-A - rendered - contexto_integral
```json
{
  "extraction_efficacy": 0.98,
  "confidence_index": 0.97,
  "qualitative_justification": "Facilidade: o JSON-LD é do tipo schema.org/Product, completo e bem estruturado, e traz nome, marca, preço numérico (3499), moeda (BRL), disponibilidade (InStock), nota (4.6), contagem de avaliações (1284) e vendedor (Loja Exemplo) em campos explícitos, sem ambiguidade. O texto visível confirma todos os valores (R$ 3.499,00 à vista, 4,6 de 5 estrelas, 1.284 avaliações, Em estoque, Vendido e entregue por Loja Exemplo), o que dá consistência entre as duas fontes. Gargalos menores: (1) o texto visível traz a mensagem 'Habilite o JavaScript', o que indica que parte da página pode depender de renderização no cliente, mas isso não afetou os dados principais, presentes no JSON-LD; (2) a seção 'Quem viu este produto também viu' contém produtos concorrentes com preços, notas e vendedores diferentes (Nexo X10 e Orbi S8), que são ruído e poderiam gerar confusão em extração baseada apenas em texto, mas foram descartados por não pertencerem ao produto principal; (3) o preço à vista (3.499,00) coexiste com o parcelado (12x de R$ 291,58), e foi usado o preço à vista, que coincide com o JSON-LD; (4) os metadados são mínimos (só viewport), sem og:tags ou description, mas isso é irrelevante dado o JSON-LD. Não foi necessário conhecimento externo.",
  "extracted_entities": {
    "product_name": "Smartphone Nexo X12 Pro 256 GB - Grafite",
    "brand": "Nexo",
    "price": 3499,
    "currency": "BRL",
    "availability": "InStock",
    "rating_value": 4.6,
    "review_count": 1284,
    "seller": "Loja Exemplo"
  }
}
```

## Execução 3 - S2-A - rendered - rag_chunking
```json
{
  "extraction_efficacy": 0.97,
  "confidence_index": 0.96,
  "qualitative_justification": "Facilidades: os fragmentos trazem dados estruturados JSON-LD (schema.org Product, AggregateRating e Offer) que concordam com o texto visível da página, o que permite validação cruzada. Nome do produto, marca (Nexo), preço (3499 BRL), disponibilidade (InStock), nota (4,6), quantidade de avaliações (1284) e vendedor (Loja Exemplo) aparecem de forma explícita e consistente nas duas fontes. Gargalos: os fragmentos estão truncados e fora de ordem. O JSON-LD está dividido entre o primeiro e o segundo trecho, sem o início do bloco Offer no mesmo fragmento do cabeçalho, e o texto visível é cortado no meio da descrição e do preço. O aviso 'Habilite o JavaScript' sugere conteúdo possivelmente renderizado via JS, mas os dados necessários estavam presentes. O preço de R$ 3.499,00 é à vista, e o parcelamento (12x de R$ 291,58) não altera o valor principal. O título do HTML é genérico ('Loja Exemplo'), mas o nome completo do produto aparece no JSON-LD e no texto. Não foi necessário conhecimento externo.",
  "extracted_entities": {
    "product_name": "Smartphone Nexo X12 Pro 256 GB - Grafite",
    "brand": "Nexo",
    "price": 3499,
    "currency": "BRL",
    "availability": "InStock",
    "rating_value": 4.6,
    "review_count": 1284,
    "seller": "Loja Exemplo"
  }
}
```

## Execução 3 - S2-B - static - contexto_integral
```json
{
  "extraction_efficacy": 0.98,
  "confidence_index": 0.95,
  "qualitative_justification": "A extração foi simples porque o JSON-LD segue o padrão schema.org (Product, Brand, AggregateRating e Offer) e traz todas as entidades solicitadas em campos explícitos e tipados. O preço (3499.0) e a nota (4.6) já são numéricos, a moeda está em código ISO (BRL), a disponibilidade vem como URL do schema.org (InStock) e o vendedor é um objeto Organization. Não foi preciso inferir nada nem usar conhecimento externo. O único gargalo é o visible_text, que contém apenas um aviso de JavaScript desabilitado. Isso mostra que o HTML renderizado não tem conteúdo visível, e a página depende de renderização client-side. Por isso, não foi possível validar os dados do JSON-LD contra o conteúdo exibido ao usuário, o que reduz levemente a confiança. O title genérico ('Loja Exemplo') e a ausência de metadados como description e Open Graph não afetaram a extração.",
  "extracted_entities": {
    "product_name": "Smartphone Nexo X12 Pro 256 GB - Grafite",
    "brand": "Nexo",
    "price": 3499.0,
    "currency": "BRL",
    "availability": "InStock",
    "rating_value": 4.6,
    "review_count": 1284,
    "seller": "Loja Exemplo"
  }
}
```

## Execução 3 - S2-B - static - rag_chunking
```json
{
  "extraction_efficacy": 0.95,
  "confidence_index": 0.95,
  "qualitative_justification": "Os dados estão em JSON-LD schema.org do tipo Product, o que facilita a extração direta e sem ambiguidade de nome, marca, preço, moeda, disponibilidade, nota, número de avaliações e vendedor. O único gargalo é que o JSON-LD foi cortado entre os dois fragmentos, na chave ratingValue. O trecho sobreposto no início do segundo fragmento permitiu reconstruir o objeto sem perda de contexto. O texto visível da página (\"Habilite o JavaScript...\") indica renderização dependente de JavaScript, mas isso não afetou a extração, porque os dados estruturados estavam no código-fonte. O produto, a variante de 256 GB e a loja correspondem à consulta. Não foi necessário conhecimento externo. A confiança não é máxima porque o texto visível da página não confirma os valores, que vêm apenas do JSON-LD, e porque o seller aparece como Organization sem outros detalhes.",
  "extracted_entities": {
    "product_name": "Smartphone Nexo X12 Pro 256 GB - Grafite",
    "brand": "Nexo",
    "price": 3499.0,
    "currency": "BRL",
    "availability": "InStock",
    "rating_value": 4.6,
    "review_count": 1284,
    "seller": "Loja Exemplo"
  }
}
```

## Execução 3 - S2-B - rendered - contexto_integral
```json
{
  "extraction_efficacy": 0.98,
  "confidence_index": 0.97,
  "qualitative_justification": "A extração foi muito fácil porque o JSON-LD segue o schema.org (Product, Brand, AggregateRating, Offer e Organization) e traz todas as entidades solicitadas em campos tipados e sem ambiguidade: nome, marca, preço numérico (3499.0), moeda (BRL), disponibilidade (InStock), nota (4.6), número de avaliações (1284) e vendedor. O texto visível confirma todos esses valores (R$ 3.499,00, 'Em estoque', 4,6 de 5 estrelas, 1.284 avaliações, 'Vendido e entregue por Loja Exemplo'), sem divergência entre as duas fontes. Os pequenos gargalos são: o aviso 'Habilite o JavaScript', que indica possível renderização dinâmica mas não afetou os dados; a seção 'Quem viu este produto também viu', que traz outros produtos com preços, notas e vendedores (por exemplo, TechMais) e poderia contaminar a extração se não fosse isolada do produto principal; e o parcelamento (12x de R$ 291,58), que pode ser confundido com o preço principal. Como o JSON-LD é inequívoco, nenhum conhecimento externo foi necessário.",
  "extracted_entities": {
    "product_name": "Smartphone Nexo X12 Pro 256 GB - Grafite",
    "brand": "Nexo",
    "price": 3499.0,
    "currency": "BRL",
    "availability": "InStock",
    "rating_value": 4.6,
    "review_count": 1284,
    "seller": "Loja Exemplo"
  }
}
```

## Execução 3 - S2-B - rendered - rag_chunking
```json
{
  "extraction_efficacy": 0.97,
  "confidence_index": 0.96,
  "qualitative_justification": "A extração foi muito fácil porque os dados aparecem em duas fontes redundantes e consistentes entre si: o JSON-LD (schema.org Product, com AggregateRating e Offer) e o texto visível da página. Os valores coincidem: preço R$ 3.499,00 (3499.0 BRL), nota 4,6 (4.6), 1.284 avaliações (1284), vendedor 'Loja Exemplo' e disponibilidade 'https://schema.org/InStock', confirmada pelo texto 'Em estoque - envio imediato'. O nome do produto e a marca também estão explícitos ('Smartphone Nexo X12 Pro 256 GB - Grafite', marca Nexo). Gargalos menores: os fragmentos estão truncados e fora de ordem, e o JSON-LD está dividido entre os fragmentos 2 e 3, exigindo reconstrução mental (o trecho 'ratingValue' é cortado no fragmento 3 e continua no 2). Há ruído como o aviso 'Habilite o JavaScript', e a variante de cor (Grafite) está no nome do produto. O preço de 12x de R$ 291,58 é parcelamento e não foi confundido com o preço à vista. Nenhum conhecimento externo foi necessário.",
  "extracted_entities": {
    "product_name": "Smartphone Nexo X12 Pro 256 GB - Grafite",
    "brand": "Nexo",
    "price": 3499.0,
    "currency": "BRL",
    "availability": "InStock",
    "rating_value": 4.6,
    "review_count": 1284,
    "seller": "Loja Exemplo"
  }
}
```

## Execução 3 - S3-A - static - contexto_integral
```json
{
  "extraction_efficacy": 0.8,
  "confidence_index": 0.85,
  "qualitative_justification": "Não há JSON-LD (json_ld é null), então toda a extração dependeu do texto visível, que é pouco estruturado, sem marcação semântica de campos. Mesmo assim, os dados principais estão explícitos e próximos uns dos outros: nome do produto, marca ('Marca: Nexo'), preço atual ('por R$ 3.499,00'), disponibilidade ('Em estoque') e nota do produto (4,6 com 1.284 avaliações). Os principais gargalos foram: (1) ambiguidade de preços, já que há preço antigo (R$ 3.999,00), preço atual (R$ 3.499,00), preço no PIX (R$ 3.324,05), parcelamento e o 'a partir de R$ 899,00' de outros celulares, o que exigiu escolher o preço padrão de venda e descartar os demais; (2) múltiplos vendedores com preços e notas distintos (TechMais, MegaCell recondicionado), além de duas notas diferentes (produto 4,6 e loja 4,8 com 25.390 avaliações), o que exige cuidado para não misturar as métricas do produto com as do vendedor; (3) a ofensa ao contexto de vendedor: o vendedor da oferta principal é identificado explicitamente como 'Loja Exemplo'; (4) o conteúdo de perguntas e respostas e avaliações menciona o modelo de 512 GB esgotado e uma queixa sobre outro vendedor, que são ruídos que não alteram a disponibilidade do item de 256 GB. A moeda (BRL) é inferida pelo símbolo 'R$', o que é seguro. Nenhum conhecimento externo foi necessário, mas a ausência de dados estruturados reduz levemente a certeza.",
  "extracted_entities": {
    "product_name": "Nexo X12 Pro 256GB 12GB RAM Câmera 200MP Tela 6.7\" - Grafite",
    "brand": "Nexo",
    "price": 3499.0,
    "currency": "BRL",
    "availability": "InStock",
    "rating_value": 4.6,
    "review_count": 1284,
    "seller": "Loja Exemplo"
  }
}
```

## Execução 3 - S3-A - static - rag_chunking
```json
{
  "extraction_efficacy": 0.7,
  "confidence_index": 0.6,
  "qualitative_justification": "Facilidades: o fragmento 2 concentra quase todos os dados do produto de forma explícita e legível: nome (Nexo X12 Pro 256GB), marca (Nexo), nota (4,6), número de avaliações (1.284), preço (de R$ 3.999,00 por R$ 3.499,00, R$ 3.324,05 no PIX com 5% de desconto, ou 10x de R$ 349,90 sem juros) e disponibilidade ('Em estoque'). O fragmento 1 confirma que a versão de 256 GB está disponível (a de 512 GB está esgotada), o que reforça a leitura de InStock. Gargalos: (1) Não há dados estruturados (JSON-LD/schema.org), então tudo depende de texto corrido sem marcação semântica. (2) O vendedor não é identificado. O título menciona 'Loja Exemplo Marketplace', mas a meta description diz que há 'ofertas de vários vendedores no marketplace'. Isso indica que Loja Exemplo é a plataforma, não necessariamente quem vende este item, por isso seller = null. (3) Há ambiguidade de preço: o preço de R$ 3.499,00 foi adotado como preço principal (parcelado/cartão) e o preço no PIX (R$ 3.324,05) é uma condição alternativa. O banner 'celulares a partir de R$ 899,00' é promocional de outros produtos e foi ignorado. A meta description cita 'até 12% de desconto', mas o desconto calculado de 3.999 para 3.499 é de cerca de 12,5%, o que é consistente, mas não essencial. (4) O fragmento 1 está truncado ('Rafael T. - 2'), e as avaliações individuais não afetam a nota média oficial. (5) Os fragmentos não trazem moeda em campo explícito, mas 'R$' permite inferir BRL sem ambiguidade. (6) O fragmento 2 não cita data nem vendedor, e o 'Modelo: X12 Pro (2026)' é só informativo.",
  "extracted_entities": {
    "product_name": "Nexo X12 Pro 256GB 12GB RAM Grafite",
    "brand": "Nexo",
    "price": 3499.0,
    "currency": "BRL",
    "availability": "InStock",
    "rating_value": 4.6,
    "review_count": 1284,
    "seller": null
  }
}
```

## Execução 3 - S3-B - static - contexto_integral
```json
{
  "extraction_efficacy": 0.95,
  "confidence_index": 0.93,
  "qualitative_justification": "Facilidades: o bloco JSON-LD (schema.org/Product) está completo e bem estruturado, com name, brand, aggregateRating, price, priceCurrency, availability e seller, e foi totalmente corroborado pelo texto visível (preço R$ 3.499,00, nota 4,6, 1.284 avaliações, 'Em estoque', vendido por Loja Exemplo). Isso permitiu extrair as entidades sem inferência externa. Gargalos: a página mistura múltiplos preços (preço 'de' R$ 3.999,00, preço no PIX R$ 3.324,05, parcelas de R$ 349,90, ofertas de outros vendedores como TechMais e MegaCell, e o 'a partir de R$ 899,00' da campanha), além de duas notas distintas (produto 4,6 e loja 4,8 com 25.390 avaliações) e menções a outra variante (512 GB esgotada) no Q&A. Esses elementos poderiam gerar ambiguidade para um extrator ingênuo, mas o JSON-LD aponta de forma inequívoca a oferta principal (Loja Exemplo, R$ 3.499,00, BRL, InStock). Pequena diferença no nome do produto entre JSON-LD ('Smartphone Nexo X12 Pro 256 GB - Grafite') e o título visível ('Nexo X12 Pro 256GB 12GB RAM Câmera 200MP Tela 6.7\" - Grafite'); optou-se pelo nome do JSON-LD por ser o campo estruturado canônico. O preço refere-se à oferta principal e não considera o desconto PIX condicional.",
  "extracted_entities": {
    "product_name": "Smartphone Nexo X12 Pro 256 GB - Grafite",
    "brand": "Nexo",
    "price": 3499.0,
    "currency": "BRL",
    "availability": "InStock",
    "rating_value": 4.6,
    "review_count": 1284,
    "seller": "Loja Exemplo"
  }
}
```

## Execução 3 - S3-B - static - rag_chunking
```json
{
  "extraction_efficacy": 0.72,
  "confidence_index": 0.68,
  "qualitative_justification": "Facilidades: o fragmento 2 traz em texto corrido quase todas as entidades pedidas, com marcadores claros (\"Marca: Nexo\", \"Nota do produto: 4,6 (1.284 avaliações de compradores)\", \"De R$ 3.999,00 por R$ 3.499,00\", \"Em estoque\"). O FAQ do fragmento 1 confirma que a versão de 256 GB está disponível, o que reforça a disponibilidade. O nome do produto aparece no título do fragmento 2 e no JSON-LD (\"Smartphone Nexo X12 Pro 256 GB - Grafite\"). Gargalos: (1) o vendedor está truncado em \"Vendido e entregue\", sem o nome, então seller = null. \"Loja Exemplo Marketplace\" é o nome do site, e os metadados indicam vários vendedores, então não o usei como vendedor. (2) O JSON-LD está cortado em \"brand\": {\"@type\":, sem os campos de offers e aggregateRating, que seriam a fonte estruturada mais confiável. A marca vem só do texto \"Marca: Nexo\". (3) Há vários preços (R$ 899,00 de outro anúncio, R$ 3.999,00 riscado, R$ 3.324,05 no PIX, parcelas de R$ 349,90). Escolhi R$ 3.499,00 como preço de venda padrão, mas isso exige interpretação. (4) O fragmento 1 mostra avaliações individuais de 5 e 2 estrelas, que não são a média e foram ignoradas. (5) Não dá para confirmar se preço, nota e estoque pertencem ao mesmo vendedor do marketplace.",
  "extracted_entities": {
    "product_name": "Smartphone Nexo X12 Pro 256 GB - Grafite",
    "brand": "Nexo",
    "price": 3499.0,
    "currency": "BRL",
    "availability": "InStock",
    "rating_value": 4.6,
    "review_count": 1284,
    "seller": null
  }
}
```

## Execução 3 - S3-C - static - contexto_integral
```json
{
  "extraction_efficacy": 0.62,
  "confidence_index": 0.55,
  "qualitative_justification": "Os dados estruturados (JSON-LD) e o texto visível se contradizem em quatro campos. Preço: o JSON-LD traz 3999,00, que no texto aparece como preço 'De' (antigo), enquanto o preço atual é R$ 3.499,00. Disponibilidade: o JSON-LD diz OutOfStock, mas o texto diz 'Em estoque' e o Q&A confirma que a versão de 256 GB está disponível. Nota: 4,4 no JSON-LD contra 4,6 no texto. Avaliações: 1102 no JSON-LD contra 1284 no texto. Escolhi o texto visível porque é consistente internamente (a descrição fala em 'até 12% de desconto', coerente com 3.999 para 3.499, cerca de 12,5%) e indica que o JSON-LD está desatualizado. Essa escolha é uma inferência, o que reduz a confiança. Outros pontos de ambiguidade: a página lista vários vendedores (TechMais, MegaCell recondicionado) e várias notas (produto 4,6; loja 4,8 com 25.390 avaliações; vendedor TechMais 4,1), e há preços alternativos (PIX R$ 3.324,05; parcelado em 10x de R$ 349,90; ofertas de outros vendedores; 'a partir de R$ 899,00' na faixa promocional). O vendedor principal é claro ('Vendido e entregue por Loja Exemplo', também no JSON-LD). Marca e moeda são consistentes nas duas fontes. O nome do produto varia entre as fontes; usei o do JSON-LD por ser mais limpo.",
  "extracted_entities": {
    "product_name": "Smartphone Nexo X12 Pro 256 GB - Grafite",
    "brand": "Nexo",
    "price": 3499.0,
    "currency": "BRL",
    "availability": "InStock",
    "rating_value": 4.6,
    "review_count": 1284,
    "seller": "Loja Exemplo"
  }
}
```

## Execução 3 - S3-C - static - rag_chunking
```json
{
  "extraction_efficacy": 0.7,
  "confidence_index": 0.6,
  "qualitative_justification": "Facilidades: o fragmento 2 concentra a maior parte dos dados em texto limpo: nome do produto (Nexo X12 Pro 256GB), marca (Nexo), nota (4,6), número de avaliações (1.284), preço atual (R$ 3.499,00, com preço de lista de R$ 3.999,00 e alternativa de R$ 3.324,05 no PIX) e o status 'Em estoque'. O fragmento 3 confirma o nome do produto e a marca via JSON-LD. O fragmento 1 reforça que a versão de 256 GB está disponível. Gargalos: (1) o vendedor está truncado em 'Vendido e entregue...', sem o nome, então seller é null, e a página é um marketplace com vários vendedores, o que impede inferir quem vende; (2) o JSON-LD está cortado logo após 'brand', sem os dados de offers, price, priceCurrency, availability, aggregateRating ou seller, então não há dados estruturados para validar o texto visível; (3) há múltiplos preços (de/por, PIX e parcelado), e escolhi o preço à vista no cartão/boleto de R$ 3.499,00 como preço principal, o que envolve certa interpretação; (4) a moeda não aparece em campo estruturado e foi deduzida do símbolo 'R$'; (5) a disponibilidade 'Em estoque' foi mapeada para InStock, e o fragmento 1 fala em 256 GB disponível, mas não deixa claro se essa informação se refere ao mesmo anúncio/vendedor; (6) a 'Nota do produto' e o número de avaliações aparecem como texto de interface e não como schema, e o fragmento 1 mostra opiniões truncadas e sem agregação. Em resumo, 5 dos 8 campos principais foram bem identificados e o vendedor não pôde ser extraído.",
  "extracted_entities": {
    "product_name": "Smartphone Nexo X12 Pro 256 GB - Grafite",
    "brand": "Nexo",
    "price": 3499.0,
    "currency": "BRL",
    "availability": "InStock",
    "rating_value": 4.6,
    "review_count": 1284,
    "seller": null
  }
}
```
