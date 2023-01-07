def soma_lista_iterativo(lista):
    soma = 0
    for i in range(len(lista)):
        soma += lista[i]
    return soma

def soma_lista(lista):
    if len(lista) > 1:
        # print(lista)
        return lista[0] + soma_lista(lista[1:])
    else:
        return lista[0]
