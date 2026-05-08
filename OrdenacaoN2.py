"""
Arquivo Python para inserção de códigos de algoritmos de ordenação O(n^2)
autor: Arthur Souza
"""

# Algoritmo N^2 escolhido: bubbleSort
def bubbleSort(lista):
    n = len(lista)
    while n > 1:
        i = 1
        while i < n:
            if lista[i] < lista[i - 1]:
                temp = lista[i]
                lista[i] = lista[i - 1]
                lista[i - 1] = temp
            i += 1
        n -= 1
    return lista

def bubbleSortRec(lista, n = 0):
    if n == 0:
        n = len(lista)
    if n <= 1:
        return lista
    else:
        i = 1
        while i < n:
            if lista[i] < lista[i - 1]:
                temp = lista[i]
                lista[i] = lista[i - 1]
                lista[i - 1] = temp
            i += 1
        return bubbleSortRec(lista, n-1)
