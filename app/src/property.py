class Propriedade:
    def __init__(self, nome: str, custo: int, aluguel: int):
        self.nome = nome
        self.custo = custo
        self.aluguel = aluguel
        self.proprietario = None

    def resetar_proprietario(self):
        self.proprietario = None
