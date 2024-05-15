class Transacao:
    def __init__(self, tipo, valor):
        self.tipo = tipo
        self.valor = valor


class ContaBancaria:
    def __init__(self, nome):
        self.nome = nome
        self.saldo = 0
        self.depositos = []
        self.saques = []
        self.saques_feitos = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.depositos.append(Transacao("Depósito", valor))
            print(f'Depósito de {self.formatar_valor(valor)} realizado. Novo saldo: {self.formatar_valor(self.saldo)}')
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if self.saques_feitos < 3 and valor <= 500 and valor <= self.saldo:
            self.saldo -= valor
            self.saques.append(Transacao("Saque", valor))
            self.saques_feitos += 1
            print(f'Saque de {self.formatar_valor(valor)} realizado. Novo saldo: {self.formatar_valor(self.saldo)}')
        elif self.saques_feitos >= 3:
            print("Limite de saques diários excedido.")
        elif valor > 500:
            print("Valor máximo por saque é de R$500.")
        else:
            print("Saldo insuficiente para saque.")

    def extrato(self):
        if not self.depositos and not self.saques:
            print("Não foram realizadas movimentações.")
        else:
            print(f'Extrato da conta de {self.nome}:')
            for deposito in self.depositos:
                print(f'Depósito: {self.formatar_valor(deposito.valor)}')
            for saque in self.saques:
                print(f'Saque: {self.formatar_valor(saque.valor)}')
            print(f'Saldo atual: {self.formatar_valor(self.saldo)}')

    @staticmethod
    def formatar_valor(valor):
        return f'R${valor:.2f}'


# Função para interagir com o usuário
def menu_conta(conta):
    while True:
        print("\nO que você deseja fazer?")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Ver Extrato")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            valor = float(input("Digite o valor a ser depositado: "))
            conta.depositar(valor)
        elif escolha == "2":
            valor = float(input("Digite o valor a ser sacado: "))
            conta.sacar(valor)
        elif escolha == "3":
            conta.extrato()
        elif escolha == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


