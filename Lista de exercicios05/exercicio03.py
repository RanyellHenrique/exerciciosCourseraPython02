def insertion_sort(lista):
    ordenacao = False
    while not ordenacao:
        ordenacao = True
        for i in range(len(lista) - 1):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
                ordenacao = False
    return lista
