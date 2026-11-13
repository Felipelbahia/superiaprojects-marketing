# Cenários multi-marca e multi-produto

Usar na conversa de criação (SKILL.md, "Conversa de criação"), só quando o usuário responder que há mais de uma marca ou produto. Mono-marca (o padrão) não usa este arquivo: a árvore é a de `arvore-padrao.md`, sem subpastas.

Princípio: cada pasta de topo tem um **escopo** (`projeto`, `marca` ou `produto`). Só a que diverge ganha subpasta; o compartilhado fica na raiz. O mapa registra o **caminho completo** de cada tipo de peça, com placeholders (`{marca}`, `{produto}`, `{tipo}`), e é ele que as skills seguem.

## Pergunta 2: como marcas e produtos se relacionam

### A. Marcas independentes
Cada marca tem voz, público e equipe próprios. Cada uma é um projeto completo.
```text
marcas/
├── {marca}/
│   ├── brand/  estrategia/{estrategia-geral.md, calendarios/, campanhas/}
│   ├── conteudos/{tipo}/…  inteligencia/  assets/
docs/mapa-de-destinos.md      # um mapa para o conjunto, na raiz
```
Caminho no mapa: `marcas/{marca}/conteudos/{tipo}/AAAA-MM-DD - Nome/`.

### B. Uma marca, vários produtos
Os produtos herdam a voz da marca. `brand/` é único; o produto é eixo nas pastas que divergem.
```text
brand/
estrategia/estrategia-geral.md  estrategia/calendarios/     # da marca
estrategia/{produto}/campanhas/AAAA-MM-DD - Nome/
conteudos/{produto}/{tipo}/AAAA-MM-DD - Nome/
inteligencia/                                                # compartilhada, se o mercado é o mesmo
assets/{produto}/
```
Caminho no mapa: `conteudos/{produto}/{tipo}/…` e `estrategia/{produto}/campanhas/…`.

### C. Marcas independentes, cada uma com produtos
Combina A e B: cada marca é um projeto, e dentro dela o produto é eixo.
```text
marcas/{marca}/
├── brand/  estrategia/estrategia-geral.md  estrategia/calendarios/
├── estrategia/{produto}/campanhas/…
├── conteudos/{produto}/{tipo}/…
├── inteligencia/  assets/{produto}/
```
Caminho no mapa: `marcas/{marca}/conteudos/{produto}/{tipo}/AAAA-MM-DD - Nome/`.

### D. Produtos com identidade própria sob uma marca-mãe
Como B, mas com voz, persona ou kit visual próprios para o produto. O que difere vai em `brand/produtos/{produto}/`; o que é igual continua em `brand/`.
```text
brand/                         # marca-mãe (fundações, voz base, kit)
brand/produtos/{produto}/      # só o que difere: voz, persona, kit do produto
estrategia/  conteudos/{produto}/…  assets/{produto}/   # como em B
```
O `brand-builder` trata `brand/produtos/{produto}/` como raiz de marca do produto e herda de `brand/` o que não estiver ali.

## Pergunta 3: onde as marcas moram (cenários A e C; em B e D, perguntar também se algum produto precisa de repositório próprio)

| | Mesmo projeto, `marcas/{marca}/` | Um repositório por marca |
|---|---|---|
| Configuração de skills e regras | Uma só, no projeto | Repetida em cada repositório (paridade de `CLAUDE.md`, `GEMINI.md`, `AGENTS.md` por marca) |
| Inteligência de mercado compartilhada | Fácil: `inteligencia/` na raiz | Precisa ser duplicada ou apontada (ver abaixo) |
| Isolamento (acesso, histórico, equipes diferentes) | Fraco | Total |
| Visão do portfólio (campanhas de todas as marcas) | Direta | Exige olhar repositório por repositório |
| Entra uma marca nova | Cria uma pasta | Cria um repositório |
| Onde mora o mapa | Raiz do projeto, um só | Um por repositório, com a seção "Respostas" apontando os repositórios irmãos |
| Quando faz sentido | Mesma equipe ou equipe pequena | Equipes ou clientes diferentes, com confidencialidade |

Não recomendar por padrão: perguntar sobre equipes, clientes e confidencialidade antes.

**Inteligência compartilhada entre repositórios** é decisão do usuário: (i) um repositório de inteligência próprio, lido por todos em somente leitura; (ii) cópia datada em cada repositório; (iii) inteligência por marca, sem compartilhar. Registrar a escolha e o caminho na seção "Respostas" do mapa.

## Pergunta 4: o que é compartilhado (sugestão padrão por pasta)

Apresentar a tabela inteira e pedir só as exceções ("de acordo? o que muda?"), em vez de uma pergunta por pasta.

| Pasta | Sugestão | Por quê |
|---|---|---|
| `brand/` | por marca (A, C); único (B); mãe + produtos (D) | Voz e identidade pertencem à marca |
| `inteligencia/` | **compartilhada** se o mercado é o mesmo; por marca se os mercados são diferentes | Tendência e estudo valem para quem atua no mesmo setor |
| `estrategia/` | por marca ou produto; `estrategia-geral.md` e `calendarios/` ficam no nível da marca | Campanha tem dono |
| `conteudos/` | por marca ou produto | A esteira de aprovação segue o dono |
| `assets/` | por marca ou produto | Imagem de uma marca raramente serve à outra |

Registrar as respostas na coluna **Escopo** do mapa e o caminho completo na coluna **Caminho**.
