---
name: brand-visual-direction
description: "Use para decidir direção visual, mood, estilo de imagem, intenção de cor e tipografia e visual de vídeo antes do design system (etapa 6 do brand-builder). Gatilhos: \"direção visual\", \"moodboard\", \"como a marca deve parecer\", \"tendências visuais\". NÃO use para gerar tokens e componentes (use brand-design-system), extrair ou aplicar um visual-style.md (use brand-visual-style) nem para conceito de anúncio (use ads-criativos)."
license: MIT
metadata:
  author: Felipe Bahia (Futuro Mercado)
  version: 1.0.0
---

# Brand Visual Direction

## Overview

Etapa 6 do `brand-builder`. Converte essência, posicionamento, voz e desejo em uma **direção visual aprovada em palavras e referências**, antes de qualquer código. O resultado é o briefing que o `brand-design-system` (etapa 7) executa e que a equipe audiovisual usa para fotografia, motion e vídeo.

**Princípio central: o visual traduz a essência; estética sem razão rastreável é decoração.**

## Antes de começar

1. Etapas 1, 2, 4 aprovadas (3 e 5 desejáveis). Ler também o `style-guide.md` existente.
2. **Marca com identidade visual existente** (paleta, fontes, logo): isso é base e vence. A direção estende, nunca substitui. Conflito vai para Known Gaps.
3. Ler `../brand-builder/question-formats.md`.
4. Aceitar anexos opcionais: logo, prints do produto ou do site, imagens-modelo do estilo desejado.

## Fluxo

| Passo | O que faz | Referência |
|---|---|---|
| 1 | Derivar sensação (3 palavras) e "não deve parecer" da essência, voz e "não comunicar" | `references/roteiro-visual.md`, rodada 1 |
| 2 | Reação a famílias visuais (amo/aceito/evito/nunca) | rodada 2 e `references/familias-visuais.md` |
| 3 | Escalas visuais (denso x arejado, quente x frio, etc.) e, ao propor cor ou fonte, **HTML de amostra** (regra 8) | rodada 3 |
| 4 | Imagem, ilustração, movimento e som | rodada 4 |
| 5 | Redigir `06-direcao-visual.md`, descrever o moodboard em palavras | template abaixo |
| 6 | Aprovação do usuário **antes** de seguir para a etapa 7 | |

Curta: passos 1, 2, 3 e 6. **Obrigatório no modo curto:**
- Perguntar explicitamente se o usuário quer opinar ou sugerir cores (paleta, temperatura, saturação).
- Perguntar sobre a logo (se já existe arquivo/vetor, ou que estilo prefere: símbolo + tipografia, monograma, abstrato).
- Gerar no HTML de amostra a **primeira quebra de página do site (Hero Section / Acima da Dobra completo)** com nav, headline, sub, CTA e visual renderizado.
- Registrar proibições estritas de Anti-Site de IA (Anti-Purple Ban, Anti-3D Slop, sem ilustrações genéricas).
Longa: todos, com anexos analisados e extração via skill `brand-visual-style` (modo Extract) quando houver site, vídeo ou PDF de referência.

## Regras

1. Cada decisão visual cita a decisão de origem: "palavra X da essência -> escolha Y".
2. **Reações a referências** usam famílias de estilo e exemplos que eu realmente conheço. Quando houver web, confirmar antes de citar marca ou peça específica.
3. Sem anexos, não inventar "estilos de imagem". Descrever direção em palavras e marcar a seção de imagens como a confirmar.
4. Gradiente só se o `style-guide.md` da marca já usa. Sem emoji em artefatos de design.
5. Registrar o que a marca **não** pode parecer (ex.: "startup genérica") e uma consequência visual concreta para cada item.
6. Acessibilidade entra desde aqui: preferir pares de cor que atendam contraste, e dizer quando uma cor de marca precisará de variante para texto.
7. Direção de movimento e som é parte da saída (vídeo e áudio dependem dela).
8. **Cor, fonte e afins se mostram, não só se descrevem.** Sempre que eu propuser paleta, tipografia, ícone ou estilo, gero um **HTML de amostra** autocontido em `<raiz da marca>/_respostas/amostras-visuais-vN.html` e entrego o caminho para o usuário abrir (decisão do usuário, 2026-10-22). A amostra traz, por direção proposta: paleta com hex, papel e **contraste calculado**, tipografia (título, corpo, rótulo) com texto em português acentuado, 2 ou 3 candidatos de ícone ou seta, e aplicações reais (topo de página, capa e lâmina 2 de carrossel em 4:5, cartão de dados). **Cada fonte vem identificada no próprio HTML** (decisão do usuário, 2026-10-22): uma tabela "Fontes" no topo (nome, peso e estilo, papel: título, palavra-chave, corpo, rótulo, número, logotipo) e uma legenda curta sob cada aplicação dizendo qual fonte está em cada elemento. **Nenhum dado real inventado:** número ilustrativo vem marcado "exemplo de layout". Fonte externa só como Google Fonts opcional, com fonte de sistema de reserva. Conferir a amostra aberta num navegador antes de entregar. Nova rodada de ajuste = `amostras-visuais-v(N+1).html`, sem editar a anterior.

9. **Ao fechar, entregar também o HTML.** Gerar `06-direcao-visual.html` ao lado do `.md` (decisão do usuário, 2026-10-22): paleta com hex e contraste calculado, tipografia com o nome de cada fonte e exemplo, logo no claro e no escuro, regras de destaque e movimento, e as aplicações aprovadas. O `.md` é a fonte; o HTML é a leitura visual. Conferir aberto num navegador antes de entregar.

## Saída: `06-direcao-visual.md` e `06-direcao-visual.html`

```
# Direção visual - <Marca>
Estado: rascunho | aprovado em AAAA-MM-DD
## Sensação (3 palavras) e "não deve parecer"
## Origem das decisões (tabela decisão -> essência/voz)
## Cor: intenção, temperatura, contraste, cores já existentes
## Tipografia: caráter, o que evitar, fontes já existentes
## Forma e espaço: densidade, cantos, grade, ritmo
## Imagem: fotografia, ilustração, tratamento, o que nunca mostrar
## Movimento: velocidade, curva, o que anima e o que não
## Som: voz de locução, trilha, silêncio, efeitos
## Referências aprovadas e rejeitadas (com o porquê)
## Anexos recebidos e como foram usados
## Lacunas
```

## Erros comuns

| Erro | Correção |
|---|---|
| Pular para paleta e fonte | Sensação e origem das decisões vêm primeiro |
| "Moderno, clean, minimalista" | Exigir contraste concreto com o "não deve parecer" |
| Pegar referências só que o usuário admira | Incluir exemplos que ele deve rejeitar e extrair o padrão |
| Ignorar o style-guide existente | Ele manda; estender |
| Esquecer movimento e som | Audiovisual depende disso |

## Referências Detalhadas

- [references/roteiro-visual.md](references/roteiro-visual.md): rodadas de perguntas da direção visual
- [references/familias-visuais.md](references/familias-visuais.md): 12 famílias visuais para o usuário reagir
- [references/design-trends-2026.md](references/design-trends-2026.md): as 10 tendências de design gráfico de 2026 (mais 2 menções) em vocabulário de estilo preciso, com prompts de IA; usar no passo 2 (reação a famílias) e para briefar designer ou gerador de imagem. Fonte: Kittl × Savee, jan. 2026; imagens do relatório não incluídas
