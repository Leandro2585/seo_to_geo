// Bundle sintético de uma Single Page Application (renderização no cliente - CSR).
// O conteúdo do produto só existe após a execução deste JavaScript no navegador.
(function () {
  var MARKUP = "<section class=\"produto\"> <h1>Smartphone Nexo X12 Pro 256 GB - Grafite</h1> <p class=\"marca\">Marca: Nexo</p> <p class=\"avaliacao\">4,6 de 5 estrelas (1.284 avaliações)</p> <p class=\"preco\">R$ 3.499,00 à vista</p> <p class=\"parcelamento\">ou 12x de R$ 291,58 sem juros no cartão</p> <p class=\"estoque\">Em estoque - envio imediato</p> <p class=\"vendedor\">Vendido e entregue por Loja Exemplo</p> </section> <section class=\"descricao\"> <h2>Descrição do produto</h2> <p>O Nexo X12 Pro foi projetado para quem busca desempenho de ponta no dia a dia. A tela AMOLED de 6,7 polegadas com taxa de atualização de 120 Hz garante rolagem fluida em redes sociais, jogos e vídeos em alta definição.</p> <p>O conjunto de câmeras traseiras conta com sensor principal de 200 MP, ultra-angular de 12 MP e teleobjetiva com zoom óptico de 3x, permitindo fotos detalhadas mesmo em ambientes com pouca luz. A câmera frontal de 32 MP é ideal para chamadas de vídeo.</p> <p>Com bateria de 5.000 mAh e carregamento rápido de 67 W, o aparelho vai de 0 a 100% em aproximadamente 40 minutos. O armazenamento interno de 256 GB e os 12 GB de memória RAM permitem manter dezenas de aplicativos abertos sem travamentos.</p> </section> <section class=\"especificacoes\"> <h2>Especificações técnicas</h2> <ul> <li>Tela: AMOLED 6,7\" 120 Hz</li> <li>Processador: octa-core 3,2 GHz</li> <li>Memória RAM: 12 GB</li> <li>Armazenamento: 256 GB</li> <li>Bateria: 5.000 mAh, carregamento de 67 W</li> <li>Garantia: 12 meses pelo fabricante</li> </ul> </section> <section class=\"opinioes\"> <h2>Opiniões de clientes</h2> <p><strong>Carla M.</strong> - 5 estrelas - \"Bateria excelente, dura o dia inteiro.\"</p> <p><strong>Rafael T.</strong> - 4 estrelas - \"Câmera muito boa, mas esquenta um pouco em jogos.\"</p> <p><strong>Joana P.</strong> - 3 estrelas - \"Bom aparelho, mas achei caro pelo que entrega.\"</p> </section> <section class=\"relacionados\"> <h2>Quem viu este produto também viu</h2> <p>Smartphone Nexo X10 128 GB - R$ 2.199,00 - 4,3 estrelas (532 avaliações) - vendido por TechMais</p> <p>Smartphone Orbi S8 256 GB - R$ 3.899,00 - 4,7 estrelas (2.010 avaliações) - vendido por Loja Exemplo</p> </section>";
  var PRODUCT_JSONLD = {
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Smartphone Nexo X12 Pro 256 GB - Grafite",
  "sku": "NX12P-256-GRF",
  "brand": {
    "@type": "Brand",
    "name": "Nexo"
  },
  "description": "Smartphone Nexo X12 Pro com tela AMOLED de 6,7 polegadas, câmera de 200 MP, 12 GB de RAM, 256 GB de armazenamento e bateria de 5.000 mAh.",
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": 4.6,
    "bestRating": 5,
    "reviewCount": 1284
  },
  "offers": {
    "@type": "Offer",
    "url": "https://loja-exemplo.com.br/nexo-x12-pro-256gb",
    "price": 3499.0,
    "priceCurrency": "BRL",
    "availability": "https://schema.org/InStock",
    "itemCondition": "https://schema.org/NewCondition",
    "seller": {
      "@type": "Organization",
      "name": "Loja Exemplo"
    }
  }
};

  function render() {
    var root = document.getElementById("root");
    root.innerHTML = "<main>" + MARKUP + "</main>";
    // Na variante CSR, o JSON-LD também é injetado dinamicamente via JavaScript
    if (root.getAttribute("data-inject-jsonld") === "true") {
      var s = document.createElement("script");
      s.type = "application/ld+json";
      s.text = JSON.stringify(PRODUCT_JSONLD);
      document.head.appendChild(s);
    }
  }
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", render);
  } else {
    render();
  }
})();
