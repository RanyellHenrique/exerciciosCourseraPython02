def busca(lista, elemento):
    maior = len(lista) - 1
    menor = 0
    while menor <= maior:
        meio = (maior + menor)//2
        print(meio)
        if elemento == lista[meio]:
            return meio
        elif elemento < lista[meio]:
            maior = meio - 1
        else:
            menor = meio + 1
    return False
            
    
