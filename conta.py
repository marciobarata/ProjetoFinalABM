import random


class Conta:
    def __init__(self, id, saldo=0.0):
        self.id = id
        self.saldo = saldo # saldo inicialmente começará com zero
        self.taxa_cheque = random.choice([0.03, 0.05, 0.07]) #taxas de cheques de 3%,5%,7%.
        self.compras = list()
        self.divida = 0
        self.bonus = 0

    def deposito(self, quantia):
        self.saldo += quantia #adicionar uma quantia a conta, no caso seria o valor do salário mínimo.
        return self.saldo

    def retirada(self, quantia):
        if quantia > self.saldo:
            diferenca = self.saldo - quantia
            self.divida = diferenca*self.taxa_cheque
            self.divida = float("%.2f" % self.divida) #limitando o número a 2 casas decimais.
        self.saldo -= quantia
        self.saldo = float("%.2f" % self.saldo)
        return self.saldo

    def nova_compra(self, compra):
        self.compras.append(compra)

    def recebe_bonus(self, valor):
        self.bonus = float("%.2f" % valor)

    def __str__(self):
        return self.id
