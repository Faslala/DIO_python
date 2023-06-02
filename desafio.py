menu = '''

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> '''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("A operação não pode ser concluída porque o valor informado está incorreto!")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = numero_saques > LIMITE_SAQUES

        if excedeu_saldo: print("Saque não foi concluído porque o saldo está insuficiente!")
        elif excedeu_limite: print("Saque não foi concluído porque o valor do saque excedeu o limite permitido!")
        elif excedeu_saque: print("Saque não foi concluído porque o número máximo de saque excedeu o limite permitido!")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("A operação não pode ser concluída porque o valor informado está incorreto!")

    elif opcao == "e":
        print("\n -^@^- _____INÍCIO DO EXTRATO_____ -^@^- \n")
        print("Não foram realizadas nenhuma movimentação até o momento!" if not extrato else extrato)
        print(f"\n Saldo: R$ {saldo:.2f}")
        print("\n -^@^- _____FIM DO EXTRATO_____ -^@^-")
    
    elif opcao == "q": break

    else:
        print("Favor digitar uma opção válida!")