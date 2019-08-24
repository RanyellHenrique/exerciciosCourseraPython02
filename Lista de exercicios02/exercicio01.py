def maiusculas(frase):
    string = ''
    for n in range(len(frase)):
        if 90 >= ord(frase[n]) >= 65 :
            string = string + frase[n]

    return string
