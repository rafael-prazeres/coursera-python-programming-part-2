def maiusculas(frase):
    ASCII_A = 65
    ASCII_Z = 90
    maiusculas = ""
    for i in range(len(frase)):
        if ord(frase[i]) > ASCII_A and ord(frase[i]) < ASCII_Z:
            maiusculas += frase[i]
    return maiusculas

def testa_maiusculas():
    if maiusculas('Programamos em python 2?') == "P":
        print("Passou no primeiro teste.")
    # deve devolver 'P'

    if maiusculas('Programamos em Python 3.') == "PP":
        print("Passou no segundo teste.")
    # deve devolver 'PP'

    if maiusculas('PrOgRaMaMoS em python!') == "PORMMS":
        print("Passou no terceiro teste.")
    # deve devolver 'PORMMS'
