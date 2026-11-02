# Etapa 8: Ativação

Traduz a marca aprovada (etapas 1 a 7) em regras operacionais para os quatro usos. Faz só os usos marcados no Intake. Cada regra cita de qual arquivo da marca vem (`origem:`) e traz um exemplo aplicado. Saída em `_brands/<marca>/ativacao/`.

Regra geral: nada novo de marca nasce aqui. Se uma pergunta revela lacuna de etapa anterior, voltar à etapa e declarar ao usuário.

## A. Conteúdo (`ativacao/conteudo.md`)

### A.0 Antes de perguntar: mapear o que o projeto já tem
Procurar no projeto da marca (e dizer ao usuário o que achou) antes de qualquer pergunta; **não perguntar o que um arquivo já responde**:
- **Esteira e pastas de produção** (por exemplo, pastas a aprovar, aprovado, publicado, revisar), nomes de arquivo e metadados obrigatórios: a ativação **herda** isso, não recria.
- **Conteúdo já publicado ou em produção** (os posts existentes): olhar canais, formatos e cadência **reais** para as perguntas partirem do que acontece, e não do que se imagina.
- **Matéria-prima**: pautas, histórias e trajetória do líder, cases (do mercado e próprios), banco de ideias, calendário, estratégia editorial já escrita.
- **Referências** (hooks, storytelling, formatos, retenção, benchmarks) e **inteligência** (tendências, estudos, imprensa).
- **Registro de números e fontes** (ver `registro-de-fontes.md`): **resolver aqui, antes das perguntas**: se existe, usar o nome e o local que o projeto já tem; se não, criar (projeto novo) ou montar com o usuário (projeto existente), e explicar em uma frase o que é e como atualizar.
- **Skills de apoio disponíveis** (retenção, psicologia, gancho, carrossel, SEO/GEO): ponteiros, não regras de marca (A.5).

### A.1 Perguntas (chat, ABCDE e escala)
1. Canais ativos hoje e canais que quer abrir (cada canal: objetivo, frequência real que consegue sustentar). **Perguntar também pelos canais emergentes e de reaproveitamento** (por exemplo X, Bluesky, Threads, Pinterest, Reddit): quais, e se o mesmo conteúdo vai para todos (adaptado por formato) ou se há canais com regra própria. Fundador solo: avisar o custo de sustentar muitos canais. **Plataformas sem skill de apoio** (as skills de redes do repositório não cobrem todas): as regras de canal vêm da busca de referências (A.3), não de improviso.
2. Séries recorrentes (rituais da essência viram séries). Nome, formato, cadência. **Série é recipiente que dá ritmo, não trava a criação**: prever uma categoria **Avulsa** para o que não cabe em série.
3. Matriz pilar x formato x canal: o usuário marca o que é principal, apoio, nunca (ou "todos em todos, para testar", e então registrar como o teste vai decidir).
4. O que nunca publicar (de "não comunicar" e dos limites de território).
5. Fluxo de aprovação: quem revisa, o que exige revisão jurídica, **se há revisão externa** (por peça, não por projeto) e em qual campo ela fica registrada.

### A.2 Matéria-prima (onde entram histórias, pautas e cases)
Perguntar o que o usuário já tem e **registrar o ponteiro, sem copiar**: histórias e trajetória do líder (só fatos já aprovados no projeto; o que falta vira "confirmar com o usuário"), pautas, cases do mercado (com fonte e grau de confiança) e cases próprios (com permissão). Esse material **alimenta as séries e os pilares**; não é série nem canal.

### A.3 Busca de referências (opcional, perguntar antes)
Objetivo: ver como perfis e marcas que o público segue fazem cada canal (formatos, ganchos, cadência, o que funciona e o que falha), para decidir regras de canal com base em exemplo, como na assessoria de imprensa (guias por veículo e por jornalista). **Perguntar** (regra 10): objetivo, opcional, escopo (quantos perfis por canal, quais canais), custo. Coleta: pesquisa na web e, quando passar de 10 páginas no mesmo lote, o Firecrawl local (protocolo ligar, verificar, usar, desligar). Saída: lista de referências por canal, com o que copiar de **estrutura** e o que **nunca** copiar (voz e marca de terceiros). Apoio: `conteudo-pesquisa`, `revenue-inteligencia-competitiva`, `conteudo-tendencias`.

### A.4 SEO e GEO (busca tradicional e busca por IA)
Perguntar se o conteúdo também precisa ser achado em buscadores e em respostas de IA. Se sim, registrar que canal e formato alimentam o quê **como hipótese a testar**, e ligar a `seo-conteudo`, `seo-palavras-chave` e `seo-geo` na hora de produzir. Não afirmar efeito de canal em SEO ou GEO sem fonte.

### A.5 Técnicas e táticas (retenção, psicologia, gancho)
Ficam nas **skills de apoio**, usadas na produção de cada peça: `copy-hooks-video-curto` e `video-hook-generator` (gancho), `revenue-psicologia`, `copy-conversao` e `copy-metodos-classicos` (persuasão), `social-carrossel`, `social-linkedin` e `social-estrategia` (canal), `conteudo-reaproveitamento` (reuso), `email-newsletter`. O arquivo de ativação só registra **o limite**: técnica nenhuma passa por cima da voz nem de "O que NÃO comunicar" (por exemplo, urgência falsa, promessa, pressão). O revisor de voz confere.

### A.6 Saída
Matriz, séries (e a categoria Avulsa), regras por canal (tamanho, abertura, chamada), lista "nunca publicar", fluxo de produção e aprovação (incluindo o campo de revisão externa, quando houver), checklist de revisão antes de postar (inclui `/ai-slop-detector`) e lacunas.

Para calendário, formatos e distribuição, usar `conteudo-estrategia` (`editorial-calendar`, `content-formats`, `distribution`); para regras por plataforma, `social-estrategia`, `social-linkedin` e `social-carrossel`. Aqui só se decide o que é da marca; o plano editorial é daquelas skills.

## B. Previsão de demanda (`ativacao/demanda.md`)

A skill não prevê números; ela organiza as **hipóteses e os sinais** para quem faz a previsão.

Perguntas:
1. Quando a necessidade aparece e quando some? (sazonalidade, prazos legais, ciclos de verba, datas, eventos do setor)
2. Que notícias ou acontecimentos aumentam a procura? Quais derrubam?
3. Que histórico existe? (vendas, buscas, tráfego, inscrições, por mês). Pedir arquivo ou período; sem dado, declarar.
4. Quais indicadores já acompanham, e onde ficam?
5. Que ações da marca alteram a demanda (lançamento, campanha, preço, parceria)?

Saída: calendário de gatilhos (data ou janela, tipo, efeito esperado, confiança), lista de eventos e notícias a vigiar, indicadores líderes e defasados, hipóteses a validar com dado, e uma tabela de cenários (base, alta, baixa) com o que mudaria em cada um. Qualquer número só aparece se vier do usuário ou de fonte citada; do contrário é hipótese rotulada.

Para achar sinais: `conteudo-tendencias` (tendências por fonte), `seo-palavras-chave` (sazonalidade de busca), `data-funil-e-coortes` (funil e coortes) e `data-atribuicao-e-relatorios` (resultado por canal). Para testar a previsão (e ampliar intervalos de quem está confiante demais), `revenue-premortem-previsao`.

## C. Monitoramento de mídia (`ativacao/monitoramento.md`)

Perguntas:
1. Nome da marca e todas as grafias, siglas e apelidos (inclui erros comuns de escrita).
2. Porta-vozes e pessoas ligadas (líder da essência).
3. Concorrentes e alternativas (do posicionamento).
4. Termos da categoria e da dor, com o vocabulário real das personas.
5. Palavras sagradas (a marca quer vê-las associadas a ela).
6. Termos de risco e de crise (temas sensíveis, acusações possíveis, o que seria um problema grave).
7. Veículos e comunidades que importam (das personas).
8. O que conta como menção positiva, neutra, negativa e crítica.
9. Quem decide e em quanto tempo responder a cada nível.

Onde fica `[ADR-001]`: as **regras** em `<raiz>/ativacao/monitoramento.md` (fonte da verdade); as **consultas, os termos e os relatórios** (só sob pedido) em `inteligencia/5_monitoramento/`, conforme o mapa de destinos. O Hub é só leitura; o Hub lê o `termos.txt` do projeto pelo argumento `--termos`. Veículos e jornalistas não são copiados.

**Termos em três arquivos de origem `[usuário, Futuro Mercado, 2026-10-23]`**, formato `termo|peso` (uma linha por termo): `termos-marca.txt` (nome, grafias, site, pessoas e vocabulário próprio; peso 3 para nome e pessoa, 1 a 2 para vocabulário), `termos-mercado.txt` (categoria, peso 2; assuntos associados, peso 1) e `termos-concorrentes.txt` (nomes, peso 2; pode ficar vazio, "a definir"). O `termos.txt` é a **junção** dos três (`cat termos-marca.txt termos-mercado.txt termos-concorrentes.txt > termos.txt`), é o único que o Hub lê e nunca se edita à mão. Palavra comum (ex.: "growth") traz ruído: peso mínimo e leitura com contexto.

Saída: lista de consultas prontas por grupo (marca, pessoas, concorrentes, categoria, risco), com operadores booleanos genéricos (E, OU, NÃO, aspas) que o usuário adapta à ferramenta que usa; classificação de sentimento com exemplos; níveis de alerta (informativo, atenção, crise) com gatilho, responsável e prazo; modelo de relatório periódico. Não citar ferramentas específicas como obrigatórias; perguntar qual usa.

Apoio: escuta social e consultas (`social-estrategia`, referência `social-listening`); monitor de concorrentes (`revenue-inteligencia-competitiva`, `competitor-monitor`); níveis de alerta, rota de escalonamento e declaração de contenção (`pr-assessoria-de-imprensa`, `crisis-detector` e `response-coordinator`); **consultas em IAs** (como as IAs citam a marca; ver `seo-geo`, `ai-citation-patterns` e `query-bank`). A skill `revenue-inteligencia-competitiva` tem ainda o `brand-monitor-api`, que usa o serviço Brand.dev e exige chave de API paga (`BRANDDEV_API_KEY`): **existe, mas não é recomendado por padrão**; só com decisão do usuário.

## D. Audiovisual (`ativacao/audiovisual.md`)

Perguntas:
1. Formatos dominantes (vertical curto, horizontal explicativo, entrevista, bastidor, motion graphics) e duração típica.
2. Quem aparece (líder, personagem, só voz, ninguém) e como se apresenta.
3. Voz de locução: ritmo, registro, pausas (da escala de voz).
4. Trilha e som: sem trilha, discreta, marcante; efeitos; silêncio como recurso.
5. Abertura e fechamento padrão (duração, o que aparece, chamada).
6. Legendas: posição, tipografia e cor (do design system), estilo de destaque de palavras.
7. Ritmo de edição: corte médio em segundos, uso de zoom, gráficos, texto em tela.
8. O que o vídeo nunca mostra ou diz (de "não comunicar" e da direção visual).

Saída: guia de fala (frases-modelo de abertura e de fechamento, ritmo), guia de imagem (enquadramento, luz, tratamento, proporção, safe areas), guia de edição (cortes, motion usando as curvas do design system), guia de som, checklist de aprovação de vídeo e ponteiros de produção.

Apoio: hooks dos 3 primeiros segundos (`copy-hooks-video-curto`), roteiro de vídeo de vendas (`copy-vsl`), direção de locução (`audiovisual-podcast-e-audio`, referência `voiceover-direction`), identidade sonora (`brand-identidade-sonora`), estilo para gerar imagem e carrossel (`visual-style.md` da marca, `social-direcao-de-arte-ia`, `audiovisual-imagem-flux-prompts`), regras visuais de marca em vídeo (`identidade-e-ativos/05-aplicacoes.md`, seção Audiovisual). **A produção programática** (edição, motion, avatar, geração de voz, renderização) vive no projeto *Edição de Vídeo com IA* (`Compartilhado/Edição de Vídeo com IA`); as skills `create-video`, `heygen`, `text-to-speech`, `elevenlabs`, `remotion` e `ffmpeg` foram removidas deste repositório. Ver `memory.md`.

## Aprovação

Cada arquivo é aprovado separadamente. Rodar `/ai-slop-detector` nos textos. Atualizar o estado em `00-intake.md`.
