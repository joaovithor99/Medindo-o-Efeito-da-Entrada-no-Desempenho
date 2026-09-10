# Análise de Desempenho: BST Simples vs. Árvore AVL

Este estudo investiga empiricamente o impacto da organização dos dados de entrada no desempenho de algoritmos de busca e inserção em Árvores Binárias de Busca (BST simples) e Árvores Autobalanceadas (AVL).

---

## Tabela de Resultados Medidos

Para cada tamanho $N$, reportamos o tempo mediano em segundos (de 3 execuções válidas, descartando a primeira) e a razão $R = \frac{T(2N)}{T(N)}$ entre passos consecutivos de dobragem.

| $N$ | BST Aleatório (s) | Razão BST Ale. | BST Ordenado (s) | Razão BST Ord. | AVL Aleatório (s) | Razão AVL Ale. | AVL Ordenado (s) | Razão AVL Ord. |
|---|---|---|---|---|---|---|---|---|
| 1000 | 0.000433 | - | 0.011760 | - | 0.002312 | - | 0.002344 | - |
| 2000 | 0.000877 | 2.03 | 0.046135 | **3.92** | 0.005134 | 2.22 | 0.005090 | 2.17 |
| 4000 | 0.001956 | 2.23 | 0.181476 | **3.93** | 0.012026 | 2.34 | 0.011167 | 2.19 |
| 8000 | 0.005526 | 2.83 | 0.729837 | **4.02** | 0.028659 | 2.38 | 0.024406 | 2.19 |
| 16000 | 0.009819 | 1.78 | 2.971550 | **4.07** | 0.056185 | 1.96 | 0.055590 | 2.28 |

---

## Análise e Classes de Crescimento

### 1. BST com Entrada Ordenada — Classe Quadrática $O(N^2)$
* **Justificativa pelos números**: Ao dobrar o tamanho do problema de $N$ para $2N$, o tempo de inserção quadruplica de maneira consistente, apresentando uma razão experimental $R \approx 4.0$. Por exemplo, ao passar de 8.000 para 16.000 elementos, o tempo saltou de $0,729\text{s}$ para $2,971\text{s}$ ($R = 4.07$).
* **Explicação**: Inserir elementos em ordem crescente em uma BST desbalanceada faz com que cada novo nó seja inserido sempre à extrema direita, transformando a árvore em uma lista encadeada degenerada com altura $H = N$. A inserção do $i$-ésimo nó requer $i-1$ comparações, totalizando $\sum_{i=1}^{N} i = \frac{N(N-1)}{2}$ operações, ou seja, custo assintótico $O(N^2)$.

### 2. BST com Entrada Aleatória — Classe Quase-Linear $O(N \log N)$
* **Justificativa pelos números**: A razão média se mantém em torno de $R \approx 2.0 - 2.2$. Dobrar o tamanho da entrada faz com que o tempo total pouco mais que dobre.
* **Explicação**: Dados aleatórios distribuem as chaves de forma proporcional entre as subárvores esquerda e direita, mantendo a altura média da árvore em $H = O(\log N)$. Como cada uma das $N$ inserções exige $O(\log N)$ comparações, o tempo total acumulado resulta em $O(N \log N)$.

### 3. Árvore AVL (Aleatória e Ordenada) — Classe Quase-Linear $O(N \log N)$
* **Justificativa pelos números**: Em ambos os cenários (dados aleatórios ou estritamente ordenados), a razão experimental permaneceu estável em $R \approx 2.17 - 2.38$.
* **Explicação**: A AVL garante que o Fator de Balanceamento $FB \in \{-1, 0, +1\}$ seja mantido por meio de rotações pontuais de custo $O(1)$. Mesmo sob o pior caso de dados ordenados, a altura da árvore nunca excede $1,44 \log_2 N$. Assim, a inserção individual é rigorosamente delimitada por $O(\log N)$, resultando em tempo total de $O(N \log N)$ independente da organização da entrada.

---

## Como Executar o Projeto

1. **Requisitos**: Python 3.8+ e a biblioteca `matplotlib`.
   ```cmd
   pip install matplotlib

2. Rodar as Medições:

python src/benchmark.py

3. Gerar o gráfico:

python src/gerar_grafico.py

---

**3. Conteúdo Completo para o `DIARIO.md`**

Copie o texto abaixo e cole no seu arquivo `DIARIO.md`:

```markdown
# Diário de Bordo do Experimento

## Expectativas Iniciais (Antes das Medições)

Antes da coleta de dados, a hipótese teórica formulada foi:
1. Em entradas aleatórias, BST e AVL teriam desempenhos muito próximos, embora a AVL pudesse ser ligeiramente mais lenta devido ao *overhead* de cálculo do fator de balanceamento e rotações.
2. Em entradas ordenadas, a BST apresentaria um gargalo grave de desempenho, enquanto a AVL manteria tempo de execução eficiente devido às rotações de rebalanceamento $O(1)$.

---

## Obstáculos e Problemas Encontrados

1. **Incompatibilidade de Comandos de Terminal**:
   * *O que deu errado*: A primeira tentativa de criar a estrutura de diretórios utilizando `mkdir -p` e `touch` falhou no Prompt de Comando (CMD) do Windows.
   * *Solução*: Ajustou-se o fluxo utilizando os comandos nativos do Windows (`type nul > arquivo`).

2. **Limite de Recursão e Estouro de Pilha**:
   * *O que deu errado*: A implementação inicial da BST utilizando algoritmos recursivos provocou erro de *RecursionError* para entradas ordenadas grandes, pois a pilha de execução atingia profundidade $N$.
   * *Solução*: Refatorou-se o algoritmo de inserção da BST para utilizar um laço iterativo (`while`), garantindo execução estável em memória constante para a pilha.

3. **Importação de Módulos no Python**:
   * *O que deu errado*: O script de benchmark disparou o erro `ImportError: cannot import name 'BST'` ao tentar carregar a classe do diretório `src/`.
   * *Solução*: Adicionou-se a manipulação explícita do `sys.path` para localizar a pasta dos arquivos-fonte do projeto.

---

## Lições Aprendidas e Conclusão

* **A Importância da Razão $T(2N)/T(N)$**: A análise isolada do tempo em segundos não revela a verdadeira complexidade. Constatar a razão quadruplicando ($R \approx 4.0$) comprovou graficamente e empiricamente a degradação para a classe $O(N^2)$.
* **Estrutura Autobalanceada na Prática**: A AVL provou ser imune à degradação por ordem de entrada, apresentando desempenho virtualmente idêntico tanto para dados aleatórios quanto para dados ordenados.