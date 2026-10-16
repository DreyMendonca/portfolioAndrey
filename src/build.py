"""Gera index.html e projetos/*.html do portfólio a partir dos dados abaixo.
Uso: python3 src/build.py  (rodar na pasta portfolio/)"""
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parent.parent

GITHUB = "https://github.com/DreyMendonca"
LINKEDIN = "https://linkedin.com/in/dreymendonca"
EMAIL = "drey.santos2005@gmail.com"

CURSOS = [
    {"nome": "Desenvolvimento de habilidades em Java (Projeto de Extensão Universitária)", "inst": "COMPETEC / EACH USP", "local": "USP Leste, São Paulo", "horas": 15},
    {"nome": "Introdução à Lógica de Programação", "inst": "TIM Tec / CATE (Centro de Apoio ao Trabalho e Empreendedorismo)", "local": "Portal CATE (online)"},
    {"nome": "Excel 2010", "inst": "CATE (Centro de Apoio ao Trabalho e Empreendedorismo)", "local": "Portal CATE (online)", "horas": 20},
    {"nome": "Processo Seletivo", "inst": "CATE (Centro de Apoio ao Trabalho e Empreendedorismo)", "local": "Portal CATE (online)", "horas": 12},
    {"nome": "Letramento Digital Microsoft", "inst": "CATE em parceria com a Microsoft", "local": "Portal CATE (online)"},
]
IDIOMAS = [{"lingua": "Português", "nivel": "Nativo", "barras": 5}, {"lingua": "Inglês", "nivel": "Intermediário", "barras": 3}]

PROJETOS = [
    {
        "slug": "buffet-simone",
        "nome": "Site do Buffet Simone",
        "quando": "2025 · 2º semestre",
        "resumo": "Site institucional para um buffet de eventos, com cardápio dinâmico e área administrativa.",
        "descricao": [
            "Site criado para o Buffet Simone, empresa de eventos com mais de 15 anos de mercado. A página apresenta a história da chef, o cardápio, depoimentos e um canal de contato para pedidos de orçamento.",
            "O cardápio e as fotos são gerenciados por uma área administrativa com login, onde é possível criar categorias, cadastrar pratos e enviar imagens, tudo salvo no Firebase.",
        ],
        "techs": ["React", "TypeScript", "Vite", "Tailwind CSS", "Radix UI", "Firebase"],
        "repo": "https://github.com/robertfullstack/Site-Buffet-Simone",
        "participacao": "Participei de todo o desenvolvimento do projeto em equipe: estrutura das seções da página inicial (hero, sobre, cardápio, contato), componentes de interface em React com TypeScript e a área administrativa integrada ao Firebase para o cadastro de pratos, categorias e fotos.",
        "shots": [("buffet-simone-1.jpg", "Página inicial com apresentação do buffet"), ("buffet-simone-2.jpg", "Login da área administrativa")],
    },
    {
        "slug": "estocai",
        "nome": "Estocaí",
        "quando": "2025 · 1º semestre",
        "resumo": "Sistema web de controle de estoque com dashboard de vendas e gestão de funcionários.",
        "descricao": [
            "O Estocaí é um sistema de gestão de estoque para pequenos comércios. A loja se cadastra, adiciona produtos com categoria, validade e imagem, e acompanha entradas, vendas e lucro.",
            "O dashboard reúne gráficos de produtos mais vendidos, vendas por dia, comparação de estoque e histórico de entradas. O administrador também cadastra funcionários com permissões diferentes.",
        ],
        "techs": ["React", "Firebase (Auth e Firestore)", "Chart.js", "React Router", "React Toastify"],
        "repo": "https://github.com/DreyMendonca/stock",
        "participacao": "Participei de todo o desenvolvimento: telas de login e cadastro, cadastro e edição de produtos, controle de estoque, dashboard com gráficos em Chart.js e integração com Firebase Authentication e Firestore. É o projeto que mais conversa com a minha área de dados, porque transforma o estoque em indicadores para a tomada de decisão.",
        "shots": [("estocai-1.jpg", "Tela de login"), ("estocai-2.jpg", "Cadastro da loja")],
    },
    {
        "slug": "meet-tea",
        "nome": "Meet TEA",
        "quando": "2024 · 2º semestre a 2025",
        "resumo": "Rede social inclusiva que aproxima pessoas autistas, familiares e cuidadores.",
        "descricao": [
            "O Meet TEA promove a comunicação entre pessoas autistas e seus familiares, com uma interface simples e pouco estimulante para evitar desconforto.",
            "Tem feed de publicações, perfis, chat, ajuste de tamanho de fonte, modo escuro, validação da carteira CIPTEA, sistema de denúncias e painel de administração para moderação.",
        ],
        "techs": ["React", "Firebase", "Bootstrap", "React Router", "Vercel"],
        "repo": "https://github.com/robertfullstack/Meet-TEA-3.0-Final",
        "participacao": "Participei de todo o desenvolvimento do projeto em equipe: telas de login e cadastro, feed e publicações, perfil, chat, recursos de acessibilidade (tamanho de fonte e modo escuro) e integração com Firebase.",
        "shots": [("meet-tea-1.jpg", "Login com a identidade visual do app"), ("meet-tea-2.jpg", "Página de termos e privacidade com controles de acessibilidade")],
    },
    {
        "slug": "mindrest",
        "nome": "MindRest",
        "quando": "2024 · 1º semestre",
        "resumo": "Plataforma web com conteúdos e exercícios para lidar com a ansiedade no dia a dia.",
        "descricao": [
            "O MindRest oferece uma abordagem prática para lidar com a ansiedade. A página inicial traz curiosidades e dicas sobre o tema, e o site tem duas ferramentas: um exercício de respiração guiada e uma seleção de músicas relaxantes.",
        ],
        "techs": ["HTML", "CSS", "JavaScript"],
        "repo": "https://github.com/lugustavos/MindRest",
        "participacao": "Participei de todo o desenvolvimento em equipe: layout e estilização das páginas, navegação, carrossel da página inicial e a lógica em JavaScript do exercício de respiração.",
        "shots": [("mindrest-1.jpg", "Página inicial"), ("mindrest-2.jpg", "Exercício de respiração guiada"), ("mindrest-3.jpg", "Página de músicas")],
    },
    {
        "slug": "portfolio-v1",
        "nome": "Primeiro portfólio",
        "quando": "2024 · 1º semestre",
        "resumo": "Minha primeira landing page pessoal, com apresentação, habilidades e formulário de contato.",
        "descricao": [
            "Landing page pessoal criada no início da faculdade, com apresentação, download do currículo, links para redes, seção de hard skills, projetos e formulário de contato.",
        ],
        "techs": ["HTML", "CSS"],
        "repo": "https://github.com/DreyMendonca/portfolio",
        "participacao": "Projeto individual: desenvolvi todo o layout e o estilo em HTML e CSS.",
        "shots": [("portfolio-v1-1.jpg", "Seção inicial")],
    },
]

ICON_GH = '<svg viewBox="0 0 24 24"><path d="M12 .5a12 12 0 0 0-3.8 23.4c.6.1.8-.3.8-.6v-2.2c-3.3.7-4-1.4-4-1.4-.6-1.4-1.4-1.8-1.4-1.8-1-.7.1-.7.1-.7 1.2.1 1.8 1.2 1.8 1.2 1 1.8 2.8 1.3 3.5 1 .1-.8.4-1.3.8-1.6-2.7-.3-5.5-1.3-5.5-5.9 0-1.3.5-2.4 1.2-3.2-.1-.3-.5-1.5.1-3.2 0 0 1-.3 3.3 1.2a11.5 11.5 0 0 1 6 0C17.3 4.7 18.3 5 18.3 5c.6 1.7.2 2.9.1 3.2.8.8 1.2 1.9 1.2 3.2 0 4.6-2.8 5.6-5.5 5.9.4.4.8 1.1.8 2.2v3.3c0 .3.2.7.8.6A12 12 0 0 0 12 .5z"/></svg>'
ICON_IN = '<svg viewBox="0 0 24 24"><path d="M20.4 20.5h-3.6v-5.6c0-1.3 0-3-1.8-3s-2.1 1.4-2.1 2.9v5.7H9.3V9h3.4v1.6h.1c.5-.9 1.6-1.8 3.4-1.8 3.6 0 4.3 2.4 4.3 5.5v6.2zM5.3 7.4a2.1 2.1 0 1 1 0-4.2 2.1 2.1 0 0 1 0 4.2zM7.1 20.5H3.5V9h3.6v11.5zM22.2 0H1.8C.8 0 0 .8 0 1.7v20.6c0 .9.8 1.7 1.8 1.7h20.4c1 0 1.8-.8 1.8-1.7V1.7C24 .8 23.2 0 22.2 0z"/></svg>'
ICON_DL = '<svg viewBox="0 0 24 24"><path d="M12 16 6 10l1.4-1.4 3.6 3.6V2h2v10.2l3.6-3.6L18 10l-6 6zM4 20h16v2H4z"/></svg>'


def page(title, body, prefix="", desc="Portfólio de Andrey de Mendonça Santos"):
    return f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)}</title>
<meta name="description" content="{escape(desc)}">
<link rel="icon" href="{prefix}assets/foto.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Space+Grotesk:wght@500;700&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{prefix}assets/style.css">
</head>
<body>
<canvas id="stars" aria-hidden="true"></canvas>
<header class="top"><div class="wrap">
  <a class="logo" href="{prefix}index.html"><span class="mark">AM</span>Andrey Mendonça</a>
  <nav class="nav">
    <a href="{prefix}index.html#formacao">Formação</a>
    <a href="{prefix}index.html#experiencia">Experiência</a>
    <a href="{prefix}index.html#cursos">Cursos</a>
    <a href="{prefix}index.html#idiomas">Idiomas</a>
    <a href="{prefix}index.html#projetos">Projetos</a>
  </nav>
</div></header>
{body}
<footer><div class="wrap">Andrey de Mendonça Santos · <a href="{GITHUB}">GitHub</a> · <a href="{LINKEDIN}">LinkedIn</a> · <a href="mailto:{EMAIL}">{EMAIL}</a></div></footer>
<script src="{prefix}assets/stars.js"></script>
</body>
</html>
"""


def chips(items):
    return '<div class="chips">' + "".join(f'<span class="chip">{escape(t)}</span>' for t in items) + "</div>"


def cursos_html():
    if not CURSOS:
        return '<div class="card todo">A preencher: nome do curso, instituição, local, carga horária e datas de início e término.</div>'
    out = []
    for c in CURSOS:
        out.append(f"""<div class="card"><h3>{escape(c['nome'])}</h3>
<dl class="kv"><dt>Instituição</dt><dd>{escape(c['inst'])}</dd><dt>Local</dt><dd>{escape(c['local'])}</dd>
{f"<dt>Período</dt><dd>{escape(c['periodo'])}</dd>" if c.get('periodo') else ""}</dl></div>""")
    return '<div class="grid-2">' + "".join(out) + "</div>"


def idiomas_html():
    if not IDIOMAS:
        return '<div class="card todo">A preencher: idiomas e nível em cada um.</div>'
    rows = []
    for l in IDIOMAS:
        bars = "".join(f'<i class="{"on" if i < l["barras"] else ""}"></i>' for i in range(5))
        rows.append(f'<div class="lang"><div><strong>{escape(l["lingua"])}</strong> <span class="meta">· {escape(l["nivel"])}</span></div><div class="level" aria-label="{escape(l["nivel"])}">{bars}</div></div>')
    return '<div class="card">' + "".join(rows) + "</div>"


def index():
    cards = "".join(f"""
<a class="pcard" href="projetos/{p['slug']}.html">
  <img src="assets/shots/{p['shots'][0][0]}" alt="Screenshot do {escape(p['nome'])}" loading="lazy">
  <div class="body"><h3>{escape(p['nome'])}</h3><p>{escape(p['resumo'])}</p>
  {chips(p['techs'][:4])}<span class="more">Explorar →</span></div>
</a>""" for p in PROJETOS)

    body = f"""
<main>
<section class="hero"><div class="wrap">
  <div class="orbit"><img class="photo" src="assets/foto.jpg" alt="Foto de Andrey de Mendonça Santos"></div>
  <div>
    <div class="eyebrow">Dados · Desenvolvimento de Software</div>
    <h1>Andrey de Mendonça Santos</h1>
    <p class="lead">Estudante de Desenvolvimento de Software Multiplataforma na FATEC Zona Leste e estagiário de Dados e CRM no Banco Safra. Uno SQL, análise de dados e desenvolvimento web para transformar dados em decisões.</p>
    <div class="actions">
      <a class="btn primary" href="{GITHUB}" target="_blank" rel="noopener">{ICON_GH} github.com/DreyMendonca</a>
      <a class="btn" href="{LINKEDIN}" target="_blank" rel="noopener">{ICON_IN} LinkedIn</a>
      <a class="btn" href="assets/curriculo-andrey-mendonca.pdf" download>{ICON_DL} Currículo</a>
    </div>
  </div>
</div></section>

<section class="block" id="formacao"><div class="wrap">
  <h2 data-n="01">Formação</h2><p class="sub">Curso em andamento e formação técnica.</p>
  <div class="grid-2">
    <div class="card"><span class="badge">Em andamento</span><h3 style="margin-top:10px">Desenvolvimento de Software Multiplataforma</h3>
      <dl class="kv"><dt>Faculdade</dt><dd>FATEC Zona Leste</dd><dt>Início</dt><dd>2024 · 1º semestre (fev/2024)</dd><dt>Conclusão prevista</dt><dd>2026 · 2º semestre (dez/2026)</dd></dl></div>
    <div class="card"><span class="badge">Concluído</span><h3 style="margin-top:10px">Técnico em Desenvolvimento de Sistemas</h3>
      <dl class="kv"><dt>Escola</dt><dd>ETEC</dd><dt>Período</dt><dd>2022 a 2023</dd></dl></div>
  </div>
</div></section>

<section class="block" id="experiencia"><div class="wrap">
  <h2 data-n="02">Experiência profissional</h2><p class="sub">Trabalho atual e anteriores.</p>
  <div class="timeline">
    <div class="tl-item card"><div class="head"><div><h3>Estagiário de Dados e CRM</h3><div class="meta">Banco Safra</div></div><span class="badge">jun/2025 · atual</span></div>
      <ul>
        <li>Consultas em SQL para extração, filtragem e segmentação de grandes volumes de dados de clientes.</li>
        <li>Acompanhamento de métricas de performance em dashboards operacionais e gerenciais.</li>
        <li>Validação, higienização e organização de bases de dados para análises e fluxos operacionais.</li>
        <li>Configuração de fluxos lógicos e réguas automatizadas de campanhas no Adobe Campaign.</li>
        <li>Atuação junto às áreas de negócio para transformar necessidades em requisitos analíticos.</li>
      </ul></div>
    <div class="tl-item card"><div class="head"><div><h3>Aprendiz de Análise de Dados e Open Finance</h3><div class="meta">Banco Safra</div></div><span class="badge">out/2024 · jun/2025</span></div>
      <ul>
        <li>Suporte na análise de dados regulatórios e operacionais do ecossistema Open Finance.</li>
        <li>Monitoramento de KPIs e elaboração de relatórios para a tomada de decisão.</li>
        <li>Documentação e mapeamento de fluxos de dados e processos para auditoria e controle.</li>
        <li>Acompanhamento de métricas atreladas às normas do Banco Central.</li>
      </ul></div>
  </div>
  <h3 style="margin:28px 0 12px">Competências</h3>
  {chips(["SQL", "Análise de dados", "Dashboards e KPIs", "Excel", "Modelagem básica", "Adobe Campaign", "Open Finance", "HTML", "CSS", "JavaScript", "React", "TypeScript", "Firebase", "Git e GitHub"])}
</div></section>

<section class="block" id="cursos"><div class="wrap">
  <h2 data-n="03">Cursos de extensão</h2><p class="sub">Cursos complementares realizados.</p>
  {cursos_html()}
</div></section>

<section class="block" id="idiomas"><div class="wrap">
  <h2 data-n="04">Idiomas</h2><p class="sub">Línguas e nível de proficiência.</p>
  {idiomas_html()}
</div></section>

<section class="block" id="projetos"><div class="wrap">
  <h2 data-n="05">Projetos</h2><p class="sub">Projetos dos primeiros semestres da FATEC. Clique em um card para ver detalhes.</p>
  <div class="projects">{cards}</div>
</div></section>
</main>"""
    return page("Andrey Mendonça · Portfólio", body)


def projeto(p):
    gal = "".join(f'<figure><img src="../assets/shots/{f}" alt="{escape(c)}" loading="lazy"><figcaption>{escape(c)}</figcaption></figure>' for f, c in p["shots"])
    desc = "".join(f"<p>{escape(x)}</p>" for x in p["descricao"])
    body = f"""
<main class="wrap">
  <a class="back" href="../index.html#projetos">← Voltar aos projetos</a>
  <section class="phero">
    <span class="meta mono">{escape(p['quando'])}</span>
    <h1>{escape(p['nome'])}</h1>
    <p class="meta" style="font-size:1.05rem">{escape(p['resumo'])}</p>
    <div class="actions"><a class="btn primary" href="{p['repo']}" target="_blank" rel="noopener">{ICON_GH} Ver código no GitHub</a></div>
  </section>
  <div class="grid-2" style="margin-bottom:28px">
    <div class="card prose"><h3 style="margin-bottom:10px">Sobre o projeto</h3>{desc}</div>
    <div class="card prose"><h3 style="margin-bottom:10px">Minha participação</h3><p>{escape(p['participacao'])}</p>
      <h3 style="margin:16px 0 10px">Tecnologias</h3>{chips(p['techs'])}</div>
  </div>
  <h2 style="margin-bottom:16px">Screenshots</h2>
  <div class="gallery" style="margin-bottom:48px">{gal}</div>
</main>"""
    return page(f"{p['nome']} · Andrey Mendonça", body, prefix="../", desc=p["resumo"])


if __name__ == "__main__":
    (ROOT / "index.html").write_text(index(), encoding="utf-8")
    (ROOT / "projetos").mkdir(exist_ok=True)
    for p in PROJETOS:
        (ROOT / "projetos" / f"{p['slug']}.html").write_text(projeto(p), encoding="utf-8")
    print("ok")
