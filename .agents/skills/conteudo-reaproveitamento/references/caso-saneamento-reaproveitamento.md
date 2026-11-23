> [!NOTE]
> **[EXEMPLO RESOLVIDO ILUSTRATIVO — USO COMO REFERÊNCIA DE PROCESSO]**
> Este documento integra o pacote de referências do Item 2042 da inbox. Demonstra o fluxo completo de preservação da fonte bruta, relatório de saneamento em 3 blocos (*corrigido*, *preservado*, *pendências*), base limpa em blocos e plano de oportunidades com matriz de reaproveitamento e corte justificado (baseado na estrutura do `promovaweb/inboundfy`).

# Caso Resolvido: Saneamento de Material Bruto e Acervo de Conteúdo — Lúmina Gestão (Fictícia)

---

## 1. Material Original Bruto (Transcrição Intacta de Reunião de Produto)

> [!IMPORTANT]
> **REGRA DE OURO:** O material bruto abaixo é preservado rigorosamente intacto, sem nenhuma edição posterior. Representa as notas e transcrição rápida de uma reunião interna entre o fundador da Lúmina e a liderança de suporte médico.

```text
[Transcrição Reunião Interna - 15/01/2026 - Áudio 18min]
Participantes: Dr. Renato (Fundador) e Mariana (Líder de Suporte a Clínicas)

Renato: ...então Mariana o que a gente viu semana passada naquela clínica lá de Campinas é surreal... a médica achava que tava lucrando horrores porque a agenda tava lotada né... mas aí quando a gente rodou o nosso script de conciliação bancária bateu um susto... tinha quase quarenta mil reais de guias paradas na Unimed que ela nem sabia que não tinham sido pagas...
Mariana: É exatamente isso Renato, o pessoal da recepção digita a matrícula no sistema antigo deles, aí o convênio cospe uma glosa técnica lá no demonstrativo de retorno depois de dois meses... só que ninguém lê o demonstrativo de retorno linha por linha né, é um PDF de oitenta páginas...
Renato: Isso! É o ralo invisível do consultório. A clínica sangra no faturamento e o médico acha que o problema é o preço da consulta dele ou que tem que trabalhar sábado... Não é! O problema é que o dinheiro evapora na burocracia do TISS. E tem outra coisa, sobre a segurança da integração bancária, acho que a gente usa [inaudível] na criptografia do Open Finance, né? Preciso ver com o time de engenharia se já tá homologado no Banco Central...
Mariana: Sim, as secretárias têm pânico de mexer em planilha... quando a gente mostra que no nosso dashboard a guia já entra conciliada com o extrato em verde e a glosa em vermelho com o botão de gerar recurso automático, elas quase choram de alívio...
Renato: Vamos transformar isso num artigo e num post pro LinkedIn. Título provisório: "O ralo invisível do faturamento médico". Mas ó, não fala que a secretária erra, a culpa é da operadora que muda regra toda hora...
```

---

## 2. Relatório de Saneamento Técnico (3 Blocos Canônicos)

```markdown
# Relatório de Saneamento — Reunião "Ralo Invisível das Glosas"

### 1. Bloco do que foi CORRIGIDO (Padronização e Limpeza sem Alterar Conteúdo)
- **Pontuação e Quebras:** Ajustada pontuação oral, vírgulas de pausa e inseridos parágrafos estruturados.
- **Caixa e Acentuação:** Correção de maiúsculas/minúsculas e acentuação gramatical em português.
- **Siglas na 1ª Menção:** Expandidas siglas para compreensão (`TISS - Troca de Informação em Saúde Suplementar`; `ANS - Agência Nacional de Saúde Suplementar`).
- **Termos Técnicos em Inglês:** Grafados em itálico e mantidos no idioma original de acordo com o `glossario.md` (*dashboard*, *script*, *Open Finance*).
- **Remoção de Muletas de Fala:** Eliminados vícios orais pontuais ("né", "ó", "tipo assim") sem suprimir nenhuma ideia.

### 2. Bloco do que foi PRESERVADO SEM REESCRITA (Inteligência e Fatos Originais)
- **Metáfora Central do Autor:** A expressão *"o ralo invisível do consultório"* preservada na íntegra como conceito-chave de posicionamento.
- **Caso Real Anônimo:** A história da clínica de Campinas com R$ 40 mil em guias retidas após dois meses mantida exatamente como relatada.
- **Diretriz de Marca Expressa:** A instrução do fundador (*"não culpar a equipe de recepção, a culpa é da mudança silenciosa de regras das operadoras"*) preservada como restrição inegociável para a redação.
- **Dor Real do Usuário:** A constatação de que demonstrativos de retorno em PDFs de 80 páginas são humanamente inviáveis de auditar manualmente.

### 3. Bloco de PENDÊNCIAS LEVANTADAS (Lacunas e Incertezas da Fonte)
- **Lacuna Técnica [CRÍTICA]:** O trecho em que o fundador menciona a criptografia do Open Finance ficou `[inaudível]` e ele mesmo diz que *"precisa ver com o time de engenharia se já tá homologado"*.
  ➔ **Ação Mandatória:** VEDADO utilizar qualquer afirmação sobre homologação no Banco Central ou padrão de criptografia até que o time técnico confirme formalmente por escrito.
- **Dados da Clínica de Campinas:** Manter como relato anônimo de bastidor. Não associar o nome da clínica em nenhum material público.

### Validação de Integridade
- [x] O arquivo bruto original permanece 100% inalterado na Seção 1.
- [x] Nenhuma inferência especulativa foi acrescentada na base limpa.
- [x] As pendências foram catalogadas antes da produção de qualquer cópia.
```

---

## 3. Base Limpa em Blocos Temáticos

```markdown
### Bloco 1: A Dor Central (O Ralo Invisível)
- Consultórios com agendas lotadas podem apresentar sangria oculta de faturamento.
- Glosas não identificadas acumulam montantes vultosos (exemplo de clínica que descobriu R$ 40.000 em guias retidas sem saber).
- A causa raiz é a impossibilidade prática de auditar manualmente relatórios de retorno de operadoras com dezenas de páginas.

### Bloco 2: A Proposta e Mecanismo da Lúmina
- Cruzamento automático entre o lote TISS e o extrato da conta bancária.
- Visualização instantânea no *dashboard*: conciliações aprovadas em verde, divergências e glosas em vermelho.
- Botão de recurso automatizado: identifica a guia rejeitada e gera o arquivo de reapresentação antes que expire o prazo legal de recurso.

### Bloco 3: Metáforas e Ângulos de Abordagem
- Metáfora: "O ralo invisível do faturamento médico".
- Contraste: O médico acha que precisa aumentar o valor da consulta ou trabalhar aos sábados, quando na verdade o dinheiro produzido está sendo retido pelo plano de saúde.
```

---

## 4. Plano de Oportunidades e Matriz de Reaproveitamento

| ID | Canal de Destino | Formato | Ângulo Editorial | Persona / Dores | Fato da Base Usado | Dependência | Prioridade e Decisão |
|---|---|---|---|---|---|---|---|
| **OP-01** | **LinkedIn** | Post reflexivo | A armadilha da agenda cheia vs. caixa vazio | Médico dono de clínica / Falta de tempo | Caso de Campinas (R$ 40 mil retidos sem aviso) | Nenhuma | **Alta (Executar de Imediato)**: Valida a tese central com o público decisor. |
| **OP-02** | **Blog Técnico** | Artigo de 1.200 palavras | Anatomia de um demonstrativo de retorno de convênio | Gestor e faturista de clínica médica | PDF de 80 páginas e mecanismo de lote TISS | Depende da tese do OP-01 | **Média (Planejada)**: Constrói autoridade orgânica para buscas de "glosas TISS". |
| **OP-03** | **Instagram** | Carrossel visual em 5 telas | 3 sinais de que seu consultório tem glosas invisíveis | Médicos jovens e consultórios individuais | Metáfora do ralo invisível e cores do *dashboard* | Depende do artigo (OP-02) | **CORTADO DELIBERADAMENTE (Justificativa: Focar primeiro em texto longo e LinkedIn; produzir carrossel apenas após validação dos dados com a engenharia).** |
| **OP-04** | **E-mail Base** | Newsletter de quinta-feira | O que aprendemos com 40 mil reais em guias perdidas | Base de médicos inscritos no teste grátis | História do Dr. Renato na reunião de produto | Requer aprovação da ficha de oferta | **Alta (Executar)**: Excelente gancho para ativação de contas no período de teste. |
