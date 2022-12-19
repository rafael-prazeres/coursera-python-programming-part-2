def letra_e_vogal(letra):
    return letra.lower() == "a" or \
    letra.lower() == "e" or \
    letra.lower() == "i" or \
    letra.lower() == "o" or \
    letra.lower() == "u"
    
def conta_letras(frase, contar="vogais"):
    
    qtd_letras = 0
    frase = frase.strip()
    frase = frase.replace(" ","")
    
    if contar == "consoantes":
        for i in range(len(frase)):
            if ord(frase[i].lower()) > 96 and \
               ord(frase[i].lower()) < 123 and \
               not letra_e_vogal(frase[i]):
                qtd_letras += 1
            
    elif contar == "vogais":
        for i in range(len(frase)):
            if letra_e_vogal(frase[i]):
                qtd_letras += 1
    return qtd_letras

def testa_conta_letras():
    if conta_letras('programamos em python') == 6:
        print("Passou no primeiro teste.")
    # deve devolver 6

    if conta_letras('programamos em python', contar="vogais") == 6:
        print("Passou no segundo teste.")
    # deve devolver 6

    if conta_letras('programamos em python', contar="consoantes") == 13:
        print("Passou no terceiro teste.")
    # deve devolver 13
