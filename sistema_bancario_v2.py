saldo = 2000
options = 0

while options != 4:
    options = int(
        input(
            "\nInforme uma opção: \n\n[1] Sacar \n[2] Extrato \n[3] Depositar \n[4] Sair \n\n"
        )
    )

    if options == 1:
        valor = int(input("Informe a quantia para o saque: "))
        if valor <= saldo:
            saldo -= valor
            print(f"\nSeu saque foi efetuado com sucesso! Seu saldo atual é R${saldo}")
        else:
            print(f"\nSaldo insuficiente! Seu saldo atual é R${saldo}")

    elif options == 2:
        print(f"\nSeu saldo atual é R${saldo}")

    elif options == 3:
        deposito = int(input("\nInforme o valor do deposito: "))
        saldo += deposito
        print(f"\nSeu deposito foi efetuado com sucesso! Seu saldo atual é R${saldo}")

    elif options == 4:
        print("\nSaindo...loading\n\n")
