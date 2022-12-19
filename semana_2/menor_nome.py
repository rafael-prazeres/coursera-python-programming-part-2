def menor_nome(lista_de_nomes):
    mais_curto = lista_de_nomes[0].strip()
    for i in range(1,len(lista_de_nomes)):
        if len(mais_curto) > len(lista_de_nomes[i].strip()):
            mais_curto = lista_de_nomes[i].strip()
    return mais_curto.capitalize()

def testa_menor_nome():
    if menor_nome(['maria', 'josé', 'PAULO', 'Catarina']) == "José":
        print("Passou no primeiro teste.")
    else:
        print("Não passou no primeiro teste. O nome mais curto capitalizado é José")
    if menor_nome(['maria', ' josé  ', '  PAULO', 'Catarina  ']) == "José":
        print("Passou no segundo teste.")
    else:
        print("Não passou no primeiro teste. O nome mais curto capitalizado é José")
    if menor_nome(['Bárbara', 'JOSÉ  ', 'Bill']) == "José":
        print("Passou no terceiro teste.")
    else:
        print("Não passou no primeiro teste. O nome mais curto capitalizado é José")
