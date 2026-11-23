# 11 — Calibração da régua (v1)

Objetivo: o dono do método ensina a skill a reconhecer cada item e cada grau, com peças reais. A régua evolui por correções, sem apagar o histórico.

## Estado atual
- Versão da régua em vigor: **v1** (escala 0–4 provisória, `[derivado]`).
- Casos de calibração registrados: **0**.

## Como funciona
1. A skill audita uma peça (A1).
2. O usuário corrige o que discorda: grau, polaridade, item ou evidência.
3. A skill propõe a **regra aprendida** em uma frase e pede confirmação.
4. Confirmada, registra em um arquivo de calibração e atualiza o `CHANGELOG.md`.

## Regras de versionamento (regra do usuário)
- Nunca editar uma versão anterior. Mudança de régua = novo arquivo `11-calibracao-vN.md` (`v2`, `v3`…), que copia o anterior e acrescenta.
- Entradas dentro da versão atual só se acrescentam (append), nunca se reescrevem.
- O `CHANGELOG.md` diz qual versão está em vigor; a `SKILL.md` aponta para ela.

## Formato do caso

```markdown
### Caso <nº> — <data> — <peça / marca / meio>
- Peça (trecho ou link):
- Item(ns) em discussão:
- Minha nota (grau/polaridade) e evidência:
- Nota do usuário (grau/polaridade) e justificativa:
- Regra aprendida (1 frase):
- Efeito: ajusta âncora de grau · muda definição de item · muda mapa de encaixe · sem efeito geral
- Status: proposta · aceita · rejeitada
```

## Âncoras que a calibração deve refinar primeiro
1. Diferença entre grau 2 (presente) e 3 (forte).
2. Quando um item é secundário versus apenas insinuado.
3. Polaridade `−` (eletrificação negativa) em peças de produto.
4. Itens fáceis de confundir (ver `05-matriz-de-combinacoes.md`).

## Casos registrados
_(nenhum ainda)_
