# Sistema Bancário em Python

Este é um sistema bancário simples desenvolvido em Python, com funcionalidades básicas para saque, depósito e extrato. Ele também possui uma simulação divertida de encerramento de sessão com a importação de um módulo externo chamado **loading.py**.

---

## 📋 Funcionalidades

- **Saque**: Permite sacar dinheiro, respeitando o saldo, o limite de saque por operação e a quantidade máxima de saques diários.
- **Depósito**: Adiciona o valor informado ao saldo da conta.
- **Extrato**: Exibe o histórico de transações realizadas e o saldo atual.
- **Sair**: Encerra a sessão com uma mensagem personalizada utilizando o módulo **loading.py**.

---

## 🗂 Estrutura do Projeto


---

## 🚀 Como Executar

1. Certifique-se de ter o **Python 3.x** instalado na sua máquina.
2. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/sistema-bancario.git

cd sistema-bancario

python sistema_bancario.py

Bem-vindo ao serviço bancario do Luiz França!

Informe a opção desejada:

[1] Sacar 
[2] Extrato 
[3] Depositar 
[4] Sair 

C:\> 3
Informe o valor do deposito: 
R$ 1000

Seu deposito foi efetuado com sucesso! Seu saldo atual é R$ 1000.00 

C:\> 1
Informe a quantia para o saque: 
R$ 500

Saque efetuado com sucesso. Por favor, retire o seu dinheiro! 

C:\> 2
******** EXTRATO ********

Saque: R$ 500.00

Seu saldo atual é R$ 500.00

********   FIM   ********

C:\> 4
Esta sessão está sendo encerrada!
Loading...

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

print("Loading...")
