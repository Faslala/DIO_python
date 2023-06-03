import textwrap

def menu():
    menu = '''

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova Conta
    [lc] Listar Contas
    [nu] Novo Cliente
    [q] Sair

    => '''
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato,/):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("A operação não pode ser concluída porque o valor informado está incorreto!")
    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
   excedeu_saldo = valor > saldo
   excedeu_limite = valor > limite
   excedeu_saque = numero_saques > LIMITE_SAQUES

   if excedeu_saldo: 
       print("Saque não foi concluído porque o saldo está insuficiente!")
   elif excedeu_limite: 
       print("Saque não foi concluído porque o valor do saque excedeu o limite permitido!")
   elif excedeu_saque: 
       print("Saque não foi concluído porque o número máximo de saque excedeu o limite permitido!")
   elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("\n Saque realizado com sucesso!")
   else:
        print("A operação não pode ser concluída porque o valor informado está incorreto!") 
   
   return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n -^@^- _____INÍCIO DO EXTRATO_____ -^@^- \n")
    print("Não foram realizadas nenhuma movimentação até o momento!" if not extrato else extrato)
    print(f"\n Saldo: R$ {saldo:.2f}")
    print("\n -^@^- _____FIM DO EXTRATO_____ -^@^-")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Esse usuário já existe com o CPF informado!")
        return
    
    nome = input("Informe o nome completo: ")
    data_de_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco: input("Informe o endereço completo: ")

    usuarios.append({"nome": nome, "data_nascimento": data_de_nascimento, "cpf": cpf, "endereco": endereco})
    print("Usuário criado com sucesso!")
    
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nConta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\n Usuário não encontrado, fluxo de criação de conta encerrado!")
        
def listar_contas(contas):
    for contas in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """

        print("-" * 50)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)
   
        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e": 
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao =="nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q": 
            break

        else:
            print("Favor digitar uma opção válida!")

main()
