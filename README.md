***Serviço Bancário Simulado***
Este script em Python é uma aplicação simples de terminal para simular operações bancárias. O usuário pode realizar saques, depósitos, visualizar o extrato e encerrar a sessão.

**Funcionalidades**

Saque: Permite retirar um valor do saldo disponível, respeitando um limite diário e o número máximo de saques permitidos.
Extrato: Exibe o extrato das movimentações realizadas e o saldo atual.
Depósito: Adiciona um valor ao saldo da conta.
Sair: Encerra a aplicação.

**Variáveis Principais**

menu: Controla a opção escolhida no menu.
saldo: Saldo disponível para operações.
limite: Limite máximo por saque (R$ 500).
extrato: Armazena o histórico de transações realizadas.
numero_saques: Conta o número de saques realizados no dia.
LIMITE_SAQUES: Limite máximo de saques permitidos por dia (3).

*Funcionamento*

1. Menu Inicial
No início, o usuário é recebido com um menu que apresenta as opções abaixo: