from simulador import Simulador

def main():
    semente = int(input("Digite a semente para gerar numeros pseudo-aleatorios: "))
    jogo = Simulador(semente)

    fim = False
    while not fim:
        jogo.sorteia()
        opcao = input("Deseja utilizar o volume sorteado? (s/n): ")
        if opcao == 's':
            fim = jogo.deposita()  # retorna True caso o balde fique cheio
        else:
            opcao = input("Deseja sortear outro volume? (s/n): ")
            if opcao == 's':
                continue
            else:
                fim = True
    jogo.finaliza()

main()
