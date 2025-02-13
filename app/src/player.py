import random

class Jogador:
    def __init__(self, nome: str, saldo_inicial: int = 300):
        self.nome = nome
        self.saldo = saldo_inicial
        self.propriedades = []
        self.posicao = 0
        self.ativo = True

    def mover(self, passos: int, tamanho_tabuleiro: int):
        posicao_antiga = self.posicao
        self.posicao = (self.posicao + passos) % tamanho_tabuleiro
        if posicao_antiga + passos >= tamanho_tabuleiro:
            self.saldo += 100

    def pagar_aluguel(self, valor: int, dono):
        self.saldo -= valor
        dono.saldo += valor

    def comprar_propriedade(self, propriedade):
        self.saldo -= propriedade.custo
        propriedade.proprietario = self
        self.propriedades.append(propriedade)

    def pode_comprar(self, propriedade) -> bool:
        raise NotImplementedError("Método deve ser sobrescrito.")

    def decidir_compra(self, propriedade) -> bool:
        if propriedade.proprietario is None and self.saldo >= propriedade.custo:
            return self.pode_comprar(propriedade)
        return False

class JogadorImpulsivo(Jogador):
    def pode_comprar(self, propriedade) -> bool:
        return True

class JogadorExigente(Jogador):
    def pode_comprar(self, propriedade) -> bool:
        return propriedade.aluguel > 50

class JogadorCauteloso(Jogador):
    def pode_comprar(self, propriedade) -> bool:
        return (self.saldo - propriedade.custo) >= 80

class JogadorAleatorio(Jogador):
    def pode_comprar(self, propriedade) -> bool:
        return random.random() < 0.5
