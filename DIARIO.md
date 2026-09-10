# Diário de Bordo do Experimento: BST vs. AVL

## 1. Expectativas e Hipóteses Iniciais

Antes do início da coleta empírica dos dados, a hipótese teórica estruturada foi:
* **Entradas Aleatórias**: A Árvore Binária de Busca simples (BST) e a Árvore AVL teriam tempos de inserção muito semelhantes, apresentando comportamento de crescimento quase-linear $O(N \log N)$. Esperava-se apenas um leve *overhead* na AVL devido às checagens de fator de balanceamento.
* **Entradas Ordenadas**: A BST sofreria uma degradação severa, transformando-se em uma lista encadeada com altura $H = N$ e complexidade quadrática $O(N^2)$. Já a AVL, através de suas rotações $O(1)$, manteria a altura limitada a $O(\log N)$ e desempenho estável.

---

## 2. Obstáculos Técnicos Encontrados e Soluções

Durante o desenvolvimento da estrutura e execução do experimento, surgiram os seguintes problemas práticos:

1. **Incompatibilidade de Comandos de Shell no Windows**:
   * *Problema*: Tentativa inicial de usar comandos Unix (`mkdir -p` e `touch`) no Prompt de Comando do Windows gerou erros de sintaxe.
   * *Solução*: Adequação dos comandos para o padrão Windows utilizando `mkdir` e `type nul > arquivo`.

2. **Limite de Recursão da BST e Estouro de Pilha**:
   * *Problema*: Inserções recursivas em entradas ordenadas grandes causariam estouro do limite nativo da pilha de chamadas do Python (`RecursionError`).
   * *Solução*: Refatoração da inserção na classe `BST` para uma abordagem estritamente **iterativa** utilizando laço `while`.

3. **Resolução de Módulos e Dependências (`ImportError` e `ModuleNotFoundError`)**:
   * *Problema*: O Python não localizava os arquivos da pasta `src/` ao rodar o benchmark, e a biblioteca `matplotlib` não estava instalada no ambiente local para geração do gráfico.
   * *Solução*: Ajuste explícito do caminho de importação via `sys.path.append()` e instalação do pacote gráfico através do gerenciador de pacotes (`pip install matplotlib`).

4. **Configuração do Git e Autenticação de Usuário**:
   * *Problema*: Impasse no envio do código para o GitHub devido à ausência do executável Git no sistema e falha no `git commit` por falta de e-mail/nome configurados (`fatal: unable to auto-detect email address`).
   * *Solução*: Instalação do Git para Windows, configuração global da identidade (`git config user.email` e `user.name`) e consolidação correta do *commit* antes de realizar o `push`.

---

## 3. Lições Aprendidas e Conclusão

* **Análise pelas Razões $T(2N)/T(N)$**: A simples observação do tempo bruto não basta. Calcular a razão entre o tempo ao dobrar $N$ evidenciou o salto de $R \approx 2.0$ para $R \approx 4.0$ na BST ordenada, confirmando empiricamente a teoria de complexidade $O(N^2)$.
* **Resiliência da Árvore Balanceada**: A AVL demonstrou invariância à ordem de inserção dos dados, mantendo a razão de tempo estável em $R \approx 2.2$ tanto para dados aleatórios quanto para dados ordenados.