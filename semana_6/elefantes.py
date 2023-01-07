def incomodam(n):
    if n < 1:
        return ""
    else:
        return "incomodam " + incomodam(n - 1)

def elefantes(n):
    if n < 0:
        return ""
    elif n == 1:
        return "Um elefante incomoda muita gente\n"
    else:
        if n < 3:
            saida = elefantes(n-1) + str(n) + " elefantes " + incomodam(n) + "muito mais"
        else:
            saida = elefantes(n-1) + "\n" + str(n-1) + " elefantes incomodam muita gente\n" + str(n) + " elefantes " + incomodam(n) + "muito mais"
        return saida
