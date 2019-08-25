import random

def lista_grande(n):
    lista = []
    for i in range(n):
        lista.append(random.randrange(n + 100))
    return lista

def ordena(lista):
    for i in range(len(lista) - 1):
        anterior = i
        for j in range(i+1, len(lista)):
            if lista[anterior] > lista[j]:
                anterior = j
        lista[i], lista[anterior] = lista[anterior], lista[i]
    return lista
