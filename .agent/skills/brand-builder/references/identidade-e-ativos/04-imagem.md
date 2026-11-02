# 4. Imagem: fotografia, ilustração, ícones, padrões e imagem gerada por IA

**Fontes:** `visual-identity` (estilo de fotografia, ilustração, ícones, padrões, formas e efeitos), `brand-guidelines` (estilo de foto e de ilustração), `branding-expert` (seção de fotografia e iconografia), `brand-strategy-framework` (elementos visuais), `brand-design-system/references/decisoes.md` (seção 9, "Style 0N"). Reescrito e ampliado no E5.

> **Divisão de trabalho.** A etapa 6 define **a direção** da imagem (fotografia documental ou produzida, ilustração, tipografia como imagem) e a etapa 7 registra os estilos travados por imagem de referência ("Style 01", "Style 02") e o prompt copiável. Este capítulo é o **manual de uso**: regras de execução, direitos, tratamento, biblioteca e imagem gerada por IA.

## 4.1 Fotografia

Registrar, uma regra por linha, com o "pode" e o "não pode":

| Item | O que decidir |
|---|---|
| **Linha** | Documental (gente real, luz natural, imperfeição) x produzida (estúdio, direção) |
| **Assuntos e cenários** | O que aparece (pessoas, produto, lugar, detalhe) e em que contexto |
| **Luz e cor** | Natural ou controlada; quente ou fria; contraste; relação com a paleta |
| **Composição** | Enquadramentos e ângulos típicos; espaço livre para texto; proporções |
| **Tratamento** | Granulação, saturação, filtros, preto e branco, duotone; o que **nunca** se aplica |
| **Pessoas** | Representatividade, naturalidade, direção de olhar; evitar clichê de banco de imagem |
| **O que nunca mostrar** | Cenas, objetos, símbolos e situações vetados (vem de "não deve parecer" e de "o que NÃO comunicar") |

Cada regra de fotografia deve apontar para a decisão de origem (`06-direcao-visual.md`).

## 4.2 Ilustração

| Item | O que decidir |
|---|---|
| Estilo | Plana, dimensional, desenhada à mão, geométrica, colagem |
| Cor | Só a paleta da marca, ou ampliada? Quantas cores por peça |
| Traço | Espessura, acabamento, ausência de contorno |
| Complexidade | Quanto detalhe; legibilidade em tamanho pequeno |
| Personagens | Existem? Proporções, expressões, o que não fazem |
| Uso | Onde ilustra (explicação, capa, vazio de tela) e onde não entra |

## 4.3 Ícones

- **Um conjunto só**: mesmo estilo (traço ou preenchido), mesma espessura, mesmo raio de canto, mesma grade.
- Tamanhos oficiais e tamanho mínimo legível.
- Cor: herda do texto ou usa a primária; ícone que carrega significado precisa de texto junto (acessibilidade).
- Origem do conjunto e licença (inventário de ativos).

## 4.4 Padrões, formas e efeitos

Elementos que reforçam a identidade sem ser logo (vindos do guia `visual-identity`):

| Elemento | Perguntas |
|---|---|
| **Padrões e texturas** | Existem? Onde entram (fundos, embalagem, divisores) e em que escala |
| **Formas características** | Que formas aparecem repetidas (cantos, círculos, linhas)? Contêineres e divisores |
| **Efeitos** | Sombra, sobreposição (overlay), gradiente. **Gradiente só se o `style-guide.md` da marca já usa** (regra do `brand-design-system`) |

Sem emoji em artefatos de design e de marca, salvo decisão registrada.

## 4.5 Imagem com texto e por canal

- **Texto sobre imagem:** garantir contraste do texto sobre a parte da imagem onde ele cai (usar área calma, base lisa ou overlay). Nunca texto sobre a parte mais movimentada.
- **Proporções por canal:** definir um conjunto fixo (por exemplo quadrado, retrato, paisagem e vertical de vídeo) e a "zona segura" onde o logo e o texto não são cortados. Valores atuais por plataforma mudam: conferir em `ads-multiplataforma/references/platform-specs.md` e na documentação da plataforma na hora de produzir; em carrossel de 4:5, ver `social-direcao-de-arte-ia`.
- **Recortes e fundos:** fundo da marca, fundo transparente, ou fundo lido da foto; uma regra só.

## 4.6 Direitos, autorização e conformidade

| Tipo | Regra |
|---|---|
| **Foto própria** | Quem fotografou, para que usos, até quando; guardar a cessão de direitos |
| **Banco de imagens** | Anotar a licença e os usos permitidos (digital, impressão, anúncio, revenda); guardar o comprovante |
| **Pessoas fotografadas** | A imagem de uma pessoa identificável pode ser **dado pessoal** (e, conforme o que revela, dado sensível, como origem racial ou saúde), e o uso comercial da imagem exige **autorização prévia** (Código Civil, art. 20). Pedir autorização **por escrito, específica** para a finalidade, os canais e o prazo previstos; autorização genérica é frágil e o consentimento pode ser revogado. Ver `geral-conformidade-lgpd` e validar com o jurídico. Conferir o texto oficial das leis; este guia não é parecer jurídico |
| **Imagens de terceiros** (clientes, parceiros, mídia) | Só com permissão; citar a fonte |
| **Marca registrada de terceiros em cena** | Evitar, ou confirmar o uso |

Sem decisão do usuário sobre licença, não afirmar que uma imagem está liberada.

## 4.7 Imagem gerada por IA

A marca pode ou não usar. É **decisão do usuário** e fica registrada:

- **Permitido para quê** (rascunho, moodboard, fundo, ilustração final) e **proibido para quê** (rostos de pessoas reais, depoimentos, resultados, prova social).
- **Consistência:** usar o `visual-style.md` da marca (passo 7b do `brand-design-system`) como bloco de estilo fixo no prompt, mais uma frase de assunto; para cor exata, ver `audiovisual-imagem-flux-prompts` (prompt por hex) e, para carrossel, `social-direcao-de-arte-ia`.
- **Revisão humana** antes de publicar: mãos, texto dentro da imagem, símbolos acidentais, semelhança com marca ou pessoa real.
- **Rótulo:** decidir se a peça avisa que foi gerada por IA e onde, conforme o canal e a regra da plataforma vigente (conferir na hora).

## 4.8 Biblioteca de imagens

Onde mora cada coisa, para ninguém recorrer ao "banco de imagem genérico":

- Estrutura de pastas por uso (produto, equipe, bastidores, ilustrações, ícones, fundos) e convenção de nomes.
- Cada arquivo com origem, licença, data e dono (inventário de ativos, `../../brandbook-e-ativos.md`, seção 6).
- Versões: original, tratada e por canal. Não sobrescrever o original.
- Texto alternativo (alt) padrão para imagens recorrentes: descrever o que importa, curto; imagem decorativa sem alt.

## 4.9 Estilos travados por imagem (ponte com a etapa 7)

Quando o usuário trouxer imagens de referência, cada uma pode virar um "Style 0N" no design system, com: imagem de referência, regras (luz, ângulo, paleta, tratamento, composição, o que nunca aparece) e prompt copiável. Sem imagens, a seção fica como **espaço honesto** ("a confirmar"); não inventar estilos de imagem.

## 4.10 Saída deste capítulo

Seção "Imagem" do `identidade-e-ativos.md`:

```
## Imagem
Fotografia (4.1) / Ilustração (4.2) / Ícones (4.3) / Padrões e efeitos (4.4)
Texto sobre imagem e proporções (4.5) / Direitos e autorizações (4.6) / Imagem gerada por IA (4.7)
Biblioteca e alt (4.8) / Estilos travados (4.9) / Lacunas
```

## Checklist

- [ ] Fotografia: linha, luz, composição, tratamento, "o que nunca mostrar"
- [ ] Ilustração e ícones com conjunto único e regras de uso
- [ ] Gradiente e efeitos só se a marca já usa
- [ ] Regra de texto sobre imagem e conjunto de proporções com zona segura
- [ ] Direitos e autorizações registrados por tipo de imagem
- [ ] Política de imagem gerada por IA decidida pelo usuário
- [ ] Biblioteca com origem, licença e dono; alt padrão
- [ ] Estilos de imagem só com referência real (ou lacuna declarada)
