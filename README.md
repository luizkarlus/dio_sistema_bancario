# Sistema Bancário em Python

Este é um projeto simples de sistema bancário desenvolvido em Python como parte de um desafio. O programa permite ao usuário realizar saques, depósitos, consultar extrato e encerrar a sessão.

## **Funcionalidades**

- **Saque:** O usuário pode realizar saques respeitando:
  - O saldo disponível.
  - O limite diário de saque de R$ 500,00.
  - Limite de 3 saques diários.

- **Depósito:** Permite adicionar saldo à conta.

- **Extrato:** Exibe as movimentações realizadas e o saldo atual.

- **Sair:** Encerra o programa.

---

## **Como Executar**

1. Certifique-se de ter o Python instalado em sua máquina.
2. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/sistema-bancario.git
3. Navegue até o diretório do projeto:
   ```bash
   cd sistema_bancario
4. Execute o script:
   ```bash
   python sistema_bancario.py

---

## **Estrutura do Código**
- O código utiliza um loop while para exibir um menu interativo até o usuário escolher opção "Sair".
- Cada operação (saque, depósito e extrato) possui suas próprias verificações e mensagens ao usuário.

---

## **Autor**
Luiz França