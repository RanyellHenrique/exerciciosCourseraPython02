def sao_multiplicaveis(m1, m2):
    coluna1 = len(m1)
    coluna2 = len(m2)
    linha1 = len(m1[0])
    linha2 = len(m2[0])
    if coluna1 == linha2 or coluna2 == linha1:
        return True
    return False
