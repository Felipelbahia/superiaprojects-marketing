# 5. Aplicações: onde a marca aparece e como

**Fontes:** `brand-guidelines` (tabelas de aplicações digitais e impressas com especificação e local do modelo), `branding-expert` (revisão por ponto de contato; seção "Applications" do documento de diretrizes), `book` (aplicações: formatos digitais, impressos, redes sociais, apresentações), `brand-strategy-framework` (checklist de pontos de contato). Reescrito e ampliado no E5.

> **O que este capítulo faz.** Transforma as regras dos capítulos 1 a 4 (logo, cor, tipografia, imagem) em **regras por peça**: para cada lugar onde a marca aparece, qual versão do logo, quais cores, qual fonte, qual modelo e quem aprova. **Não** cria o conteúdo das peças (isso é o fluxo normal do 0 Mkt) e **não** replica a ativação da etapa 8 (que define voz, ritmo, formato e canais). Aqui o assunto é **aparência e arquivo**.

## 5.1 Como decidir quais aplicações entram

1. Ler `00-intake.md` (usos prioritários) e `ativacao/*` (canais ativos).
2. Listar só os pontos de contato **reais** da marca hoje e os que ela abrirá em até 6 meses. Aplicação sem uso previsto é peso morto no guia.
3. Para cada um, preencher a ficha da seção 5.2. Se não dá para preencher, vira lacuna.

## 5.2 Ficha de aplicação (modelo)

| Campo | O que registrar |
|---|---|
| **Peça / ponto de contato** | Nome e onde aparece |
| **Logo** | Qual versão (principal, símbolo, monocromática, reversa) e onde fica |
| **Cor** | Fundo, texto, destaque (nomes da ficha de cor, não códigos soltos) |
| **Fonte** | Papel (display, corpo) e a fonte substituta, se o canal não aceita a da marca |
| **Imagem** | Estilo permitido e proporção |
| **Especificação técnica** | Formato, tamanho, resolução, perfil de cor, margem e sangria, conforme o fornecedor ou a plataforma |
| **Modelo** | Onde está o arquivo-base e em que programa |
| **Dono e aprovação** | Quem produz, quem aprova, prazo (capítulo 6) |
| **Exemplo** | Uma peça aprovada como referência |

**Medidas técnicas nunca são inventadas aqui.** Tamanhos, resoluções e margens variam por plataforma e por gráfica e mudam com o tempo: registrar o valor **confirmado na hora** com a fonte (documentação da plataforma ou orçamento da gráfica) e a data da conferência.

## 5.3 Digital

| Aplicação | Pontos de atenção | Onde se liga |
|---|---|---|
| **Site e landing pages** | Cabeçalho com logo principal; favicon do símbolo; tokens do design system; modo claro e escuro | `brand-design-system`, agente `site-construcao-web` |
| **E-mail (marketing e transacional)** | Cabeçalho e rodapé; pilha de sistema aprovada (clientes de e-mail ignoram fonte própria); versão do logo legível em fundo escuro do cliente de e-mail; assinatura padrão | `email-copy`, `email-newsletter`, `email-entregabilidade` |
| **Redes sociais** | Avatar com o símbolo; capa; destaques; modelos de post e de carrossel; zona segura; tratamento de imagem | `social-carrossel`, `social-direcao-de-arte-ia`, `social-linkedin` |
| **Anúncios** | Logo pequeno e legível; texto sobre imagem com contraste; zona segura por posicionamento; variações por formato | `ads-criativos`, `ads-multiplataforma/references/platform-specs.md` |
| **Apresentações** | Mestre de slides com logo, fontes e cores; fonte substituta se o arquivo circular fora; versão em PDF | `audiovisual-pitch-deck`, `audiovisual-slidev` |
| **Documentos e propostas** | Cabeçalho, rodapé, estilos de título e de corpo; PDF final | `vendas-materiais-de-venda` |
| **Aplicativo / produto** | Ícone do app, tela de abertura, interface com os tokens | `brand-design-system`, `site-tailwind-design-system` |

### 5.3.1 Assinatura de e-mail: dois formatos `[usuário, 2026-10-23, projeto Futuro Mercado]`

Oferecer **sempre dois formatos** e deixar o usuário escolher:

| Formato | Estrutura |
|---|---|
| **Coluna única** | Logo (versão horizontal) no topo; nome; cargo; contatos; redes sociais; frase da marca em linha pequena no fim |
| **Duas colunas** | **Esquerda:** logo (versão principal) e **frase da marca (slogan)**, ocupando cerca de **1/5 da largura** (proporção aproximada, não rígida). **Direita:** nome, abaixo o cargo, abaixo os contatos, abaixo as redes sociais |

Regras que valem para os dois:
- **Redes sociais como ícone com link** para o perfil (a logo da rede, com o endereço do perfil), em vez do endereço escrito.
- **Contatos:** site, e-mail, telefone ou WhatsApp com link (`mailto:`, `wa.me`).
- **Texto da assinatura vem de uma decisão aprovada, nunca inventado.** O "slogan" é a **frase da marca** (a promessa aprovada no posicionamento), **não** o descritor da empresa ("o que ela é"); o descritor é vago como assinatura. Se não houver frase aprovada, perguntar antes de preencher. Nome, cargo e contatos vêm do usuário; o que não foi informado vira "exemplo a confirmar".
- **Fonte de sistema** (clientes de e-mail ignoram fonte própria) e **tabela com estilos em linha**, não CSS externo.
- **Imagens precisam de endereço público** (ou do envio de imagem do próprio programa de e-mail): imagem local não aparece para quem recebe. Entregar uma versão de prévia (imagens locais) e uma versão para colar (endereço a definir), dizendo isso.
- Ícones de redes sociais: glifos simples na cor de tinta da marca, ou as versões oficiais conforme as regras de uso de marca de cada rede; avisar qual foi usada.

## 5.4 Impresso e físico

| Aplicação | Pontos de atenção |
|---|---|
| **Papelaria (cartão, papel timbrado, envelope)** | Logo vetorial; CMYK ou Pantone confirmados (capítulo 2); margens de segurança e sangria da gráfica |
| **Cartão de visita: o que entra** | **Identidade e contato**: logo, nome, cargo, contatos, frase da marca (aprovada). **Não** colocar nome de método, de oferta ou rótulos decorativos (siglas internas, etiquetas) que o cliente não conhece: não são identidade e não fazem sentido para quem recebe o cartão. Frente: logo; verso: nome, cargo, contatos |
| **Folhetos, catálogos, relatórios** | Hierarquia tipográfica; imagem em resolução de impressão; perfil de cor da gráfica |
| **Embalagem e rótulo** | Pantone quando a cor precisa ser idêntica entre lotes; textos legais; materiais e acabamentos; prova física antes da tiragem |
| **Sinalização e fachada** | Versão de logo para distância; contraste com o fundo físico; vetorial e escala |
| **Brindes e uniformes** | Versão monocromática ou de uma cor; técnica de aplicação (bordado, silk) limita detalhes |
| **Eventos e estandes** | Mesmo kit; tamanhos grandes exigem arquivo vetorial |

Para qualquer impresso, a **prova de cor** com o fornecedor é parte da aprovação.

## 5.5 Audiovisual

Aqui entram só as **regras de marca na imagem**; ritmo, locução, trilha e edição estão em `ativacao/audiovisual.md` (etapa 8).

- Abertura e fechamento padrão: versão do logo, duração, fundo.
- Legendas: posição, fonte, cor e estilo de destaque, vindos do design system.
- Barras e títulos na tela: fonte e cor; zona segura para cortes de plataforma.
- Identidade sonora: `brand-identidade-sonora`.
- Produção programática (motion, edição, avatar, voz): projeto *Edição de Vídeo com IA*.

## 5.6 Checklist de peça (antes de publicar ou imprimir)

- [ ] Versão correta do logo, com área de respiro e tamanho mínimo
- [ ] Cores da ficha de cor; contraste conferido
- [ ] Fontes da marca ou a substituta aprovada
- [ ] Imagem dentro do estilo, com direito de uso e autorização
- [ ] Texto passou pelo `/ai-slop-detector` e respeita "O que NÃO comunicar"
- [ ] Especificação técnica confirmada com o fornecedor ou a plataforma
- [ ] Aprovação conforme a tabela do capítulo 6

## 5.7 Saída deste capítulo

Seção "Aplicações" do `identidade-e-ativos.md`: uma ficha por ponto de contato real (5.2), agrupadas em digital, impresso e audiovisual, mais a lista de lacunas (aplicação prevista sem modelo ou sem especificação confirmada).
