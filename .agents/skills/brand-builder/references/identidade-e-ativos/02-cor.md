# 2. Cor: papéis, especificação para tela e impressão, acessibilidade

**Fontes:** `visual-identity` (tabela com CMYK e Pantone, uso por papel), `brand-guidelines` (paleta primária e de acento com RGB), `branding-expert` (sistema de cor: primária, secundária, neutra, semântica), `brand-strategy-framework` (psicologia das cores), guia da Anthropic (exemplo de paleta com papéis nomeados e cores de acento). Reescrito e ampliado no E5.

> **Divisão de trabalho com o `brand-design-system`.** Os valores de **tela** (hex, claro e escuro, contraste WCAG, exports) vivem no `tokens.json` e são decididos na etapa 7. Este capítulo **não os redigita**: referencia. O que nasce aqui é o que o design system não faz: **papéis de cor da identidade**, **especificação para impressão** (CMYK, Pantone), **regras por versão do logo** e **uso proibido**.

## 2.1 Papéis de cor da identidade

| Papel | O que é | Quantas | Onde aparece |
|---|---|---|---|
| **Primária** | A cor que identifica a marca | 1 a 2 | Logo, elementos-chave, botões principais |
| **Secundárias** | Apoiam a primária | 2 a 4 | Acentos, variedade, gráficos |
| **Neutras** | Texto, fundos, linhas | Escala de 4 a 8 degraus | Quase tudo |
| **Semânticas** | Estado: sucesso, aviso, erro, informação | 4 | Interface e avisos |
| **De acento** | Destaque pontual (o guia da Anthropic usa 3) | 1 a 3 | Chamadas e formas não textuais |

Regras:
- A cor da marca é **decisão do usuário** ou do `style-guide.md` existente (que vence). Cor sugerida pela IA é `[derivado]` e pede confirmação.
- Dar um **nome descritivo** a cada cor ("Azul Profundo"), não só código. O nome é o que o time usa no dia a dia.
- Cada cor tem **papel e regra de uso**: "primária para CTAs e elementos-chave; secundárias para apoio; neutras para texto e fundo".
- Cada cor de texto passa pelo contraste (seção 2.5).

## 2.2 Ficha de cor (modelo)

Uma linha por cor, com **todas** as especificações que a marca usará. Campos de tela vêm do `tokens.json`; campos de impressão são os novos.

| Nome | Papel | Hex | RGB | CMYK | Pantone | Uso e restrições |
|---|---|---|---|---|---|---|
| | primária | `#RRGGBB` | R, G, B | C, M, Y, K | código | |

Campos de impressão (CMYK, Pantone) ficam em branco com a marca **"a definir"** até existirem (ver 2.3). Hex em 6 dígitos maiúsculos, igual ao `tokens.json`, para a comparação por texto ser exata.

## 2.3 Tela x impressão: o que é possível derivar e o que não é

- **RGB e hex**: valores de tela. Fonte única no `tokens.json`.
- **CMYK**: valores de impressão por tintas. Converter hex em CMYK direto, por fórmula, costuma distorcer a cor e **não é confiável**: o resultado muda com o perfil de cor e com o papel. O valor CMYK oficial deve vir da gráfica ou de quem faz o arquivo de impressão (com prova de cor). Registrar como `[usuário]` ou `[externo]`, nunca como `[derivado]` apresentado como oficial.
- **Pantone**: cor de catálogo, usada quando a cor precisa ser idêntica entre fornecedores. Conversores de hex para Pantone (há vários) dão só o **candidato mais próximo**, não a cor certa; confirmar no **leque impresso** sob luz padrão ou em **prova medida pela gráfica**. Algumas cores Pantone não se reproduzem em RGB nem em CMYK, então a tela nunca mostra a cor exata. Sem leque ou prova, deixar "a definir".
- Cores muito saturadas na tela (azuis e verdes vivos) podem ficar menos vivas no CMYK. Avisar o usuário **antes** de a gráfica descobrir.
- Se a marca nunca vai para impressão, a coluna Pantone/CMYK pode ficar como "não se aplica"; registrar a decisão.

## 2.4 Cor por versão do logo

| Versão | Regra |
|---|---|
| Principal | Cores da identidade, em fundo claro |
| Reversa | Variante clara aprovada, em fundo escuro (não é inverter automaticamente) |
| Monocromática | Uma só cor: preto, branco ou a primária; definir qual por contexto |
| Em tons de cinza | Para impressão sem cor; conferir se as partes do logo continuam distinguíveis |

Cada variante é uma decisão com contraste conferido, como no modo escuro do design system.

## 2.5 Acessibilidade

- **Texto normal:** razão de contraste mínima de 4,5:1; **texto grande** (a partir de 24 px, ou 18,66 px em negrito) e componentes de interface: 3:1. Os pares e o cálculo estão em `brand-design-system/references/tokens-e-contraste.md`; não duplicar.
- Os limiares vêm do WCAG 2.x (critérios 1.4.3, contraste de texto, e 1.4.11, contraste de componentes de interface e gráficos). Os tamanhos em pixels são a aproximação usual de 18 pt e de 14 pt em negrito; conferir contra o tamanho efetivamente calculado pelo navegador. Texto oficial: W3C.
- Cor de marca que falha como texto vira uma **variante para texto** (`-text`) e mantém a original para fundos e ícones grandes.
- **Não depender só da cor** para comunicar estado (erro, sucesso): acrescentar ícone ou texto.
- Considerar daltonismo ao escolher pares que só se distinguem por matiz (verde x vermelho).

## 2.6 Uso proibido

- Cores fora da paleta aprovada no logo e em elementos de marca.
- Efeitos de cor sobre o logo (gradiente, brilho) que a marca não usa.
- Versões de logo ou cores "aproximadas" a olho em peças novas: usar sempre a ficha de cor.
- Combinações que reprovam no contraste, mesmo que "fiquem bonitas".

## 2.7 Psicologia das cores: use como hipótese

A tabela abaixo é do `brand-strategy-framework` e é uma **generalização cultural**, não regra. Tag `[externo]`. Serve para abrir a conversa, nunca para decidir sozinha; a cor da marca nasce da essência, do posicionamento e do público.

| Cor | Associações comuns | Setores onde aparece |
|---|---|---|
| Azul | Confiança, estabilidade, calma | Finanças, tecnologia, saúde |
| Verde | Crescimento, natureza, dinheiro | Finanças, saúde, ecologia |
| Vermelho | Energia, urgência, paixão | Alimentos, entretenimento, varejo |
| Laranja | Amigável, confiante, criativo | Tecnologia, alimentos, fitness |
| Roxo | Luxo, criatividade, sabedoria | Beleza, educação, luxo |
| Amarelo | Otimismo, clareza, calor | Alimentos, infantil, varejo |
| Preto | Sofisticação, luxo | Moda, luxo, tecnologia |

Cuidados: o significado muda por cultura e contexto (o branco, o roxo e o vermelho têm leituras diferentes em países diferentes); a "cor do setor" pode ser **justamente a cor da qual se afastar** para diferenciar (conferir no mapa de concorrentes da etapa 2). Quando o Sexy Canvas estiver em uso (etapa 5), a lente visual (`revenue-sexy-canvas`, referência `sexy-canvas-visual.md`) ajuda a ver qual desejo a paleta ativa.

## 2.8 Saída deste capítulo

Seção "Cor" do `identidade-e-ativos.md`:

```
## Cor
Papéis e ficha de cor (2.2) / Regras por versão do logo (2.4) / Acessibilidade (referência ao tokens.json)
Uso proibido / Lacunas de impressão (CMYK e Pantone "a definir", com quem confirma)
```

## Checklist

- [ ] Cada cor com nome, papel, hex e regra de uso
- [ ] Hex idêntico ao `tokens.json`
- [ ] CMYK e Pantone preenchidos por fonte confiável, ou marcados "a definir" com responsável
- [ ] Variante de logo aprovada para fundo escuro e para uma cor só
- [ ] Contraste conferido para texto; variante `-text` onde preciso
- [ ] Uso proibido registrado
- [ ] Psicologia das cores usada só como hipótese, com tag `[externo]`
