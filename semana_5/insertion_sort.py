def insertion_sort(lista):
    novo = 2
    while novo <= len(lista):
        for i in range(1,len(lista[:novo])):
            if lista[novo - i] < lista[novo - i - 1]:
                lista[novo - i], lista[novo - i - 1] = lista[novo - i - 1], lista[novo - i]
            else:
                break
        novo += 1
    return lista
