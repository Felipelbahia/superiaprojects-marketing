---
name: site-injecao-de-cta-astro
description: "Insere blocos de CTA (newsletter, produto, isca digital) em posts de um site Astro, com posição inteligente, pontuação de relevância feita pelo próprio agente, pré-visualização obrigatória e reversão por git. Sem programas: o agente lê e edita os arquivos de conteúdo do site. Gatilhos: \"adicione CTA nos posts\", \"inserir inscrição na newsletter nos artigos\", \"promova o produto nos posts do blog Astro\". NÃO use para criar o CTA em si (use copy-landing-page e cta-writing de copy-conversao), para escolher onde ele vai na página (use site-cro) nem para sites que não são Astro."
argument-hint: "[caminho do site] [tipo de CTA] [filtro de posts]"
---

# Astro CTA Injector

Versão recriada na R16b (2026-10-20). A anterior mandava rodar scripts Python (`score_posts.py`, `preview_injection.py`, `inject_ctas.py`) que nunca existiram; está arquivada em `.agent/skills/_arquivo/mescladas/r16b-design/workflows/astro-cta-injector.md`. **Esta versão não usa programa:** o agente lê os posts, pontua, mostra o que mudaria e só então edita. Se um dia você quiser automação em lote, os scripts só entram com **autorização explícita** (regra 1.5).

## Pré-requisitos (perguntar, não presumir)

1. **Caminho do site Astro** (a pasta do projeto do usuário; fica **fora** deste repositório) e a pasta dos posts (em geral `src/content/blog`, arquivos `.md`, `.mdx` ou `.astro`).
2. **Controle de versão:** o site tem `git`? Se sim, a reversão é por `git`; se não, o agente **para** e pede para copiar a pasta de posts antes (cópia de segurança em outra pasta).
3. **Marca e CTA:** qual marca (regra 1.1), qual tipo (newsletter, produto, isca digital), texto do CTA e URL de destino. O texto do CTA passa pelo [geral-anti-slop](../skills/geral-anti-slop/SKILL.md) e segue a voz da marca.
4. **Autorização (regra 1.5):** o agente edita arquivos do site do usuário. Peça o **"sim" explícito** para alterar esses arquivos, uma vez por lote.

## Posições possíveis

| Posição | Onde entra | Serve para |
|---|---|---|
| `fim` | Depois de todo o conteúdo | CTA discreto |
| `meio` (50%) | Depois de metade dos parágrafos | Engajamento no meio do texto |
| `60%` | Depois de 60% dos parágrafos | Engajamento mais tardio |
| `apos-h2` | Depois do primeiro H2 | Engajamento cedo |
| `antes-conclusao` | Antes do último parágrafo | Fechamento forte |

Dica de conversão: o CTA do meio costuma funcionar melhor em texto longo; no texto curto, use o fim. Regras de formulário e de popup: [site-cro](../skills/site-cro/SKILL.md).

## Procedimento

1. **Listar** os posts da pasta (nome, título, tamanho em palavras, se já tem CTA).
2. **Pontuar** cada post de 0 a 10 para o tipo de CTA: palavras-chave do tema (ex.: "dica", "guia", "estratégia" para newsletter), tamanho (texto mais longo é melhor candidato), alinhamento do tema com a oferta, e **descartar** (nota 0) o que já tem CTA ou é página institucional. Mostrar a tabela com a nota e o motivo. Limite padrão para entrar no lote: 5.
3. **Pré-visualização (obrigatória):** para cada post do lote, mostrar o trecho antes e depois, com a posição escolhida. **Nada é gravado nesta etapa.**
4. **Confirmação:** o usuário aprova o lote inteiro ou retira posts.
5. **Aplicar** só o aprovado. O bloco leva um **marcador** (`<!-- cta:newsletter -->`) no início e no fim, para a inserção ser idempotente: se o marcador já existe, **não inserir de novo**.
6. **Verificar:** reabrir cada arquivo editado, conferir que o marcador aparece uma vez, que o Markdown continua válido e que o `.mdx` ou `.astro` não perdeu o `import`. Se o site tem comando de build (`npm run build`), pedir ao usuário para rodar, ou rodar com a autorização dele, e conferir que não há erro.
7. **Relatório:** quais posts foram alterados, quais ficaram de fora e por quê, e como desfazer (`git diff` e `git restore <arquivo>`, ou a cópia de segurança).

## Modelo de bloco (HTML)

```html
<!-- cta:newsletter -->
<aside class="cta-newsletter" data-cta-type="newsletter">
  <h3>{{titulo}}</h3>
  <p>{{descricao}}</p>
  <form action="{{url_do_formulario}}" method="post">
    <label for="cta-email">E-mail</label>
    <input id="cta-email" type="email" name="email" placeholder="voce@exemplo.com" required />
    <button type="submit">{{texto_do_botao}}</button>
    <p class="cta-consent">{{texto_de_consentimento_lgpd}} <a href="{{url_da_politica_de_privacidade}}">Política de privacidade</a></p>
  </form>
</aside>
<!-- /cta:newsletter -->
```

Variáveis: `titulo`, `descricao`, `url_do_formulario` (ou `url_do_produto`, `url_da_imagem`), `texto_do_botao`, `texto_de_consentimento_lgpd` (revisar com [geral-conformidade-lgpd](../skills/geral-conformidade-lgpd/SKILL.md)). Em projeto com componente Astro de CTA, prefira inserir o **componente** (`<CtaNewsletter />`) no lugar do HTML solto, respeitando o `import`.

## Limites

- Não altera o site sem o "sim" explícito e não publica.
- Não conecta o formulário a serviço real: a URL do formulário vem do usuário.
- Não inventa número nem prova social no texto do CTA.
