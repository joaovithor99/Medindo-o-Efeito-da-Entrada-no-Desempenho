import time
import random
import statistics
import csv
import sys
import os

# Garante que o Python encontre os arquivos na pasta src
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from bst import BST
from avl import AVL

# Tamanhos que dobram a cada passo
TAMANHOS = [1000, 2000, 4000, 8000, 16000]
SEMENTE = 42

def medir_desempenho(estrutura_cls, dados):
    # Warmup (primeira execução descartada para aquecer cache/interpretador)
    est = estrutura_cls()
    for x in dados:
        est.inserir(x)
        
    tempos = []
    # 3 execuções válidas
    for _ in range(3):
        est = estrutura_cls()
        t0 = time.perf_counter()
        for x in dados:
            est.inserir(x)
        t1 = time.perf_counter()
        tempos.append(t1 - t0)
        
    return statistics.median(tempos)

def rodar_experimento():
    resultados = []

    for n in TAMANHOS:
        print(f"Coletando dados para N = {n}...")
        
        # Garante a mesma massa de dados para todas as iterações
        random.seed(SEMENTE)
        dados_rand = [random.randint(0, n * 10) for _ in range(n)]
        dados_ord = list(range(n))

        t_bst_rand = medir_desempenho(BST, dados_rand)
        t_bst_ord = medir_desempenho(BST, dados_ord)
        t_avl_rand = medir_desempenho(AVL, dados_rand)
        t_avl_ord = medir_desempenho(AVL, dados_ord)

        resultados.append({
            'n': n,
            'bst_aleatorio': t_bst_rand,
            'bst_ordenado': t_bst_ord,
            'avl_aleatorio': t_avl_rand,
            'avl_ordenado': t_avl_ord
        })
        
    return resultados

def salvar_csv(resultados, caminho='dados/resultados.csv'):
    colunas = ['n', 'bst_aleatorio', 'bst_ordenado', 'avl_aleatorio', 'avl_ordenado']
    with open(caminho, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=colunas)
        writer.writeheader()
        writer.writerows(resultados)

if __name__ == "__main__":
    dados_medidos = rodar_experimento()
    salvar_csv(dados_medidos)
    print("\nExecução concluída! Dados salvos em 'dados/resultados.csv'.")