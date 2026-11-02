# 6. Governança, auditoria e evolução da marca

**Fontes:** `brand-guidelines` (aprovação, violações e resolução), `brand-strategy-framework` (governança em 5 partes, auditoria por ponto de contato, métricas de saúde, rastreio, evolução), `branding-expert` (auditoria de marca, ponto de contato, atualizar x refazer), `assets` (governança de ativos). Reescrito e ampliado no E5.

> **O que este capítulo faz.** Mantém a marca **consistente depois que o brandbook existe**: quem decide, como se corrige o que sai fora da marca, como se versiona, como se audita e quando se atualiza ou se refaz. O inventário e a organização dos arquivos estão em `../../brandbook-e-ativos.md` (seção 6); aqui está a regra de funcionamento.

## 6.1 Papéis

| Papel | O que faz |
|---|---|
| **Dono da marca** | Decide em conflito, aprova mudanças no guia e é a última palavra |
| **Guardião do guia** | Mantém o arquivo vigente, responde dúvidas, recebe pedidos de exceção |
| **Aprovadores por tipo de peça** | Conferem peças conforme a tabela 6.2 |
| **Quem produz** | Usa o kit, o modelo e o checklist de peça (capítulo 5) |
| **Revisão automática de consistência** | Agente `brand-voice-guardian` confere voz e consistência de peças novas contra `_brands/<marca>/` |

Em marca pessoal ou time pequeno, uma pessoa acumula papéis; registrar quem.

## 6.2 Aprovação por tipo de peça (modelo)

| Tipo de peça | Aprovador | Prazo de resposta | O que exige revisão extra |
|---|---|---|---|
| Campanha grande, nova identidade, mudança de logo | Dono da marca | | Jurídico, quando houver marca registrada ou promessa |
| Conteúdo recorrente (posts, e-mails padrão) | Guardião do guia | | Texto passou pelo `/ai-slop-detector` |
| Peça de baixo risco com modelo pronto | Quem produz | — | Checklist de peça preenchido |
| Material impresso | Guardião + prova de cor da gráfica | | Prova física |
| Peça com imagem de pessoa | Guardião | | Autorização de imagem (capítulo 4) |

Prazos e nomes são do usuário. Sem preencher, fica lacuna declarada.

## 6.3 Violações e correção

Sinais de alerta: mensagem fora da voz; uso de logo não aprovado; paleta ou fonte errada; peça que contradiz "O que NÃO comunicar"; versão antiga do kit em circulação.

Resolução em 4 passos:
1. **Identificar** a peça e o ponto da regra violado.
2. **Documentar** (o que, onde, quem produziu, quando).
3. **Corrigir** imediatamente (tirar do ar, reimprimir se for o caso, avisar o produtor).
4. **Atualizar o guia** se a violação mostrou ambiguidade na regra. Violação repetida em uma regra costuma ser regra mal escrita.

## 6.4 Controle de versão e distribuição

- **Um único arquivo vigente** do guia e do kit; os anteriores ficam preservados, com versão e data. Versão nova é arquivo novo `-vN`; **não editar a anterior no lugar** (regra do projeto para documentos de marca).
- Registrar no topo do guia: versão, data, o que mudou e quem aprovou.
- **Onde mora o kit:** um lugar só, com acesso definido (quem baixa, quem altera). Pasta compartilhada ou repositório; arquivos finais separados dos editáveis.
- **Quem recebe o guia** quando muda: lista de distribuição (time, agências, fornecedores) e como são avisados.
- **Treinamento:** quem entra no time recebe o guia e o checklist de peça no primeiro dia.

## 6.5 Auditoria de marca

Rodar em momentos fixos (por exemplo semestral, antes de campanha grande, depois de fusão ou mudança de público). Cada área recebe uma pergunta e uma evidência.

| Área | Pergunta | Evidência |
|---|---|---|
| **Consistência** | Tem a mesma cara em todos os lugares? | Amostra de peças por ponto de contato lado a lado |
| **Clareza** | A proposta de valor é clara em 5 segundos? | Teste com alguém de fora; primeira dobra do site |
| **Diferenciação** | Destaca-se dos concorrentes? | Comparação com o mapa de concorrentes da etapa 2 |
| **Relevância** | Ressoa com o público atual? | Comentários, vendas, pesquisa; personas ainda valem |
| **Autenticidade** | A marca cumpre o que promete? | Avaliações, atendimento, entregas |

**Revisão por ponto de contato:** site (visual, voz, experiência) · redes (perfil, conteúdo, engajamento) · e-mail (design, tom, assinaturas) · produto e embalagem · atendimento (roteiros e respostas) · publicidade · material de vendas · interface do produto. Para cada ponto, abrir uma peça real e conferir o checklist do capítulo 5.

Cada achado leva **evidência** (arquivo, link, captura) e um dono para corrigir.

## 6.6 Saúde da marca (opcional, só com dado)

Métricas que organizam o acompanhamento. **Números só entram com fonte; sem medição, a linha fica vazia.**

| Pergunta | Como medir | Onde ligar |
|---|---|---|
| Reconhecimento | Pesquisa de lembrança espontânea e assistida | Pesquisa própria ou contratada |
| Percepção | Análise de sentimento, NPS | `data-atribuicao-e-relatorios`, monitoramento (etapa 8, C) |
| Preferência | Pesquisa de consideração | Pesquisa própria |
| Lealdade | Recompra, retenção | `growth-retencao-e-churn`, `data-funil-e-coortes` |
| Participação de voz | Menções vs concorrentes | Escuta social (`social-estrategia`) |

Rastreio (modelo; as ferramentas são exemplos, usar a que o time já tem):

| Métrica | Ferramenta (exemplo) | Frequência sugerida |
|---|---|---|
| Menções | Escuta social | Semanal |
| Sentimento | Brandwatch, Sprout ou equivalente | Mensal |
| Volume de busca pelo nome | Google Trends | Mensal |
| Tráfego direto | GA4 | Semanal |
| Tráfego de indicação | GA4 | Semanal |
| NPS | Ferramenta de pesquisa | Trimestral |

Definir só o que o time de fato vai olhar, com dono e periodicidade. Frequência é sugestão do guia original, não regra.

## 6.7 Atualizar ou refazer

| Sinal | Ação | Tipo |
|---|---|---|
| Visual datado | Atualização visual | **Atualizar** |
| Inconsistência entre peças | Reforçar o guia e a governança | **Atualizar** |
| Público novo | Evoluir a voz e as mensagens | **Atualizar** |
| Fusão ou aquisição | Nova identidade | **Refazer** |
| Mudança de rumo do negócio | Revisão completa | **Refazer** |
| Crise de reputação | Recomeço, com cuidado e jurídico | **Refazer** |
| Mudança fundamental de posicionamento | Novo posicionamento | **Refazer** |

| Atualizar | Refazer |
|---|---|
| Evolui elementos existentes | Reformula tudo |
| Mantém o reconhecimento | Nova identidade |
| Moderniza a aparência | Novo posicionamento |
| Risco menor, execução mais rápida | Risco maior, prazo maior |

**Dentro do `brand-builder`:** atualizar é modo **estender** (nova versão `-vN` dos arquivos afetados); refazer é modo **refazer** (recomeço, o anterior preservado). Marca com nome novo passa de novo pelo `brand-naming`. A comparação com a essência fica em `brand-essence`.

## 6.8 Registro de decisões

Manter uma lista curta no fim do guia: data, decisão, motivo, quem decidiu, exceções concedidas. Exceção sem prazo vira regra; por isso toda exceção tem data de revisão.

## 6.9 Saída deste capítulo

Seção "Governança" do `identidade-e-ativos.md`:

```
## Governança
Papéis (6.1) / Aprovação por tipo de peça (6.2) / Violações e correção (6.3)
Versão e distribuição (6.4) / Auditoria: calendário e responsável (6.5) / Saúde da marca (6.6, se houver dado)
Critérios para atualizar ou refazer (6.7) / Registro de decisões (6.8)
```

## Checklist

- [ ] Dono da marca e guardião do guia nomeados
- [ ] Tabela de aprovação preenchida ou lacuna declarada
- [ ] Processo de correção de violação definido
- [ ] Guia com versão, data e histórico; arquivo vigente único
- [ ] Local do kit e lista de distribuição definidos
- [ ] Calendário de auditoria e dono
- [ ] Critérios de atualizar x refazer registrados
- [ ] Nenhum número de saúde da marca sem fonte
