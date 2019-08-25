def ordenada(lista):
    anterior = lista[0]
    for i in range(len(lista)):
        if anterior < lista[i]:
            anterior = lista[i]
        elif anterior > lista[i]:
            return False
    return True
            
