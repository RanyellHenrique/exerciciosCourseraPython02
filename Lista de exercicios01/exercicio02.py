def dimensoes(m1, m2):
    linha1 = len(m1)
    coluna1 = len(m1[0])
    linha2 = len(m2)
    coluna2 = len(m2[0])
    if coluna1 == coluna2 and linha1 == linha2:
        return True
    return False
        
def soma_matrizes(m1, m2):
    if dimensoes(m1, m2) == False:
        resultado = dimensoes(m1, m2)
        return resultado
    soma = []
    for linha in range(len(m1)):
        linhas = []
        for coluna in range(len(m1[0])):
            soma_das_linhas = m1[linha][coluna] + m2[linha][coluna]
            linhas.append(soma_das_linhas)
        soma.append(linhas)
    return soma
