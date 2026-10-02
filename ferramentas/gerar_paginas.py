#!/usr/bin/env python3
"""Gera as páginas estáticas do site E&E Contabilidade.

Uso (a partir da pasta 'site contabilidade'):  python3 ferramentas/gerar_paginas.py

Header, footer e ícones ficam aqui para não divergirem entre as páginas.
Edite textos/estrutura neste arquivo e rode novamente para regenerar os .html.
"""
from pathlib import Path
import html

RAIZ = Path(__file__).resolve().parent.parent
NOME = "E&E Contabilidade"

# ---------------------------------------------------------------- ícones
ICONES = {
    "arrow": '<path d="M5 12h14"/><path d="m12 5 7 7-7 7"/>',
    "pin": '<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/>',
    "shield": '<path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/><path d="m9 12 2 2 4-4"/>',
    "users": '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>',
    "sprout": '<path d="M7 20h10"/><path d="M10 20c5.5-2.5.8-6.4 3-10"/><path d="M9.5 9.4c1.1.8 1.8 2.2 2.3 3.7-2 .4-3.5.4-4.8-.3-1.2-.6-2.3-1.9-3-4.2 2.8-.5 4.4 0 5.5.8z"/><path d="M14.1 6a7 7 0 0 0-1.1 4c1.9-.1 3.3-.6 4.3-1.4 1-1 1.6-2.3 1.7-4.6-2.7.1-4 1-4.9 2z"/>',
    "file": '<path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z"/><path d="M14 2v4a2 2 0 0 0 2 2h4"/><path d="M10 9H8"/><path d="M16 13H8"/><path d="M16 17H8"/>',
    "filecheck": '<path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z"/><path d="M14 2v4a2 2 0 0 0 2 2h4"/><path d="m9 15 2 2 4-4"/>',
    "chart": '<path d="M3 3v16a2 2 0 0 0 2 2h16"/><path d="M18 17V9"/><path d="M13 17V5"/><path d="M8 17v-3"/>',
    "user": '<path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/>',
    "home": '<path d="M15 21v-8a1 1 0 0 0-1-1h-4a1 1 0 0 0-1 1v8"/><path d="M3 10a2 2 0 0 1 .709-1.528l7-5.999a2 2 0 0 1 2.582 0l7 5.999A2 2 0 0 1 21 10v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>',
    "lock": '<rect width="18" height="11" x="3" y="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>',
    "heart": '<path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z"/>',
    "book": '<path d="M12 7v14"/><path d="M3 18a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1h5a4 4 0 0 1 4 4 4 4 0 0 1 4-4h5a1 1 0 0 1 1 1v13a1 1 0 0 1-1 1h-6a3 3 0 0 0-3 3 3 3 0 0 0-3-3z"/>',
    "mountain": '<path d="m8 3 4 8 5-5 5 15H2L8 3z"/>',
    "trend": '<polyline points="22 7 13.5 15.5 8.5 10.5 2 17"/><polyline points="16 7 22 7 22 13"/>',
    "phone-app": '<rect width="14" height="20" x="5" y="2" rx="2"/><path d="M12 18h.01"/>',
    "folder": '<path d="M20 20a2 2 0 0 0 2-2V8a2 2 0 0 0-2-2h-7.9a2 2 0 0 1-1.69-.9L9.6 3.9A2 2 0 0 0 7.93 3H4a2 2 0 0 0-2 2v13a2 2 0 0 0 2 2Z"/>',
    "headset": '<path d="M3 11h3a2 2 0 0 1 2 2v3a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-5Zm0 0a9 9 0 1 1 18 0m0 0v5a2 2 0 0 1-2 2h-1a2 2 0 0 1-2-2v-3a2 2 0 0 1 2-2h3Z"/><path d="M21 16v2a4 4 0 0 1-4 4h-5"/>',
    "compass": '<circle cx="12" cy="12" r="10"/><path d="m16.24 7.76-1.804 5.411a2 2 0 0 1-1.265 1.265L7.76 16.24l1.804-5.411a2 2 0 0 1 1.265-1.265z"/>',
    "percent": '<line x1="19" x2="5" y1="5" y2="19"/><circle cx="6.5" cy="6.5" r="2.5"/><circle cx="17.5" cy="17.5" r="2.5"/>',
    "clipboard": '<rect width="8" height="4" x="8" y="2" rx="1"/><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><path d="M12 11h4"/><path d="M12 16h4"/><path d="M8 11h.01"/><path d="M8 16h.01"/>',
    "phone": '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/>',
    "mail": '<rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/>',
    "insta": '<rect width="20" height="20" x="2" y="2" rx="5" ry="5"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/><line x1="17.5" x2="17.51" y1="6.5" y2="6.5"/>',
    "menu": '<path d="M4 6h16M4 12h16M4 18h16"/>',
    "image": '<rect width="18" height="18" x="3" y="3" rx="2"/><circle cx="9" cy="9" r="2"/><path d="m21 15-3.09-3.09a2 2 0 0 0-2.82 0L6 21"/>',
}
WHATSAPP = ('<path class="icon-fill" d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/>')

SPRITE = ('<svg xmlns="http://www.w3.org/2000/svg" style="display:none" aria-hidden="true">'
          + "".join(f'<symbol id="i-{k}" viewBox="0 0 24 24">{v}</symbol>' for k, v in ICONES.items())
          + f'<symbol id="i-wa" viewBox="0 0 24 24">{WHATSAPP}</symbol></svg>')


def ic(nome, extra=""):
    return f'<svg class="icon {extra}" aria-hidden="true"><use href="#i-{nome}"/></svg>'


WA = '<svg class="icon icon-fill" aria-hidden="true"><use href="#i-wa"/></svg>'


# ---------------------------------------------------------------- partes comuns
def logo(claro=False, root="", home=False):
    destino = "#inicio" if home else f"{root}index.html"
    return (f'<a class="logo{" logo-claro" if claro else ""}" href="{destino}" aria-label="{NOME} — início">'
            f'<img src="{root}imagens/web/logo.png" alt="{NOME}" width="640" height="457"></a>')


def header(root="", home=False):
    h = "" if home else f"{root}index.html"
    itens = [("Início", f"{h}#inicio"), ("Serviços", f"{h}#servicos"), ("Reforma Tributária", f"{h}#reforma"),
             ("Aplicativo", f"{h}#aplicativo"), ("Sobre", f"{h}#sobre"), ("Conteúdos", f"{root}conteudos/index.html"),
             ("Contato", f"{h}#contato")]
    lis = "".join(f'<li><a href="{href}">{n}</a></li>' for n, href in itens)
    return f'''<header class="site-header">
  <div class="container header-inner">
    {logo(root=root, home=home)}
    <nav class="main-nav" id="menu" aria-label="Principal"><ul>{lis}</ul></nav>
    <a class="btn btn-verde header-cta" data-wa href="{h}#contato">{WA} Falar com uma especialista {ic("arrow")}</a>
    <button class="nav-toggle" aria-expanded="false" aria-controls="menu" aria-label="Abrir menu">{ic("menu")}</button>
  </div>
</header>'''


def footer(root="", home=False):
    h = "" if home else f"{root}index.html"
    return f'''<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">{logo(True, root, home)}<p>Você cuida da produção.<br>A E&amp;E ajuda a cuidar do resto.</p></div>
      <div><h4>E&amp;E</h4><ul><li><a href="{h}#sobre">Sobre</a></li><li><a href="{h}#contato">Contato</a></li></ul></div>
      <div><h4>Serviços</h4><ul>
        <li><a href="{h}#servicos">Assessoria ao Produtor</a></li><li><a href="{root}conteudos/nota-fiscal-produtor-rural.html">Nota Fiscal Rural</a></li>
        <li><a href="{root}conteudos/planejamento-tributario-agronegocio.html">Gestão Tributária</a></li><li><a href="{root}conteudos/imposto-de-renda-produtor-rural.html">Imposto de Renda</a></li>
        <li><a href="{root}conteudos/holding-rural-quando-faz-sentido.html">Holding Rural</a></li></ul></div>
      <div><h4>Informação</h4><ul><li><a href="{h}#reforma">Reforma Tributária</a></li><li><a href="{root}conteudos/index.html">Conteúdos</a></li><li><a href="{h}#aplicativo">Aplicativo</a></li></ul></div>
      <div><h4>Contato</h4><ul>
        <li>Bom Repouso - MG</li>
        <li><span class="todo" data-contact="whatsapp">[TODO WhatsApp]</span></li>
        <li><span class="todo" data-contact="email">[TODO e-mail]</span></li>
        <li><span class="todo" data-contact="instagram">Instagram [TODO]</span></li></ul></div>
    </div>
    <div class="footer-bottom">
      <span>© <span id="ano">2026</span> {NOME}. Todos os direitos reservados.</span>
      <nav aria-label="Legal"><a href="{root}privacidade.html">Política de Privacidade</a><a href="{root}termos.html">Termos de Uso</a></nav>
    </div>
  </div>
</footer>
<a class="wa-float" data-wa href="{h}#contato" aria-label="Falar pelo WhatsApp">{WA}</a>'''


def pagina(titulo, descricao, corpo, root="", extra_head="", classe="", home=False):
    return f'''<!doctype html>
<html lang="pt-BR" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(titulo)}</title>
<meta name="description" content="{html.escape(descricao, quote=True)}">
<meta property="og:type" content="website">
<meta property="og:locale" content="pt_BR">
<meta property="og:title" content="{html.escape(titulo, quote=True)}">
<meta property="og:description" content="{html.escape(descricao, quote=True)}">
<meta property="og:image" content="{root}imagens/web/hero.jpg">
<meta name="theme-color" content="#123b2a">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Baskervville:wght@400;500;600&family=Manrope:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{root}assets/css/style.css">
{extra_head}
</head>
<body{f' class="{classe}"' if classe else ""}>
<a class="skip-link" href="#conteudo-principal">Ir para o conteúdo</a>
{SPRITE}
{header(root, home)}
<main id="conteudo-principal">
{corpo}
</main>
{footer(root, home)}
<script src="{root}assets/js/site.js"></script>
<script>document.getElementById("ano").textContent = new Date().getFullYear();</script>
</body>
</html>
'''


# ---------------------------------------------------------------- artigos
ARTIGOS = [
    {
        "slug": "reforma-tributaria-produtor-rural",
        "titulo": "Reforma Tributária: o que muda para o produtor rural?",
        "seo": "Reforma Tributária e produtor rural: o que muda",
        "desc": "Entenda de forma clara como a Reforma Tributária pode afetar o produtor rural, o que muda com CBS e IBS e como se preparar com antecedência.",
        "cat": "Reforma Tributária",
        "img": "reforma-bg.jpg",
        "lead": "A Reforma Tributária sobre o consumo muda a forma como impostos são cobrados em toda a cadeia — e o agronegócio faz parte dela.",
        "corpo": [
            ("p", "A Reforma Tributária do consumo (Emenda Constitucional 132/2023, regulamentada pela Lei Complementar 214/2025) cria um novo modelo de tributação. Em vez de vários tributos com regras diferentes, entram em cena a CBS (federal) e o IBS (estadual e municipal), que substituem gradualmente PIS, Cofins, ICMS e ISS. A transição é escalonada, com etapas até 2033."),
            ("h2", "Por que isso importa para quem produz"),
            ("p", "O produtor rural vende para cooperativas, indústrias, atacadistas e consumidores, e compra insumos, máquinas e serviços. Como o novo sistema funciona com créditos ao longo da cadeia, a forma de emitir notas, de organizar documentos e até de negociar com compradores e fornecedores pode ser afetada."),
            ("h2", "Tratamento específico para o produtor rural"),
            ("p", "A legislação prevê regras próprias para o setor agropecuário, como tratamento diferenciado para produtores de menor porte (com base em um limite de receita anual) e alíquotas reduzidas para determinados insumos e produtos. Como os detalhes dependem do tipo de atividade, do porte e da forma de tributação de cada produtor, o ideal é avaliar cada caso."),
            ("h2", "Como se preparar desde já"),
            ("ul", ["Organizar notas fiscais, contratos e comprovantes de despesas da propriedade;", "Conhecer o enquadramento fiscal atual (pessoa física ou jurídica) e como ele se comporta no novo modelo;", "Simular impactos nas vendas e nas compras mais relevantes;", "Acompanhar as regulamentações, que ainda estão sendo detalhadas."]),
            ("p", "A E&E acompanha a Reforma Tributária de perto e pode ajudar você a entender o que muda na sua propriedade."),
        ],
        "rel": ["cbs-ibs-agronegocio", "planejamento-tributario-agronegocio"],
    },
    {
        "slug": "cbs-ibs-agronegocio",
        "titulo": "CBS e IBS: como podem impactar o agronegócio?",
        "seo": "CBS e IBS no agronegócio: impactos para o produtor",
        "desc": "O que são CBS e IBS, como funciona a não cumulatividade e quais impactos podem ser esperados para o produtor rural e o agronegócio.",
        "cat": "Reforma Tributária",
        "img": "svc-gestao.jpg",
        "lead": "CBS e IBS são os novos tributos sobre o consumo. Entenda a lógica por trás deles antes de olhar para os números.",
        "corpo": [
            ("h2", "O que são CBS e IBS"),
            ("p", "A CBS (Contribuição sobre Bens e Serviços) é federal e substitui PIS e Cofins. O IBS (Imposto sobre Bens e Serviços) é compartilhado entre estados e municípios e substitui ICMS e ISS. Juntos, formam um modelo de imposto sobre valor agregado (IVA) com regras mais uniformes."),
            ("h2", "A lógica dos créditos"),
            ("p", "No novo modelo, o tributo pago nas etapas anteriores da cadeia gera crédito para quem compra. Na prática, isso muda a forma como compradores enxergam seus fornecedores: quem consegue emitir documentos fiscais corretos e gerar crédito tende a ter mais facilidade de negociação."),
            ("h2", "Onde o agro pode sentir os efeitos"),
            ("ul", ["Compra de insumos, sementes, defensivos e máquinas;", "Venda da produção para cooperativas, indústrias e atacadistas;", "Contratação de serviços, como transporte e assistência técnica;", "Documentação fiscal e rotina de emissão de notas."]),
            ("h2", "Regras específicas do setor"),
            ("p", "A regulamentação traz tratamento específico para a produção rural, incluindo regras para produtores de menor porte e alíquotas diferenciadas para certos produtos e insumos. Os detalhes variam conforme a atividade e o enquadramento, por isso vale uma análise individual."),
            ("p", "Quer entender o que CBS e IBS significam para a sua propriedade? Fale com a equipe da E&E."),
        ],
        "rel": ["reforma-tributaria-produtor-rural", "planejamento-tributario-agronegocio"],
    },
    {
        "slug": "nota-fiscal-produtor-rural",
        "titulo": "Nota Fiscal Rural: o que o produtor precisa saber?",
        "seo": "Nota fiscal do produtor rural: o que você precisa saber",
        "desc": "Guia introdutório sobre nota fiscal do produtor rural: quando emitir, cuidados com o cadastro, certificado digital e boas práticas de organização.",
        "cat": "Nota Fiscal Rural",
        "img": "svc-nota-fiscal.jpg",
        "lead": "Emitir a nota fiscal corretamente protege a operação, facilita a venda e evita dores de cabeça com o fisco.",
        "corpo": [
            ("h2", "Por que a nota fiscal é tão importante"),
            ("p", "A nota fiscal comprova a venda ou a movimentação da mercadoria, sustenta a escrituração da atividade rural e é a base para a apuração de tributos e para a declaração do Imposto de Renda. Com a Reforma Tributária, a qualidade da documentação fiscal tende a ganhar ainda mais relevância."),
            ("h2", "Quando o produtor costuma emitir"),
            ("ul", ["Na venda da produção;", "Em transferências e remessas de mercadorias;", "Em determinadas operações de entrada e devolução;", "Em outras situações previstas na legislação do seu estado."]),
            ("p", "As regras variam conforme o estado, o tipo de operação e o enquadramento do produtor. Em Minas Gerais, a emissão é eletrônica, e o procedimento correto depende da situação de cada produtor."),
            ("h2", "Cuidados que evitam problemas"),
            ("ul", ["Manter o cadastro (inclusive a inscrição estadual) regular e atualizado;", "Conferir dados do comprador, produto, quantidade e valores antes de emitir;", "Guardar os arquivos das notas emitidas e recebidas pelo prazo legal;", "Manter o certificado digital dentro da validade, quando exigido."]),
            ("h2", "Tecnologia para simplificar"),
            ("p", "Ferramentas digitais ajudam a emitir notas com menos erros e a manter tudo organizado. A E&E orienta o produtor e oferece um aplicativo para facilitar essa rotina."),
        ],
        "rel": ["imposto-de-renda-produtor-rural", "reforma-tributaria-produtor-rural"],
    },
    {
        "slug": "imposto-de-renda-produtor-rural",
        "titulo": "Imposto de Renda do Produtor Rural",
        "seo": "Imposto de Renda do produtor rural: pontos de atenção",
        "desc": "Pontos de atenção sobre o Imposto de Renda do produtor rural pessoa física: apuração da atividade rural, escrituração e organização de documentos.",
        "cat": "Imposto de Renda",
        "img": "svc-ir.jpg",
        "lead": "A atividade rural tem regras próprias no Imposto de Renda. Conhecê-las ajuda a declarar com segurança e a planejar melhor.",
        "corpo": [
            ("h2", "A atividade rural na declaração"),
            ("p", "O produtor rural pessoa física que obtém receitas da atividade rural apura o resultado dessa atividade em um demonstrativo próprio dentro da declaração anual de Imposto de Renda. Há critérios de obrigatoriedade definidos pela Receita Federal a cada ano."),
            ("h2", "Formas de apurar o resultado"),
            ("p", "De modo geral, o resultado pode ser apurado com base na escrituração (como o Livro Caixa), que considera receitas e despesas efetivamente comprovadas, ou por uma forma simplificada prevista na legislação, com percentual sobre a receita bruta. Cada opção tem vantagens e limitações, e a melhor escolha depende do perfil da propriedade."),
            ("h2", "Organização faz diferença"),
            ("ul", ["Separar as finanças da propriedade das finanças pessoais;", "Guardar notas fiscais, recibos e comprovantes de despesas;", "Registrar financiamentos, investimentos e bens da atividade;", "Acompanhar prejuízos de anos anteriores, que podem ser compensados nos termos da lei."]),
            ("h2", "Atenção às particularidades"),
            ("p", "Sazonalidade de receitas, venda de bens da propriedade e financiamentos rurais são exemplos de situações que exigem cuidado. Um acompanhamento contábil ao longo do ano evita a correria na hora de declarar."),
        ],
        "rel": ["planejamento-tributario-agronegocio", "nota-fiscal-produtor-rural"],
    },
    {
        "slug": "holding-rural-quando-faz-sentido",
        "titulo": "Holding Rural: quando faz sentido?",
        "seo": "Holding rural: quando faz sentido para a propriedade",
        "desc": "O que é uma holding rural, para que serve no planejamento patrimonial e sucessório e quais cuidados considerar antes de constituir uma.",
        "cat": "Holding Rural",
        "img": "svc-holding.jpg",
        "lead": "A holding rural pode ajudar a organizar o patrimônio e a sucessão da família produtora — mas não é solução para todos os casos.",
        "corpo": [
            ("h2", "O que é uma holding rural"),
            ("p", "É uma empresa criada para deter e administrar bens, como terras e outros ativos ligados à atividade rural. Ela pode centralizar a gestão do patrimônio e facilitar a organização da sucessão familiar."),
            ("h2", "Quando pode fazer sentido"),
            ("ul", ["Patrimônio rural relevante e que precisa de uma gestão mais organizada;", "Desejo de planejar a sucessão em vida, com regras claras entre herdeiros;", "Necessidade de separar o patrimônio da operação da atividade;", "Famílias que querem dar continuidade à propriedade ao longo das gerações."]),
            ("h2", "Cuidados antes de decidir"),
            ("p", "Constituir e manter uma holding tem custos, obrigações contábeis e implicações tributárias, como as que envolvem a transferência de bens e a doação de quotas. Em alguns casos, a estrutura não compensa. Por isso, a decisão exige análise do patrimônio, da família e dos objetivos, com apoio contábil e jurídico."),
            ("h2", "Planejamento com calma"),
            ("p", "Quanto mais cedo o assunto entra na conversa, mais opções existem. A E&E pode ajudar você a avaliar se a holding rural faz sentido para a sua realidade."),
        ],
        "rel": ["planejamento-tributario-agronegocio", "imposto-de-renda-produtor-rural"],
    },
    {
        "slug": "planejamento-tributario-agronegocio",
        "titulo": "Planejamento tributário no agronegócio",
        "seo": "Planejamento tributário no agronegócio: por onde começar",
        "desc": "Como o planejamento tributário ajuda produtores rurais e empresas do agronegócio a organizar a operação e a tomar decisões com mais segurança.",
        "cat": "Gestão Tributária",
        "img": "svc-gestao.jpg",
        "lead": "Planejar é escolher, dentro da lei, o caminho mais adequado para a sua operação — antes que a decisão vire urgência.",
        "corpo": [
            ("h2", "O que é planejamento tributário"),
            ("p", "É o estudo antecipado das alternativas legais de tributação para reduzir riscos e organizar o fluxo de caixa. Não tem relação com sonegação: o objetivo é entender as regras e tomar decisões conscientes."),
            ("h2", "Pontos que costumam entrar na análise"),
            ("ul", ["Atuar como pessoa física ou por meio de uma empresa;", "Regime de tributação mais adequado à realidade da propriedade;", "Sazonalidade das receitas e dos custos ao longo do ano;", "Estrutura de compras, vendas e contratos com fornecedores e compradores;", "Impactos da Reforma Tributária no médio prazo."]),
            ("h2", "A base é a informação organizada"),
            ("p", "Sem dados confiáveis, não há planejamento. Notas fiscais em dia, escrituração organizada e controle de receitas e despesas permitem simular cenários e enxergar oportunidades e riscos."),
            ("h2", "Acompanhamento ao longo do ano"),
            ("p", "O planejamento tributário funciona melhor quando é contínuo: revisar o cenário periodicamente evita surpresas e prepara a propriedade para mudanças na legislação."),
        ],
        "rel": ["reforma-tributaria-produtor-rural", "holding-rural-quando-faz-sentido"],
    },
]
POR_SLUG = {a["slug"]: a for a in ARTIGOS}


ICONE_ARTIGO = {"reforma-tributaria-produtor-rural": "compass", "cbs-ibs-agronegocio": "percent",
                "nota-fiscal-produtor-rural": "filecheck", "imposto-de-renda-produtor-rural": "user",
                "holding-rural-quando-faz-sentido": "home", "planejamento-tributario-agronegocio": "chart"}


def card_artigo(a, root):
    k = ARTIGOS.index(a) % 6 + 1
    return f'''<a class="card-art reveal" href="{root}conteudos/{a["slug"]}.html">
  <figure class="painel tema-{k}" aria-hidden="true"><span class="painel-ico">{ic(ICONE_ARTIGO[a["slug"]])}</span></figure>
  <div class="body"><span class="cat">{a["cat"]}</span><h3>{a["titulo"]}</h3><span class="ler">Ler artigo {ic("arrow")}</span></div>
</a>'''


def gerar_artigo(a):
    root = "../"
    corpo = ""
    lista = None
    for tipo, val in a["corpo"]:
        if tipo == "h2":
            corpo += f"<h2>{val}</h2>\n"
        elif tipo == "p":
            corpo += f"<p>{val}</p>\n"
        else:
            corpo += "<ul>" + "".join(f"<li>{i}</li>" for i in val) + "</ul>\n"
    rel = "".join(card_artigo(POR_SLUG[s], root) for s in a["rel"])
    ld = f'''<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Article","headline":"{a["titulo"]}","description":"{a["desc"]}","inLanguage":"pt-BR","author":{{"@type":"Organization","name":"{NOME}"}},"publisher":{{"@type":"Organization","name":"{NOME}"}}}}</script>'''
    body = f'''<section class="page-hero">
  <img src="{root}imagens/web/{a["img"]}" alt="" width="1200" height="600">
  <div class="container">
    <nav class="breadcrumb" aria-label="Você está em"><a href="{root}index.html">Início</a> / <a href="{root}conteudos/index.html">Conteúdos</a> / {a["cat"]}</nav>
    <span class="eyebrow dourado">{a["cat"]}</span>
    <h1>{a["titulo"]}</h1>
    <p class="lead">{a["lead"]}</p>
  </div>
</section>
<article class="artigo">
  <div class="container">
    <p class="aviso">Conteúdo informativo, sem caráter de consultoria individual. <span class="todo">[TODO: revisão técnica pela equipe E&amp;E antes da publicação]</span></p>
    {corpo}
    <div class="artigo-cta">
      <h2>Vamos conversar sobre a sua propriedade?</h2>
      <p>Nossa equipe está pronta para entender sua necessidade e orientar você.</p>
      <a class="btn btn-dourado" data-wa href="{root}index.html#contato">{WA} Falar com uma especialista {ic("arrow")}</a>
    </div>
  </div>
</article>
<section class="relacionados">
  <div class="container">
    <h2>Continue lendo</h2>
    <div class="grid-artigos" style="grid-template-columns:repeat(auto-fit,minmax(280px,1fr))">{rel}</div>
  </div>
</section>'''
    (RAIZ / "conteudos").mkdir(exist_ok=True)
    (RAIZ / "conteudos" / f'{a["slug"]}.html').write_text(
        pagina(f'{a["seo"]} | {NOME}', a["desc"], body, root, ld), encoding="utf-8")


def gerar_hub():
    root = "../"
    cards = "".join(card_artigo(a, root) for a in ARTIGOS)
    body = f"""<section class="page-hero">
  <img src="{root}imagens/web/reforma-bg.jpg" alt="" width="1200" height="600">
  <div class="container">
    <nav class="breadcrumb" aria-label="Você está em"><a href="{root}index.html">Início</a> / Conteúdos</nav>
    <span class="eyebrow dourado">ARTIGOS E GUIAS</span>
    <h1>Informação para o produtor rural</h1>
    <p class="lead">Guias simples e diretos sobre Reforma Tributária, nota fiscal, imposto de renda e planejamento para a propriedade.</p>
  </div>
</section>
<section class="section conteudos">
  <div class="container"><div class="grid-artigos">{cards}</div></div>
</section>"""
    (RAIZ / "conteudos").mkdir(exist_ok=True)
    (RAIZ / "conteudos" / "index.html").write_text(pagina(
        f"Conteúdos para o produtor rural | {NOME}",
        "Artigos e guias da E&E Contabilidade sobre Reforma Tributária, nota fiscal rural, imposto de renda, holding rural e planejamento tributário.",
        body, root), encoding="utf-8")


# ---------------------------------------------------------------- páginas legais
def gerar_legal(arq, titulo, desc, secoes):
    corpo_txt = "".join(f"<h2>{t}</h2>{p}" for t, p in secoes)
    body = f'''<section class="page-hero"><img src="imagens/web/reforma-bg.jpg" alt="" width="1200" height="600"><div class="container">
  <nav class="breadcrumb" aria-label="Você está em"><a href="index.html">Início</a> / {titulo}</nav><h1>{titulo}</h1></div></section>
<article class="artigo legal"><div class="container">
  <p class="aviso"><span class="todo">[TODO: texto provisório — revisar com assessoria jurídica e completar dados da empresa antes de publicar]</span></p>
  {corpo_txt}
</div></article>'''
    (RAIZ / arq).write_text(pagina(f"{titulo} | {NOME}", desc, body), encoding="utf-8")


# ---------------------------------------------------------------- home
SERVICOS = [
    ("Assessoria ao Produtor Rural", "Apoio contábil, fiscal e tributário para a rotina da propriedade.", "svc-assessoria.jpg", "sprout", "Fotografia de produtor rural colhendo morangos ao pôr do sol", "#contato", "Falar com a E&E"),
    ("Nota Fiscal Rural", "Orientação e tecnologia para simplificar a emissão de documentos fiscais.", "svc-nota-fiscal.jpg", "file", "Produtor rural usando o celular em plantação de morango", "conteudos/nota-fiscal-produtor-rural.html", "Ler o guia"),
    ("Gestão Tributária", "Planejamento e acompanhamento tributário para o agronegócio.", "svc-gestao.jpg", "chart", "Estufas agrícolas e plantação em vale do Sul de Minas", "conteudos/planejamento-tributario-agronegocio.html", "Ler o guia"),
    ("Imposto de Renda", "Atendimento às particularidades fiscais do produtor rural.", "svc-ir.jpg", "user", "Morangos maduros e flores na lavoura", "conteudos/imposto-de-renda-produtor-rural.html", "Ler o guia"),
    ("Holding Rural", "Planejamento patrimonial e sucessório.", "svc-holding.jpg", "home", "Propriedade rural com montanhas ao fundo durante o pôr do sol", "conteudos/holding-rural-quando-faz-sentido.html", "Ler o guia"),
    ("Certificado Digital", "Praticidade e segurança para suas obrigações digitais.", "svc-certificado.jpg", "lock", "Produtor com celular em mãos na lavoura", "#contato", "Falar com a E&E"),
]
DIFS = [("users", "Atendimento especializado no agro"), ("shield", "Segurança e conformidade fiscal"),
        ("sprout", "Experiência com produtores rurais"), ("heart", "Relacionamento próximo"),
        ("mountain", "Conhecimento da realidade regional")]
REFORMA = [("percent", "CBS e IBS", "Entenda como os novos tributos podem impactar sua atividade."),
           ("clipboard", "Novas obrigações fiscais", "Prepare sua propriedade para as mudanças."),
           ("trend", "Planejamento tributário", "Antecipe impactos e organize sua operação."),
           ("compass", "Acompanhamento especializado", "Conte com orientação durante a transição.")]
BENEF = [("filecheck", "Emissão simplificada de notas"), ("folder", "Informações organizadas"),
         ("phone-app", "Praticidade no dia a dia"), ("headset", "Suporte da equipe E&E")]
PILARES = [("heart", "Proximidade", "Estar perto de quem produz."), ("book", "Conhecimento", "Contábil, fiscal e tributário."),
           ("shield", "Segurança", "Obrigações em dia, com tranquilidade."), ("sprout", "Compromisso com o agro", "Entender a realidade de cada propriedade.")]
ASSUNTOS = ["Assessoria ao Produtor Rural", "Nota Fiscal Rural", "Reforma Tributária", "Imposto de Renda", "Holding Rural",
            "Certificado Digital", "Aplicativo", "Outro"]


def gerar_home():
    dif = "".join(f'<li class="dif-item">{ic(i)}<span>{t}</span></li>' for i, t in DIFS)
    svc = "".join(f'''<article class="card-svc reveal"><figure class="painel tema-{k}" aria-hidden="true"><span class="painel-ico">{ic(i)}</span></figure>
  <div class="body"><h3>{t}</h3><p>{d}</p><a class="link-seta" href="{href}">{rotulo} {ic("arrow")}</a></div></article>'''
                  for k, (t, d, img, i, alt, href, rotulo) in enumerate(SERVICOS, 1))
    ref = "".join(f'<div class="card-ref reveal">{ic(i)}<div><h3>{t}</h3><p>{d}</p></div></div>' for i, t, d in REFORMA)
    ben = "".join(f'<li class="benef">{ic(i)}<span>{t}</span></li>' for i, t in BENEF)
    opts = "".join(f"<option>{a}</option>" for a in ASSUNTOS)
    ld = f'''<script type="application/ld+json">{{"@context":"https://schema.org","@type":"AccountingService","name":"{NOME}","description":"Contabilidade para produtor rural e agronegócio em Bom Repouso - MG.","address":{{"@type":"PostalAddress","addressLocality":"Bom Repouso","addressRegion":"MG","addressCountry":"BR"}},"areaServed":["Bom Repouso","Sul de Minas"],"knowsAbout":["Contabilidade rural","Reforma Tributária","Nota fiscal do produtor rural","Imposto de Renda do produtor rural","Holding rural"]}}</script>'''
    body = f'''<!-- HERO -->
<section class="hero" id="inicio">
  <!-- Imagem gerada por IA (temporária). Para trocar: substitua imagens/web/hero.jpg -->
  <img class="hero-img" src="imagens/web/hero.jpg" alt="Produtor rural observando plantação de morango em estufas, com montanhas do Sul de Minas ao pôr do sol" width="1774" height="887" fetchpriority="high">
  <div class="container">
    <div class="hero-content">
      <span class="selo">ESPECIALISTAS NO AGRONEGÓCIO • BOM REPOUSO E REGIÃO</span>
      <h1>Contabilidade<br>que entende<br><span class="dourado">o campo.</span></h1>
      <p class="sub">Gestão tributária, tecnologia e assessoria especializada para o produtor rural.</p>
      <p class="compl">Da emissão de notas fiscais à Reforma Tributária, ajudamos você a cuidar das obrigações da propriedade com mais segurança e tranquilidade.</p>
      <div class="hero-btns">
        <a class="btn btn-verde" data-wa href="#contato">{WA} Falar com uma especialista {ic("arrow")}</a>
        <a class="btn btn-outline-claro" href="#reforma">Entender a Reforma Tributária {ic("arrow")}</a>
      </div>
    </div>
  </div>
  <aside class="hero-card">{ic("pin")}<div><strong>Bom Repouso e Bueno Brandão - MG</strong><span>Dois escritórios para atender produtores de toda a região.</span></div></aside>
</section>

<!-- DIFERENCIAIS -->
<section class="diferenciais" aria-label="Diferenciais"><div class="container"><ul class="dif-grid">{dif}</ul></div></section>

<!-- SERVIÇOS -->
<section class="section" id="servicos">
  <div class="container">
    <div class="servicos-head reveal">
      <span class="eyebrow">NOSSOS SERVIÇOS</span>
      <h2 class="section-title">Soluções completas<br>para o produtor rural</h2>
      <p style="margin-top:18px;max-width:560px;color:#4a524c">Contabilidade rural e assessoria tributária para produtores de Bom Repouso e do Sul de Minas.</p>
    </div>
    <div class="grid-servicos">{svc}</div>
  </div>
</section>

<!-- REFORMA TRIBUTÁRIA -->
<section class="section reforma" id="reforma">
  <img class="reforma-bg" src="imagens/web/reforma-bg.jpg" alt="" loading="lazy" width="1774" height="457">
  <div class="container">
    <div class="reveal">
      <span class="eyebrow" style="color:var(--dourado-claro)">REFORMA TRIBUTÁRIA</span>
      <h2>O agro está mudando.<br>Sua propriedade está preparada?</h2>
      <p>A Reforma Tributária traz novas regras e impactos para o produtor rural. Conte com acompanhamento especializado para entender as mudanças e se preparar com antecedência.</p>
      <a class="btn btn-dourado" href="conteudos/reforma-tributaria-produtor-rural.html">Entender a Reforma Tributária {ic("arrow")}</a>
      <p class="reforma-mais">Quer ir mais fundo? <a href="conteudos/cbs-ibs-agronegocio.html">Veja como CBS e IBS podem impactar o agronegócio</a>.</p>
    </div>
    <div class="reforma-cards">{ref}</div>
  </div>
</section>

<!-- APLICATIVO -->
<section class="section app" id="aplicativo">
  <div class="container app-grid">
    <div class="app-text reveal">
      <span class="eyebrow">TECNOLOGIA A FAVOR DO PRODUTOR</span>
      <h2>Nota fiscal rural<br>na palma da mão.</h2>
      <p>Mais praticidade para a rotina do produtor. Emita suas notas e mantenha suas informações organizadas diretamente pelo celular.</p>
      <a class="btn btn-verde" data-wa href="#contato">Conhecer o aplicativo {ic("arrow")}</a>
    </div>
    <div class="phone-wrap reveal">
      <div class="phone">
        <div class="phone-screen">
          <img src="imagens/app-screenshot.png" alt="Tela de login do aplicativo E&amp;E Contabilidade">
        </div>
      </div>
    </div>
    <div class="benef-card reveal"><ul>{ben}</ul></div>
  </div>
</section>

<!-- SOBRE -->
<section class="section sobre" id="sobre">
  <div class="container">
    <div class="reveal">
      <span class="eyebrow">QUEM SOMOS</span>
      <h2 class="section-title sobre-titulo">Ao lado de quem<br>faz o campo acontecer.</h2>
    </div>
    <div class="sobre-grid">
      <div class="sobre-foto reveal">
        <img src="imagens/web/sobre-equipe.jpg" alt="Sócias e equipe da E&amp;E Contabilidade, de camisa branca com a logo bordada" loading="lazy" width="1600" height="1066">
      </div>
      <div class="sobre-txt reveal">
        <h3>E&amp;E Contabilidade</h3>
        <p>Com atuação voltada ao produtor rural e ao agronegócio, a E&amp;E une conhecimento contábil, acompanhamento tributário e tecnologia para tornar a gestão mais simples e segura.</p>
        <p>De Bom Repouso para toda a região, buscamos estar próximos de quem produz, entendendo a realidade de cada propriedade e oferecendo orientação para cada etapa do negócio rural.</p>
        <div class="mv mv-um">
          <div><h4>Nossa missão</h4><p>Apoiar produtores e empresas do agronegócio com orientação contábil e tributária próxima, clara e responsável.</p></div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- EQUIPE -->
<section class="section equipe" id="equipe">
  <div class="container">
    <div class="equipe-head reveal">
      <span class="eyebrow">NOSSA EQUIPE</span>
      <h2 class="section-title">Conheça quem cuida<br>do seu negócio.</h2>
    </div>
    <div class="galeria reveal">
      <figure class="g-main"><img src="imagens/web/galeria-equipe-morango.jpg" alt="Equipe da E&amp;E Contabilidade reunida em frente a uma escultura de morango, com as montanhas do Sul de Minas ao fundo" loading="lazy" width="1800" height="1350"></figure>
      <figure class="g-a"><img src="imagens/web/galeria-escritorio.jpg" alt="Sala de reuniões do escritório da E&amp;E Contabilidade" loading="lazy" width="1400" height="933"></figure>
      <figure class="g-b"><img src="imagens/web/galeria-socias-morango.jpg" alt="Sócias da E&amp;E Contabilidade sentadas na escultura de morango" loading="lazy" width="900" height="1200"></figure>
    </div>
  </div>
</section>

<!-- CONTATO -->
<section class="section contato" id="contato">
  <img class="contato-bg" src="imagens/web/contato-bg.jpg" alt="" loading="lazy" width="1200" height="795">
  <div class="container">
    <div class="reveal">
      <span class="eyebrow" style="color:var(--dourado-claro)">FALE COM A E&amp;E</span>
      <h2>Vamos conversar<br>sobre a sua propriedade?</h2>
      <p class="lead">Nossa equipe está pronta para entender sua necessidade e orientar você.</p>
      <div class="contato-cards">
        <a class="c-card" data-wa href="#contato"><span class="ico">{WA}</span><div><small>WhatsApp</small><span class="todo" data-contact="whatsapp">[TODO: número]</span></div></a>
        <a class="c-card"><span class="ico">{ic("phone")}</span><div><small>Telefone</small><span class="todo" data-contact="telefone">[TODO: telefone]</span></div></a>
        <a class="c-card"><span class="ico">{ic("mail")}</span><div><small>E-mail</small><span class="todo" data-contact="email">[TODO: e-mail]</span></div></a>
        <div class="c-card"><span class="ico">{ic("pin")}</span><div><small>Localização</small><span>Bom Repouso - MG</span></div></div>
        <a class="c-card"><span class="ico">{ic("insta")}</span><div><small>Instagram</small><span class="todo" data-contact="instagram">[TODO: Instagram]</span></div></a>
      </div>
    </div>
    <form class="form-card reveal" id="form-contato" novalidate>
      <h3>Envie uma mensagem</h3>
      <div class="field"><label for="f-nome">Nome</label><input id="f-nome" name="nome" autocomplete="name" required></div>
      <div class="form-row">
        <div class="field"><label for="f-tel">Telefone / WhatsApp</label><input id="f-tel" name="telefone" type="tel" autocomplete="tel" required></div>
        <div class="field"><label for="f-mail">E-mail</label><input id="f-mail" name="email" type="email" autocomplete="email" required></div>
      </div>
      <div class="field"><label for="f-assunto">Assunto</label><select id="f-assunto" name="assunto" required><option value="" disabled selected>Selecione</option>{opts}</select></div>
      <div class="field"><label for="f-msg">Como podemos ajudar?</label><textarea id="f-msg" name="mensagem"></textarea></div>
      <label class="check"><input type="checkbox" name="lgpd" required><span>Concordo com o tratamento dos meus dados para retorno do contato, conforme a <a href="privacidade.html">Política de Privacidade</a> (LGPD).</span></label>
      <button class="btn btn-verde" type="submit">Enviar mensagem {ic("arrow")}</button>
      <a class="btn btn-outline" data-wa href="#contato">{WA} Prefiro falar pelo WhatsApp</a>
      <p class="form-status" role="status"></p>
    </form>
  </div>
</section>'''
    (RAIZ / "index.html").write_text(pagina(
        "Contabilidade para Produtor Rural em Bom Repouso - MG | E&E Contabilidade",
        "Contabilidade rural e para o agronegócio em Bom Repouso - MG e Sul de Minas. Assessoria ao produtor rural, nota fiscal, imposto de renda, holding rural e Reforma Tributária.",
        body, "", ld, home=True), encoding="utf-8")


LEGAL_PRIV = [
    ("Quem somos", "<p>Este site é mantido pela E&amp;E Contabilidade, em Bom Repouso - MG. <span class=\"todo\">[TODO: razão social, CNPJ e endereço]</span></p>"),
    ("Quais dados coletamos", "<p>Ao preencher o formulário de contato, coletamos nome, telefone/WhatsApp, e-mail, assunto e a mensagem enviada. Não coletamos dados sensíveis por meio do site.</p>"),
    ("Para que usamos", "<p>Usamos esses dados apenas para responder ao seu contato e prestar informações sobre nossos serviços. A base legal é o seu consentimento (LGPD, art. 7º, I), que pode ser retirado a qualquer momento.</p>"),
    ("Compartilhamento e armazenamento", "<p>Não vendemos dados. Eles podem ser tratados por prestadores que apoiam o envio e o armazenamento das mensagens, sob obrigações de confidencialidade. Mantemos os dados pelo tempo necessário para o atendimento e para cumprir obrigações legais. <span class=\"todo\">[TODO: informar ferramentas utilizadas]</span></p>"),
    ("Seus direitos", "<p>Você pode solicitar confirmação de tratamento, acesso, correção, anonimização, portabilidade, eliminação dos dados e revogação do consentimento, conforme o art. 18 da LGPD. <span class=\"todo\">[TODO: canal do encarregado / e-mail de contato]</span></p>"),
    ("Cookies e estatísticas", "<p>Este site não utiliza cookies de rastreamento próprios. <span class=\"todo\">[TODO: atualizar caso sejam adicionadas ferramentas de análise ou publicidade]</span></p>"),
    ("Atualizações", "<p>Esta política pode ser atualizada. A versão vigente estará sempre nesta página.</p>"),
]
LEGAL_TERMOS = [
    ("Uso do site", "<p>Ao navegar neste site, você concorda com estes termos. O site apresenta os serviços da E&amp;E Contabilidade e conteúdos informativos sobre temas contábeis e tributários.</p>"),
    ("Caráter informativo", "<p>Os conteúdos têm finalidade informativa e não substituem a análise do caso concreto por um profissional habilitado. A legislação tributária muda com frequência.</p>"),
    ("Propriedade intelectual", "<p>Textos, marca, logotipo e demais elementos do site pertencem à E&amp;E Contabilidade ou são usados com autorização, sendo vedada a reprodução sem permissão.</p>"),
    ("Links e disponibilidade", "<p>O site pode conter links para serviços de terceiros, pelos quais não nos responsabilizamos. Podemos alterar ou suspender o site a qualquer momento.</p>"),
    ("Foro", "<p><span class=\"todo\">[TODO: definir foro e demais cláusulas com assessoria jurídica]</span></p>"),
]

if __name__ == "__main__":
    gerar_home()
    gerar_hub()
    for a in ARTIGOS:
        gerar_artigo(a)
    gerar_legal("privacidade.html", "Política de Privacidade", "Como a E&E Contabilidade trata os dados pessoais coletados neste site, conforme a LGPD.", LEGAL_PRIV)
    gerar_legal("termos.html", "Termos de Uso", "Termos de uso do site da E&E Contabilidade.", LEGAL_TERMOS)
    print("Páginas geradas em", RAIZ)
