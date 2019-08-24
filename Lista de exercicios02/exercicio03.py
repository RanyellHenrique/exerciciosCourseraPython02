def conta_letras(frase, contar="vogais"):
    conta_letras = 0
    if contar == 'vogais':
        for letras in frase:
            if letras == 'a' or letras =='A' or letras == 'e' or letras == 'E' or letras == 'i' or letras == 'I' or letras == 'o' or letras == 'O' or letras == 'u' or letras == 'U':
                conta_letras += 1
        return conta_letras
    elif contar == 'consoantes':
        for letras in frase:
            if letras != 'a' and letras !='A' and letras != 'e' and letras != 'E' and letras != 'i' and letras != 'I' and letras != 'o' and letras != 'O' and letras != 'u' and letras != 'U' and letras != ' ':
                conta_letras += 1
        return conta_letras
