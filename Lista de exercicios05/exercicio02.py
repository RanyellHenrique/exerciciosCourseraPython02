def bubble_sort(lista):
    ordenado = False
    while  not ordenado:
        ordenado = True
        for i in range(len(lista) - 1):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                ordenado = False
                print(lista)
    return lista
    
