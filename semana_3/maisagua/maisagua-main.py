from simulador2 import Simulador2

def main():
    # cria um objeto Simulador2 usando uma semente
    semente = int(input("Semente: "))
    jogo  = Simulador2(semente)
    fim = False

    # cabecalho de inicio da simulacao
    print("--------------------------------")
    print("Início da simulação\n")
    print("Em cada iteração as opções possíveis são: ")
    print("    0 para abandonar")
    print("    1 para depositar no recipiente 1")
    print("    2 para depositar no recipiente 2")
    print("    3 para depositar no recipiente 3")
    print("    4 para descartar a quantidade de água\n")

    while not fim:
        jogo.sorteia()
        escolha = int(input("    Opção desejada: "))

        if escolha == 0:
            fim = True
        elif escolha == 4:
            fim = jogo.descarta()
        else:
            fim = jogo.deposita(escolha)

    jogo.finaliza()

main()
