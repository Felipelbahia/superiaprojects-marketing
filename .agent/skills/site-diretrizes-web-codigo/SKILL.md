---
name: site-diretrizes-web-codigo
description: "Use para revisar CÓDIGO de interface contra as Web Interface Guidelines da Vercel (acessibilidade, UX, boas práticas), com saída terse em arquivo:linha. Busca a lista atual online a cada uso: precisa de acesso à internet. Gatilhos: \"revise minha UI\", \"cheque acessibilidade do código\", \"audite o design do site\". NÃO use para auditar a conversão de uma página (use site-cro), desenhar a interface (use site-interface-de-conversao) nem alterar página existente sem duplicar o que há (use site-auditoria-de-interface)."
license: MIT
metadata:
  author: vercel
  version: 1.0.0
---

# Web Interface Guidelines

Review files for compliance with Web Interface Guidelines.

## How It Works

1. Fetch the latest guidelines from the source URL below
2. Read the specified files (or prompt user for files/pattern)
3. Check against all rules in the fetched guidelines
4. Output findings in the terse `file:line` format

## Guidelines Source

Fetch fresh guidelines before each review:

```
https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md
```

Use WebFetch to retrieve the latest rules. The fetched content contains all the rules and output format instructions.

## Usage

When a user provides a file or pattern argument:
1. Fetch guidelines from the source URL above
2. Read the specified files
3. Apply all rules from the fetched guidelines
4. Output findings using the format specified in the guidelines

If no files specified, ask the user which files to review.
