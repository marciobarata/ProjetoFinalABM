import random

from compra import Compra


class Mercado:

    def __init__(self, id, locs):
        self.id = id
        self.valor_bonus = random.choice([0.0, 0.01, 0.02, 0.03]) # bônus do mercado
        self.x, self.y = locs
        self.custo = random.randint(80, 120)/100 # valor do custo a ser usado em porcentagem

    def nova_venda(self, cliente):
        id_compra = len(cliente.conta.compras)+1 # Id com base nas compras do cliente
        custo = cliente.salario*self.custo # custo da compra com base no custo do mercado
        cliente.conta.recebe_bonus(custo*self.valor_bonus) # armazena o valor de bônus
        custo -= custo*self.valor_bonus # custo final com base no bônus
        custo = float("%.2f" % custo)
        cliente.conta.retirada(custo) # retirada do saldo do cliente
        venda = Compra(id_compra, custo)
        cliente.conta.nova_compra(venda)

    def __str__(self):
        return str(self.id)
