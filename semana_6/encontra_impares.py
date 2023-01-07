def encontra_impares_iterativo(lista):
    impares = []
    for i in range(len(lista)):
        if lista[i]%2 != 0:
            impares.append(lista[i])
    return impares

def encontra_impares(lista):
    if len(lista) == 0:
        return lista
    lista_retornada = encontra_impares(lista[1:])
    if lista[0] % 2 == 0:
        return lista_retornada
    else:
        nova_lista = [lista[0]]
        nova_lista.extend(lista_retornada)
        return nova_lista
