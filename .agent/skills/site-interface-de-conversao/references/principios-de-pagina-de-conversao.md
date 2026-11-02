# Princípios de página de conversão

> Junção, na R16b (2026-10-20), de `frontend-design.md` e `ui-ux-pro-max.md` (originais em `.agent/skills/_arquivo/mescladas/r16b-design/ui-ux-conversion-designer/`). Números de medida e de contraste aqui valem para todas as skills do hub. **Números de desempenho (queda por segundo, taxa de conversão) não estão aqui:** são "ordem de grandeza, sem fonte primária" e ficam só em [element-benchmarks.md](../../site-cro/references/element-benchmarks.md).

## 1. Anatomia da página de conversão

Ordem usual: **Hero → prova social (logos, números) → problema → solução → recursos → depoimentos → preço → FAQ → CTA final.** O texto de cada bloco está em [copy-landing-page](../../copy-landing-page/SKILL.md); aqui só a função visual:

| Bloco | Função |
|---|---|
| Hero | Gancho, proposta de valor, CTA principal. Sempre acima da dobra: título, subtítulo, CTA, um sinal de confiança, uma imagem |
| Prova social | Logos e números logo abaixo do hero |
| Problema e solução | Reconhecimento da dor, depois como você resolve |
| Recursos | Cada recurso com o benefício ("para que serve") |
| Depoimentos | Antes do preço |
| Preço | Opções claras, plano recomendado destacado |
| FAQ | Quebra de objeção |
| CTA final | Última chamada, repetindo a promessa |

## 2. Hierarquia visual

- **Um foco primário por tela.** Ordem de atenção: título (maior), imagem de apoio, subtítulo, botão, conteúdo secundário.
- Ferramentas de hierarquia: **tamanho** (quanto maior, mais importante), **cor** (a cor de marca enfatiza), **espaço em branco** (isolar chama atenção), **posição** (alto e à esquerda é visto primeiro).
- Razão de escala: título 1,5 a 2 vezes o corpo; secundário 1,25; legenda 0,875.

## 3. Cor

- **60-30-10:** 60% base, 30% estrutura, 10% acento. O acento é **só para CTA, links críticos e alertas**; nunca em fundo decorativo.
- O botão principal contrasta com a página e tem **significado único** (a mesma cor significa a mesma coisa em todo o site).
- Associações de cor (azul = confiança, verde = crescimento, laranja = ação, vermelho = urgência, preto = luxo) são **ponto de partida**, não regra: a identidade da marca em `_brands/<marca>/style-guide.md` vence.
- **Contraste (WCAG AA):** texto normal 4,5:1; texto grande e componentes de interface 3:1.

## 4. Tipografia

| Nível | Tamanho | Peso |
|---|---|---|
| Display (hero) | 64 a 80 px | Negrito |
| H1 | 48 a 56 px | Negrito |
| H2 | 32 a 40 px | Seminegrito |
| H3 | 24 a 28 px | Seminegrito |
| Corpo | 16 a 18 px | Regular |
| Legenda | 14 px | Regular |

No celular o título do hero cai 40 a 50%. Corpo: **mínimo de 16 px**, linha de 1,5 a 1,7, **50 a 75 caracteres por linha**, parágrafos de 3 a 4 frases. Título distintivo e corpo limpo; no máximo duas famílias.

## 5. Espaço, forma e componentes

- **Grade de 8 pontos** (base de 4 px): 4, 8, 16, 24, 32, 48, 64. Nomear os degraus e usar só eles.
- **Cartão:** ícone ou imagem, título, descrição, CTA. **Formulário:** rótulo **acima** do campo (placeholder só como exemplo), erro embaixo do campo, enviar em largura total no celular, texto do botão com a ação. Menos campos, menos desistência: 1 campo (e-mail) é o máximo de conversão, 2 a 3 é um bom equilíbrio, 4 ou mais já pesa.
- **Imagens:** foto real do produto em uso, não banco de imagem genérico; pessoas olhando para o CTA. WebP para foto, SVG para ícone, PNG só com transparência.
- **Confiança:** logos abaixo do hero, selos de segurança perto do formulário, depoimentos antes do preço, garantia perto do CTA.

## 6. Movimento

| Tipo | Duração |
|---|---|
| Micro (hover, foco) | 100 a 200 ms |
| Padrão | 200 a 300 ms |
| Complexo | 300 a 500 ms |

Curvas: `ease-out` para entrar, `ease-in` para sair, `ease-in-out` para mover. Animação de rolagem só para revelar conteúdo (fade, subida de cartões). Respeitar `prefers-reduced-motion`.

## 7. Celular e acessibilidade

- **Pontos de interrupção:** celular abaixo de 640 px, tablet 640 a 1024, desktop 1024 a 1280, largo acima de 1280.
- **Alvo de toque: 48 × 48 px** (44 px é o mínimo aceitável), com 8 px entre alvos. Esse é o valor único do hub (`site-interface-de-conversao`, `site-cro` e `copy-landing-page`).
- Desktop em várias colunas vira **uma coluna**; hover vira feedback de toque; menu fixo vira hambúrguer; CTA em largura total.
- Links com sublinhado ou cor distinta; botões com `:focus-visible` visível; formulários com rótulo; imagens com `alt`; navegação por teclado.

## 8. Antes de entregar

- [ ] Espaçamento consistente, elementos alinhados, hierarquia tipográfica clara
- [ ] Estados de hover, foco, carregamento e erro
- [ ] Layout em celular, tablet e desktop, sem rolagem horizontal
- [ ] Contraste, `alt` e teclado conferidos
- [ ] Teste no navegador (tela cheia e 375 px, console sem erro): ver o workflow [site-construcao-de-landing-page](../../../workflows/site-construcao-de-landing-page.md)

## 9. Testar primeiro o que importa

Alto impacto: títulos, CTAs, imagem do hero, prova social. Baixo impacto: cor do botão (o que conta é o contraste), fonte, espaçamento. Método de teste: [growth-testes-ab](../../growth-testes-ab/SKILL.md).

> Beleza que não converte é só arte. Boa estética é invisível: leva à ação sem atrito.
