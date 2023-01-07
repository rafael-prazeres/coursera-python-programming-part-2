def acha(seq, x):
    for i in range(len(seq)):
        if seq[i] == x:
            return i
    return None

def main():
    seq = []
    opcao = 's'
    i = 1
    while opcao == 's':
        elemento = int(input("Informe o {}º elemento da sequência: ".format(i)))
        seq.append(elemento)
        opcao = input("Deseja incluir mais elementos na sequência (s/n)? ")
        i += 1

    seq_sem_repeticoes = []

    for i in range(len(seq)):
        if acha(seq_sem_repeticoes, seq[i]) == None:
            seq_sem_repeticoes.append(seq[i])

    print(seq_sem_repeticoes)

main()
