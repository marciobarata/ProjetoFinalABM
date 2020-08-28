import random

from pessoa import Pessoa
from mercado import Mercado

num_clientes = 200
num_mercados = 20
salario = 1045.00


class Simulacao:

    def __init__(self):
        self.clientes = list()
        self.mercados = list()

    def cria_agente(self):
        num_localizacoes = 2 * (num_clientes + num_mercados)
        localizacoes = []
        for i in range(num_localizacoes):
            localizacoes.append(random.randint(0, 100))

        for j in range(num_clientes):
            locs = localizacoes.pop(), localizacoes.pop()
            preferencia = random.choice(['distancia', 'custo', 'cashback'])
            self.clientes.append(Pessoa(j+1, salario, locs, preferencia))

        for k in range(num_mercados):
            locs = localizacoes.pop(), localizacoes.pop()
            self.mercados.append(Mercado(k+1, locs))

    def roda_modelo(self):
        data = {
            "distancia": 0,
            "cashback": 0,
            "custo": 0
        }

        for cliente in self.clientes:
            cliente.escolhe_mercado(self.mercados)
            data[cliente.preferencia] += 1

        preferencias = ['tipo,quantidade']
        for chave in data.keys(): # ['distancia', 'cashback', 'custo']
            print(chave, ': ', data[chave])
            preferencias.append('\n'+chave+','+str(data[chave]))

        # gravando dados sobre preferências
        gravar('preferencias.csv', preferencias)

        for cliente in self.clientes:
            cliente.mercado.nova_venda(cliente)

        valores = ["cliente, localizacao_cliente, mercado, localizacao_mercado, custo_mercado,bonus_mercado,"
                   "valor da compra,preferencia do cliente,saldo do cliente,divida do cliente, cashback utilizado"]
        for cliente in self.clientes:
            # Valor a ser registrado no arquivo
            valor = "\n" + str(cliente.id) + "," + str(cliente.x) + " " + str(cliente.y) + "," + \
                    str(cliente.mercado.id) + "," + str(cliente.mercado.x) + " " + str(cliente.mercado.y) + "," + \
                    str(cliente.mercado.custo) + "," + str(cliente.mercado.valor_bonus) + "," + \
                    str(cliente.conta.compras[0].valor) + "," + str(cliente.preferencia) + "," + \
                    str(cliente.conta.saldo) + "," + str(cliente.conta.divida) + "," + str(cliente.conta.bonus)
            valores.append(valor)

            print("-------------------------------")
            print("Cliente: ", cliente.id)
            print("Localização cliente:", cliente.x, cliente.y)
            print("Mercado:", cliente.mercado)
            print("Localização mercado:", cliente.mercado.x, cliente.mercado.y)
            custo = int(cliente.mercado.custo*100)
            print("Custo do mercado", custo,"%")
            print("Valor do bonus: ", cliente.mercado.valor_bonus)
            print("Valor da compra: ", cliente.conta.compras[0].valor)
            print("Preferencia: ", cliente.preferencia)
            print("Saldo: ", cliente.conta.saldo)
            print("Divida: ", cliente.conta.divida)
            print("Desconto: ", cliente.conta.bonus)
            print("-------------------------------")

        # gravando valores da simulação em um arquivo
        gravar('simulacao.csv', valores)


def gravar(arquivo, valores):
    with open(arquivo, 'w') as handler:
        handler.writelines(valores)


if __name__ == '__main__':
    minha_simulacao = Simulacao()
    minha_simulacao.cria_agente()
    minha_simulacao.roda_modelo()
