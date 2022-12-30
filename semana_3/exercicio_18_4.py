def main():
    # modifique o codigo para incluir o calculo de DE
    # e verifique se o resultado é diferente de ED usando
    # soma de reais e soma de racionais.

    n = 50
    soma_ed = 0
    soma_ed_rac = Racional()

    for i in range(1, n+1):
        soma_ed = soma_ed + 1/i
        soma_ed_rac = soma_ed_rac + Racional(1, i)

    print("Soma ED:          ", soma_ed)
    print("Soma ED racional: ", soma_ed_rac)
    print("                = ", soma_ed_rac.num/soma_ed_rac.den)

    soma_de = 0
    soma_de_rac = Racional()
    for i in range(1, n+1):
        soma_de = soma_de + 1/(n+1-i)
        soma_de_rac = soma_de_rac + Racional(1, n+1-i)

    print("Soma DE:          ", soma_de)
    print("Soma DE racional: ", soma_de_rac)
    print("                = ", soma_de_rac.num/soma_de_rac.den)


def mdc(a, b):
    ''' (int, int) -> int
        recebe dois inteiros diferentes de zero e retorna o maximo
        divisor comum entre a e b'''
    if b == 0: return a
    if a == 0: return b
    while a%b != 0:
        a, b = b, a%b
    return b

class Racional:
    def __init__(self, n=0, d=1):
        div = mdc(n, d)
        self.num = n//div
        self.den = d//div

    def __str__(self):
        return "%d/%d"%(self.num, self.den)

    def __add__(self, other):
        n = self.num * other.den + self.den * other.num
        d = self.den * other.den
        return Racional(n, d)

    # escreva aqui o seu codigo para os metodos
    # __truediv__
    # __mul__
    # __sub__
    # e ao menos um teste para cada metodo

main()
