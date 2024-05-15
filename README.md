# Sistema_bancario
Esse projeto foi desenvolvido por um desafio do bootcamp da DIO.

❤️💻Descrição do Projeto: Sistema Bancário Simples em Python💻❤️

O projeto consiste em desenvolver um sistema bancário simples em Python que permite realizar operações básicas como depósito, saque e visualização de extrato. O sistema é projetado para atender a um único usuário e é executado no console.

Funcionalidades:

Depósito: O usuário pode depositar valores em sua conta bancária. O sistema valida se o valor é positivo e realiza o depósito, atualizando o saldo da conta. Cada depósito é registrado e exibido no extrato.

Saque: O usuário pode realizar saques em sua conta bancária. Existem algumas regras para saques: apenas 3 saques por dia são permitidos, com um limite máximo de R$500 por saque. O sistema verifica se as condições são atendidas antes de processar o saque. Cada saque é registrado e exibido no extrato.

Visualização de Extrato: O usuário pode visualizar o extrato de sua conta bancária, que inclui todos os depósitos e saques realizados, além do saldo atual da conta. Se não houver movimentações na conta, uma mensagem apropriada é exibida.

Implementação:

O sistema é implementado usando classes em Python. A classe Transacao é utilizada para representar cada transação realizada na conta, incluindo o tipo (depósito ou saque) e o valor. A classe ContaBancaria representa a conta bancária do usuário, armazenando informações como nome, saldo, depósitos e saques. Métodos são implementados para realizar as operações de depósito, saque e visualização de extrato, juntamente com a formatação adequada dos valores em moeda brasileira (R$XXX.XX).

Interatividade com o Usuário:

Para interagir com o usuário, é implementado um menu simples no console, onde o usuário pode escolher entre depositar, sacar, visualizar extrato ou sair do sistema. Dependendo da escolha do usuário, ele será solicitado a fornecer o valor para depósito ou saque. Após cada operação, o sistema fornece feedback sobre o resultado da operação.

Conclusão:

O sistema bancário desenvolvido em Python oferece uma maneira simples e intuitiva para os usuários gerenciarem suas contas bancárias, permitindo realizar operações comuns de forma eficiente e segura. Este projeto serve como uma base sólida para implementações mais complexas e pode ser expandido com recursos adicionais, como autenticação de usuário, persistência de dados, entre outros.






