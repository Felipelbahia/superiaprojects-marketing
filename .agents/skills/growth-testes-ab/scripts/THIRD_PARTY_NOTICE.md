Scripts copiados do pacote npm `@clawfu/mcp-skills` 0.4.0 (autor: ClawFu, licença MIT), com três correções feitas em 2026-10-20 a pedido do usuário (ver abaixo). Instalação autorizada pelo usuário em 2026-10-20 (regra 1.5 do CLAUDE.md). Resultado dos testes e limites conhecidos: seção "Scripts de cálculo" do SKILL.md desta skill.

Alteração: `ab_test_stats.py` passou a calcular o z de confiança e o z de poder com `statistics.NormalDist` (antes usava uma tabela fixa e o z errado para o poder).
