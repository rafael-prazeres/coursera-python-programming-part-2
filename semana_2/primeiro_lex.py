def primeiro_lex(lista_de_strings):
    menor_string = lista_de_strings[0]
    for i in range(1,len(lista_de_strings)):
        if lista_de_strings[i].lower() < menor_string.lower():
            menor_string = lista_de_strings[i]
    return menor_string

def testa_primeiro_lex():
    if primeiro_lex(['oĺá', 'A', 'a', 'casa']) == "A":
        print("Passou no primeiro teste.")
    else:
        print("Não passou no primeiro teste.")
    if primeiro_lex(['AAAAAA', 'b']) == "AAAAAA":
        print("Passou no segundo teste.")
    else:
        print("Não passou no segundo teste.")
