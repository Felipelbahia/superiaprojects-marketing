# Exemplo: auditoria boa contra auditoria ruim

> Condensado, na R16b, de quatro arquivos do autor original (incidente, caso de sucesso, exemplo bom, exemplo ruim; em `.agent/skills/_arquivo/mescladas/r16b-design/ui-ux-audit/`). Os dados do projeto original foram trocados por um caso neutro: **página inicial de um site de consultoria**. Pedido do usuário: "melhore a página inicial".

## Auditoria ruim (o que NÃO fazer)

Resposta imediata, sem abrir nenhum arquivo:

> "Recomendo adicionar: 1. gráfico animado com os resultados da empresa; 2. cartão grande do assistente de IA no hero; 3. depoimentos em carrossel com vídeo; 4. painel de métricas; 5. linha do tempo da empresa."

Por que é ruim:

- **Não leu o estado atual.** Nenhum arquivo, nenhum trecho de código como prova.
- **Não checou redundância.** Os resultados da empresa já aparecem em três cartões de números; o assistente já existe como botão no canto; os depoimentos já estão na página; a lista de serviços já tem prévia com link.
- **Ignorou a filosofia da página** (minimalista, escaneável): mais itens não é melhor, e o cartão do assistente esconderia os CTAs principais.
- **Sem prioridade nem esforço.** Cinco itens soltos; o usuário não sabe por onde começar.
- **Consequência real que motivou a skill:** o usuário vê tudo implementado, percebe a duplicação, **reverte** e perde horas.

## Auditoria boa (o que fazer)

1. **Ler primeiro** (`page.tsx`, componentes da seção, arquivo de conteúdo) e dizer quais arquivos foram lidos.
2. **Inventário do que existe, com prova** (arquivo e linhas):

   | Componente | Onde | O que mostra |
   |---|---|---|
   | Hero | `page.tsx:15-45` | Nome, promessa, 3 CTAs (Ver trabalhos, Ver serviços, Falar comigo) |
   | Cartões de números | `page.tsx:47-80` | Resultados e tempo de mercado |
   | Depoimentos | `page.tsx:105-140` | 3 citações com nome, cargo e empresa |
   | Prévia de serviços | `page.tsx:82-103` | 3 categorias com link para a página completa |

3. **Inventário de dados repetidos** (cada dado aparece uma vez?):

   | Dado | Local 1 | Local 2 | Redundante? |
   |---|---|---|---|
   | Resultados da empresa | Cartões de números | - | Não |
   | CTA "Falar comigo" | Hero | - | Não |

4. **Lacunas reais, com prova e solução mínima** (só o que o código mostra que **não existe**):
   - **P1:** nenhum CTA depois dos depoimentos (a seção termina na linha 140 e vem o rodapé). Solução: um botão "Vamos conversar" para o contato. Esforço: 30 min.
   - **P2:** ícone do menu no celular menor que 44 px (`Header.tsx:25`). Solução: 48 px. Esforço: 15 min.
   - **P3:** sem link "pular para o conteúdo" (acessibilidade). Solução: link visualmente oculto. Esforço: 20 min.

5. **"Não recomendado, porque duplica":** gráfico de resultados (já há cartões), cartão grande do assistente (esconde os CTAs), painel de métricas (a página é minimalista).
6. **Checagem de filosofia:** simples e escaneável; espaço em branco; cada informação aparece **uma vez**; nada de volume sem necessidade. Responder às perguntas: isso **soma valor ou só volume**? é a solução **mais simples**? sobreviveria à revisão do usuário?
7. **Recomendação** com próximos passos: aprovação do usuário → implementar P1, P2, P3 um a um → testar a cada mudança.

Resultado esperado: o usuário aprova a recomendação sem reverter nada, porque cada item tem prova e nenhum duplica o que existe.

## Lista de verificação antes de entregar a auditoria

- [ ] Li os arquivos da página e dos componentes **antes** de recomendar?
- [ ] Documentei o que **existe**, e não o que presumi que falta?
- [ ] Chequei redundância de forma sistemática (dado por dado)?
- [ ] Cada lacuna tem prova no código e solução mínima?
- [ ] A recomendação respeita o desenho limpo e é a mais simples?
- [ ] Sobreviveria à revisão do usuário?

Se alguma resposta for "não", **pare e refaça**.
