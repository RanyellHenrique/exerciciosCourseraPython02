def menor_nome(nomes):
    resultado = nomes[0].strip()
    tamanho = len(nomes[0].strip())
    for nome in nomes:
        nome = nome.strip()
        if len(nome) < tamanho:
            tamanho = len(nome)
            resultado = nome
    return resultado.capitalize()
