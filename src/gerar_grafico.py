import csv
import matplotlib.pyplot as plt

# Leitura dos dados medidos
n_vals = []
bst_rand, bst_ord = [], []
avl_rand, avl_ord = [], []

with open('dados/resultados.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        n_vals.append(int(row['n']))
        bst_rand.append(float(row['bst_aleatorio']))
        bst_ord.append(float(row['bst_ordenado']))
        avl_rand.append(float(row['avl_aleatorio']))
        avl_ord.append(float(row['avl_ordenado']))

# Configuração do gráfico
plt.figure(figsize=(10, 6))
plt.plot(n_vals, bst_rand, marker='o', label='BST (Aleatório)', linewidth=2)
plt.plot(n_vals, bst_ord, marker='s', color='red', label='BST (Ordenado - Pior Caso)', linewidth=2)
plt.plot(n_vals, avl_rand, marker='^', label='AVL (Aleatório)', linewidth=2)
plt.plot(n_vals, avl_ord, marker='d', label='AVL (Ordenado)', linewidth=2)

plt.title('Comparativo de Tempo de Inserção: BST vs. Árvore AVL', fontsize=14, fontweight='bold')
plt.xlabel('Tamanho da Entrada (N)', fontsize=12)
plt.ylabel('Tempo Mediano de Execução (s)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=11)
plt.tight_layout()

plt.savefig('graficos/desempenho.png', dpi=300)
print("Gráfico salvo com sucesso em 'graficos/desempenho.png'!")