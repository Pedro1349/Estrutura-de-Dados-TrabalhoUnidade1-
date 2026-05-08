"""
Arquivo Python para inserção de códigos de algoritmos de ordenação O(n*Log(n))
autor: Arthur Souza
"""

def trocarPosicao(lista, indiceI, indiceJ):
    temp = lista[indiceJ]
    lista[indiceJ] = lista[indiceI]
    lista[indiceI] = temp

def particao(lista, esquerda, direita):
    pivot = lista [esquerda]
    fronteira = esquerda
    for i in range (esquerda+1, direita+1):
        if(lista[i] <= pivot):
            fronteira += 1
            trocarPosicao(lista, i, fronteira)
    trocarPosicao(lista, esquerda, fronteira)

# Algoritmo Nlog escolhido: Quick Sort
def quickSortIt(lista):
    stack = []

    # adiciona intervalo inicial
    stack.append((0, len(lista) - 1))

    while stack:
        esquerda, direita = stack.pop()
        if esquerda < direita:

            indexPivot = particao(lista, esquerda, direita)
            stack.append((esquerda, indexPivot - 1))
            stack.append((indexPivot + 1, direita))
    return lista

def quickSort (lista, esquerda, direita):
    if (esquerda < direita):
        indexPivot = particao(lista, esquerda, direita)
        quickSort(lista, esquerda, indexPivot - 1)
        quickSort(lista, indexPivot+1,direita)