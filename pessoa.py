from conta import Conta


class Pessoa:

    def __init__(self, id, salario, locs, preferencia):
        self.id = id
        self.salario = salario
        self.conta = Conta(id, salario)
        self.x, self.y = locs
        self.preferencia = preferencia
        self.mercado = None

    def escolhe_mercado(self, mercados):
        if self.preferencia == 'custo':
            # Verifica os custos
            custos = []
            for mercado in mercados:
                custos.append(mercado.custo)

            # Separa todos os mercados com custo mínimo para tomar escolha por distância
            aux = []
            menor = min(custos)
            for i in range(len(custos)):
                if custos[i] == menor:
                    aux.append(mercados[i])
            mercados = aux

        elif self.preferencia == 'cashback':
            # Verifica os cashbacks
            cashbacks = []
            for mercado in mercados:
                cashbacks.append(mercado.valor_bonus)

            # Separa todos os mercados com valor de cashback máximo para tomar escolha por distância
            aux = []
            maior = max(cashbacks)
            for i in range(len(cashbacks)):
                if cashbacks[i] == maior:
                    aux.append(mercados[i])
            mercados = aux

        distancias = []
        for mercado in mercados:
            distancias.append(((mercado.x - self.x) ** 2 + (mercado.y - self.y) ** 2) ** .5)
        self.mercado = mercados[distancias.index(min(distancias))]

    def __str__(self):
        return str(self.id)
