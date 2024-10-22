Serviço Bancário Simulado
Este script em Python é uma aplicação simples de terminal para simular operações bancárias. O usuário pode realizar saques, depósitos, visualizar o extrato e encerrar a sessão.

Funcionalidades
Saque: Permite retirar um valor do saldo disponível, respeitando um limite diário e o número máximo de saques permitidos.
Extrato: Exibe o extrato das movimentações realizadas e o saldo atual.
Depósito: Adiciona um valor ao saldo da conta.
Sair: Encerra a aplicação.
Variáveis Principais
menu: Controla a opção escolhida no menu.
saldo: Saldo disponível para operações.
limite: Limite máximo por saque (R$ 500).
extrato: Armazena o histórico de transações realizadas.
numero_saques: Conta o número de saques realizados no dia.
LIMITE_SAQUES: Limite máximo de saques permitidos por dia (3).
Funcionamento
1. Menu Inicial
No início, o usuário é recebido com um menu que apresenta as opções abaixo:

csharp
Copiar código
[1] Sacar
[2] Extrato
[3] Depositar
[4] Sair
O usuário deve inserir o número correspondente à operação desejada.

2. Regras de Saque
O valor do saque não pode exceder o saldo disponível.
O valor do saque deve ser menor ou igual ao limite diário (R$ 500).
O número máximo de saques permitidos por dia é 3.
3. Exibindo o Extrato
Se não houver movimentações, uma mensagem informativa é exibida.
O extrato apresenta todas as transações e o saldo atualizado.
4. Depósito
O usuário pode depositar valores para incrementar o saldo.
Após o depósito, o saldo atualizado é exibido.
5. Encerrando a Sessão
Quando o usuário escolhe a opção "4 - Sair", a aplicação é encerrada e uma mensagem final é exibida.
Exemplo de Uso
less
Copiar código
Bem-vindo ao serviço bancario do Luiz França!

Informe a opção desejada:

[1] Sacar
[2] Extrato
[3] Depositar
[4] Sair

C:\> 1
Informe a quantia para o saque:
R$ 100

Saque efetuado com sucesso. Por favor, retire o seu dinheiro!
Estrutura do Código
Inicialização das variáveis: As variáveis são declaradas no início para armazenar informações como saldo, extrato e número de saques.
Loop principal: O script executa continuamente até que o usuário escolha a opção "Sair" (opção 4).
Condições de validação: As operações verificam se há saldo suficiente, se o limite foi atingido ou se o número máximo de saques foi realizado.
Importação do loading: No momento de encerrar, o script importa um módulo chamado loading (é necessário garantir que este módulo esteja disponível).
Requisitos
Python 3.x instalado na máquina.
Possíveis Melhorias
Implementar validação para evitar a inserção de valores inválidos.
Utilizar try-except para lidar com erros de entrada.
Permitir depósitos com valores decimais.
Adicionar persistência para salvar o saldo e extrato em arquivos.
Autor
Luiz França
Especialista em Infraestrutura e Sistemas
