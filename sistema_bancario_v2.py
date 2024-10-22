# Variáveis do desafio:
menu = 0
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
print("\n\nBem-vindo ao serviço bancario do Luiz França!")

# Início do script
while menu != 4:
    menu = int(input("\nInforme a opção desejada: \n\n[1] Sacar \n[2] Extrato \n[3] Depositar \n[4] Sair \n\nC:\\> "))

    if menu == 1:
        valor = float(input("\nInforme a quantia para o saque: \nR$ "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("\nSeu saldo é insuficiente. Verifique o seu extrato selecionando a opção 2 do menu: \n")
        elif excedeu_limite:
            print(f"\nPor motivos de segurança, o seu limite de saque diário é de R$ {limite:.2f}. \n")
        elif excedeu_saques:
            print("\nVocê excedeu o seu limite diário de saque. Tente novamente amanhã. \n")
        else:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("Saque efetuado com sucesso. Por favor, retire o seu dinheiro! \n")

    elif menu == 2:
        print("\n******** EXTRATO ********")
        print("\nNão foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSeu saldo atual é R$ {saldo:.2f}")
        print("\n********   FIM   ********")

    elif menu == 3:
        deposito = int(input("\nInforme o valor do deposito: \nR$ "))
        saldo += deposito
        print(f"\nSeu depósito foi efetuado com sucesso! Seu saldo atual é R$ {saldo:.2f} \n")

    elif menu == 4:
        print("Esta sessão está sendo encerrada!")
        import loading as loading
        print(loading)
