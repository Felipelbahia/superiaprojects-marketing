# Guia de identidade e ativos da marca

Guia operacional da parte **visual e material** de uma marca: como o logo é usado, como a cor é especificada para tela e para impressão, como a tipografia e a imagem são aplicadas, onde a marca aparece e quem aprova o quê. Complementa a etapa 6 (direção visual: *o que* a marca deve parecer) e a etapa 7 (design system: *tokens e componentes* para tela). Este guia cobre o que essas duas etapas não cobrem: **regras de uso**, **especificação para impressão e arquivos**, **aplicações**, **governança** e **auditoria**.

Use quando o usuário pedir brandbook Recomendado ou Completo (ver `../../brandbook-e-ativos.md`), quando a marca tiver logo mas nenhuma regra de uso, quando for preciso entregar arquivos a uma gráfica ou agência, ou quando houver peças fora da marca circulando.

**Não use** para decidir o estilo visual (use `brand-visual-direction`), para gerar tokens, site de referência e `DESIGN.md` (use `brand-design-system`) nem para criar o logo (nenhuma skill do repositório desenha logo; este guia diz como **briefar** quem desenha).

## Capítulos

| # | Arquivo | Assunto | Estado |
|---|---|---|---|
| 1 | [01-logo.md](01-logo.md) | Versões, área de respiro, tamanho mínimo, fundos, o que não fazer, kit de arquivos, briefing de logo | escrito |
| 2 | [02-cor.md](02-cor.md) | Papéis de cor, especificação para tela e para impressão (RGB, CMYK, Pantone), versões do logo em cor, acessibilidade, psicologia das cores como hipótese | escrito |
| 3 | [03-tipografia.md](03-tipografia.md) | Famílias, hierarquia, licença, substituição, uso em tela e impressão | escrito |
| 4 | [04-imagem.md](04-imagem.md) | Fotografia, ilustração, ícones, padrões, tratamento, o que nunca mostrar | escrito |
| 5 | [05-aplicacoes.md](05-aplicacoes.md) | Digital (site, e-mail, redes, anúncios), impressos, apresentações, embalagem, vídeo | escrito |
| 6 | [06-governanca-e-auditoria.md](06-governanca-e-auditoria.md) | Quem aprova, violações, controle de versão, auditoria de pontos de contato, atualizar x refazer a marca | escrito |

## Como este guia se encaixa no fluxo

```
6 Direção visual ─► 7 Design system (tokens, site, DESIGN.md, visual-style.md)
                         │
                         ▼
        Guia de identidade e ativos (este)  ─► 8 Ativação ─► 9 Brandbook (índice)
```

- **Entrada:** `06-direcao-visual.md`, `design-system/tokens.json` e `DESIGN.md` aprovados, `style-guide.md` existente (vence em conflito), logo e arquivos que o usuário já tem.
- **Saída proposta:** `_brands/<marca>/identidade-e-ativos.md`, com as regras decididas, que o `brandbook.md` linka. Nome de arquivo a confirmar com o usuário na hora de usar (entra no `catalog.md` quando o guia for ligado ao fluxo).
- **Valores de tela** (hex, contraste, claro e escuro) vivem no `tokens.json`; este guia **referencia** esses valores e não os redigita. **Valores de impressão** (CMYK, Pantone) e **regras de uso do logo** nascem aqui.
- Regras do `brand-builder` valem aqui: estender o que existe (o `style-guide.md` manda), tags de proveniência, nada inventado quando o usuário pode decidir, texto final pelo `/ai-slop-detector`.

## Princípio

Uma marca forte se constrói por consistência; todo ponto de contato deve parecer vindo da mesma fonte. Regra sem exemplo é regra que ninguém aplica: cada capítulo pede um "pode" e um "não pode" visual para cada decisão.

## Fontes e direito de uso

Fusão feita no E5 (2026-10-20), em português, com direito de uso confirmado pelo usuário. Cada capítulo anota de onde veio cada trecho.

| Fonte | Onde está | Contribuição |
|---|---|---|
| `brand-guidelines` (AgentKits) | `.agent/skills/_arquivo/mescladas/e5-brand/brand-essence/brand-guidelines.md` | Esqueleto do documento: logo, cor com RGB, tipografia, imagem, aplicações, governança, violações |
| `branding-expert` | `.agent/skills/_arquivo/mescladas/e5-brand/brand-essence/branding-expert.md` | Seções do documento de diretrizes, guia de logo, sistema de cor, revisão de pontos de contato |
| `visual-identity` (arquivado) | `.agent/skills/_arquivo/mescladas/r13-cro/ui-ux-conversion-designer/visual-identity.md` | Versões do logo, regras de uso, tabela de cor com CMYK e Pantone, hierarquia tipográfica, estilo de imagem, elementos de design |
| `brand-strategy-framework` | `.agent/skills/_arquivo/mescladas/e5-brand/brand-essence/brand-strategy-framework.md` | Elementos visuais, psicologia das cores, auditoria de pontos de contato, governança |
| `book` e `assets` (AgentKits) | `revenue-gtm-e-posicionamento/references/` (adaptados em `../../brandbook-e-ativos.md`) | Escopos e inventário de ativos |
| Exemplos de guia aplicado | `brand-voice-messaging/references/agentkits-brand-voice-guidelines.md` (seção 8) e `brand-builder/references/brand-guidelines-anthropic.md` | Como um guia real fixa tamanho mínimo, área de respiro, cores e fontes com fallback |
