def primeiro_lex(lista):
    primeira_palavra = lista[0]
    for i in range(len(lista)):
        if lista[i] < primeira_palavra:
            primeira_palavra = lista[i]
    return primeira_palavra
            
        
        
