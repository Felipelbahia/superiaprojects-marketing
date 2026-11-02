# 1. Logo: versões, uso e kit de arquivos

**Fontes:** `visual-identity` (versões e proibições), `brand-guidelines` (uso do logo), `branding-expert` (seção 6), guia da AgentKits (tamanho mínimo e respiro como exemplo). Reescrito e ampliado no E5.

> Este capítulo registra **regras de uso**. Ele não desenha logo. Se a marca não tem logo, vá ao fim do capítulo (briefing de logo).

## 1.1 Inventário de versões

Toda marca precisa decidir quais versões existem e quando cada uma entra. Preencher a tabela com o usuário; versão que não existe vira lacuna declarada.

| Versão | Quando usar | Existe? |
|---|---|---|
| **Principal** (completa: símbolo + nome) | Padrão: site, apresentações, material institucional | |
| **Secundária / simplificada** | Espaços horizontais ou verticais apertados | |
| **Símbolo (ícone) sozinho** | Avatar de rede social, favicon, ícone de app, selos | |
| **Só o nome (logotipo)** | Quando o símbolo já aparece perto, ou em texto corrido | |
| **Monocromática** (1 cor) | Carimbos, bordados, jornal em preto e branco, marca d'água | |
| **Reversa** (clara sobre fundo escuro) | Fundos escuros e fotos | |
| **Sobre cor** | Cor de fundo da marca, se houver regra específica | |

Regra: cada versão aponta para um arquivo real (ver 1.6). Versão sem arquivo não conta.

## 1.2 Área de respiro (clear space)

Espaço livre mínimo em volta do logo, onde nenhum texto, borda ou imagem entra.

- Definir por **unidade do próprio logo**, não por pixel: por exemplo "1x = altura da letra principal" ou "altura do símbolo", e a área de respiro vale 1x em cada lado. Assim a regra escala com o tamanho.
- Alternativa usada em guias reais: porcentagem da largura do logo (o guia da AgentKits fixa 20% da largura; é **exemplo** de como escrever, não valor para outras marcas).
- Desenhar um diagrama com a unidade marcada (o brandbook mostra; em texto, descrever a medição).
- A área vale também para as versões reversa e monocromática.

## 1.3 Tamanho mínimo

Abaixo de certo tamanho o logo perde legibilidade. Definir **dois** mínimos, separados:

| Meio | Como medir | Observação |
|---|---|---|
| Tela | Largura em pixels (e altura, se o logo for vertical) | O guia da AgentKits usa 40 px como exemplo; testar com o logo real |
| Impressão | Largura em milímetros | Depende do processo de impressão e da gráfica; confirmar com ela quando houver |
| Símbolo isolado | Pode ter mínimo menor que o logo completo | Testar em favicon (16 e 32 px) |

Teste prático: reduzir o logo até o menor detalhe sumir ou virar mancha; o mínimo é o tamanho um pouco acima disso. `[derivado]` A medida final é do usuário.

## 1.4 Fundos e contraste

| Situação | Regra |
|---|---|
| Fundo claro liso | Versão principal |
| Fundo escuro liso | Versão reversa |
| Fundo de cor | Usar a versão que passa no contraste (ver capítulo 2, seção "acessibilidade") ou a monocromática |
| Foto ou fundo movimentado | Colocar o logo em área calma da imagem, ou sobre uma base lisa; nunca sobre textura que cruze o desenho |
| Fundo com gradiente | Só se a marca já usa gradiente (regra do `brand-design-system`) |

Conferir o contraste do logo sobre claro e escuro, como pede o `roteiro-visual.md` da direção visual.

## 1.5 O que nunca fazer

- Esticar, achatar ou distorcer.
- Trocar as cores por outras fora da paleta aprovada.
- Acrescentar efeitos: sombra, brilho, relevo, contorno, gradiente que não existe.
- Girar ou inclinar.
- Mudar a posição ou a proporção entre símbolo e nome.
- Colocar sobre fundo movimentado ou de baixo contraste.
- Apertar contra bordas, textos ou outros logos (respeitar a área de respiro).
- Redesenhar, trocar a fonte do nome ou "refazer de memória".
- Usar uma versão em baixa resolução ampliada.

Cada item merece um exemplo visual no brandbook ("certo" ao lado de "errado"). Sem exemplo, vira texto que ninguém lê.

## 1.6 Kit de arquivos

Entregar o logo em um conjunto organizado. Formatos e quando usar:

| Formato | Para quê | Observação |
|---|---|---|
| **SVG** | Site, aplicativo, qualquer tela; escala sem perder qualidade | Fonte principal para o `brand-design-system` (`logo.svg`, `logo-light.svg`) |
| **PNG com fundo transparente** | Apresentações, documentos, quando não dá para usar SVG | Entregar em tamanhos grandes e conferir fundo claro e escuro |
| **PDF ou EPS vetorial** | Gráfica, impressão, sinalização | Texto convertido em curvas |
| **Favicon e ícones de app** | Aba do navegador, tela inicial | Tamanhos exigidos pela plataforma de destino; conferir a documentação atual dela |
| **Avatar de redes sociais** | Perfis | Recorte quadrado ou redondo; símbolo sozinho costuma funcionar melhor |

Nomear de forma consistente (marca, versão, cor, formato), por exemplo `marca_principal_colorido.svg`, `marca_simbolo_reverso.png`. Registrar no inventário de ativos (ver `../../brandbook-e-ativos.md`, seção 6) com local, formato e dono.

## 1.7 Briefing de logo (quando a marca não tem)

Nenhuma skill do repositório desenha logo. Para quem vai desenhar (designer, agência, ferramenta), entregar um briefing curto, montado a partir das etapas já aprovadas:

1. **Essência em uma frase** e **arquétipo** (`01-essencia.md`, `02-posicionamento.md`).
2. **Sensação em 3 palavras** e **"não deve parecer"** (`06-direcao-visual.md`).
3. **Onde o logo vai aparecer primeiro**: favicon, avatar, cabeçalho de site, impresso. Isso fixa o teste de tamanho mínimo.
4. **Restrições**: cores já decididas, fontes, símbolos que não podem aparecer (jurídico, cultura, concorrentes).
5. **Referências aprovadas e rejeitadas** (com o porquê), em palavras.
6. **Versões a entregar** (tabela 1.1) e **formatos** (tabela 1.6).
7. **Teste de nome**: o nome já passou pelos 6 portões de `brand-naming`? Logo de nome que muda é retrabalho.

Aprovação: o usuário vê o logo nas versões principal, símbolo e monocromática, em fundo claro e escuro, e em tamanho mínimo, antes de qualquer outra coisa ser construída sobre ele.

## 1.8 Saída deste capítulo

Seção "Logo" do `identidade-e-ativos.md`:

```
## Logo
Versões existentes (tabela 1.1) / Unidade da área de respiro / Tamanho mínimo (tela e impressão)
Regras de fundo / O que nunca fazer (com exemplos) / Kit de arquivos e local / Lacunas
```

## Checklist

- [ ] Versões listadas e cada uma com arquivo
- [ ] Área de respiro definida por unidade do logo
- [ ] Tamanho mínimo para tela e para impressão (ou lacuna declarada)
- [ ] Regra para fundo claro, escuro, de cor e de foto
- [ ] Lista do que nunca fazer, com exemplos
- [ ] Kit com SVG, PNG transparente e vetorial para impressão
- [ ] Nomes de arquivo consistentes e inventário atualizado
