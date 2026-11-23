> [!NOTE]
> **[EXEMPLO RESOLVIDO ILUSTRATIVO — USO COMO REFERÊNCIA DE PROCESSO]**
> Este documento integra o pacote de referências do Item 2042 da inbox. Apresenta um relatório de auditoria e conformidade visual para peças de rede social (Instagram Feed), validando medidas, proporções, hexadecimais de marca e zona segura (em conformidade com o `05a-moldes-de-canais.md` e a estrutura do `promovaweb/inboundfy`).

# Caso Resolvido: Auditoria de Conformidade Visual de Feed — Lúmina Gestão (Fictícia)

---

## 1. Especificação Técnica do Brief de Design (Instagram Feed)
- **Ativo:** Card Estático de Feed — "Demonstrativo de Retorno vs. Fatura Paga"
- **Formato Obrigatório:** Feed Retrato / Vertical 4:5 (1080 x 1350 px) para maior ocupação de tela no app mobile.
- **Paleta Obrigatória:** Azul Petróleo (`#0F3D4C`), Verde Menta (`#2ECC71`), Fundo Cinza Gelo (`#F7F9FA`) e Texto Grafite (`#1E293B`).
- **Restrições Visuais:** Proibido uso de gradientes roxo/neon; texto obrigatório dentro da zona segura (afastado 135 px do topo e do rodapé); proporção de texto não superior a 20% da área do card.

---

## 2. Candidato Visual Reprovado (Relatório da Rodada 1)

```markdown
# Relatório de Conformidade Visual — Instagram Card (Rodada 1)

- **Ativo:** Card Feed Instagram — `assets/lumina/cards/draft-card-glosas.png`
- **Validador:** `@brand-direcao-de-arte` (com skill `social-direcao-de-arte-ia`)
- **Data:** 2026-02-04
- **Veredito:** ❌ **REPROVADO POR NÃO CONFORMIDADE VISUAL E DE MARCA**

### Tabela de Achados Técnicos Visuais

| Parâmetro Técnico | Especificação do Brief | Evidência Medida no Arquivo | Regra / Diretriz Violada | Diagnóstico de Correção |
|---|---|---|---|---|
| **Dimensão e Aspect Ratio** | 1080 x 1350 px (4:5) | **1080 x 1080 px (1:1)** | `05a-moldes-de-canais.md` (Feed Retrato) | Card gerado no formato quadrado antigo, perdendo 30% de área de visualização no feed mobile. Refazer em 1080x1350 px. |
| **Paleta de Cores** | Primária `#0F3D4C` | **Fundo gradiente roxo (#6C5CE7 para #A29BFE)** | `brand-voice.md` e Guia de Cores da Lúmina | Cores completamente alheias à identidade da marca médica. Substituir por fundo `#F7F9FA` com acentos em `#0F3D4C`. |
| **Zona Segura (Margens)** | Mínimo 135 px de margem superior e inferior | **Título posicionado a 45 px do topo** | Especificação de interface do Instagram | O título do card será encoberto pelo cabeçalho do perfil do usuário no app móvel. Recuar para área segura. |
| **Legibilidade em Miniatura** | Contraste WCAG AA (mínimo 4.5:1) | **Texto cinza claro (#BDC3C7) sobre fundo branco (relação 1.8:1)** | Diretriz de Acessibilidade Visual | Contraste insuficiente. Ilegível na grade de fotos do perfil. Escurecer o texto para Grafite `#1E293B` (relação 10.5:1). |

### Encaminhamento
Devolver à fila de geração visual para ajuste de canvas (1080x1350 px), aplicação dos hexadecimais da marca e readequação de margens.
```

---

## 3. Relatório de Aprovação Final da Peça Ajustada (Rodada 2)

```markdown
# Relatório de Conformidade Visual — Instagram Card (Rodada 2)

- **Ativo:** Card Feed Instagram — `assets/lumina/cards/card-glosas-v2-final.png`
- **Validador:** `@brand-direcao-de-arte`
- **Data:** 2026-02-04
- **Veredito:** ✅ **APROVADO PARA PUBLICAÇÃO**

### Lista de Conferência Positiva (Hard Gate Visual)

- [x] **Dimensões e Proporção:** Exatamente 1080 x 1350 px (Aspect Ratio 4:5 vertical verificado).
- [x] **Cores da Marca:** Fundo sólido `#F7F9FA`, moldura de destaque em Azul Petróleo `#0F3D4C` e ícone de conciliação em Verde Menta `#2ECC71`.
- [x] **Sem Gradientes Não Autorizados:** Zero gradientes neon ou efeitos de sombra pesada.
- [x] **Zona Segura Respeitada:** Margem superior de 160 px e margem inferior de 180 px livres de texto e elementos vitais.
- [x] **Contraste e Legibilidade:** Relação de contraste de 11.2:1 (Grafite `#1E293B` sobre `#F7F9FA`), perfeitamente legível na miniatura da grade do Instagram.
- [x] **Tipografia Oficial:** Fonte limpa sem serifa, peso *Medium* para leitura ágil no celular.

### Liberação
Card aprovado e liberado para upload e agendamento no perfil oficial da Lúmina Gestão.
```
