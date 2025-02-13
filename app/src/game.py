import random
from typing import List
from app.src.property import Propriedade
from app.src.player import Jogador

class Jogo:
    def __init__(self, jogadores: List[Jogador], propriedades: List[Propriedade]):
        self.jogadores = jogadores
        self.propriedades = propriedades
        random.shuffle(self.jogadores)
        self.rodada = 0
        self.maximo_rodadas = 1000

    def executar(self):
        while not self.esta_finalizado():
            self.jogar_rodada()
            self.rodada += 1
            if self.rodada >= self.maximo_rodadas:
                break
        return self.determinar_vencedor()

    def jogar_rodada(self):
        for jogador in self.jogadores:
            if not jogador.ativo:
                continue
            passos = self.rolar_dado()
            jogador.mover(passos, len(self.propriedades))
            propriedade_atual = self.propriedades[jogador.posicao]
            if propriedade_atual.proprietario is not None and propriedade_atual.proprietario != jogador:
                jogador.pagar_aluguel(propriedade_atual.aluguel, propriedade_atual.proprietario)
            if jogador.saldo < 0:
                self.remover_jogador(jogador)
                continue
            if propriedade_atual.proprietario is None and jogador.ativo:
                if jogador.decidir_compra(propriedade_atual):
                    jogador.comprar_propriedade(propriedade_atual)
                    if jogador.saldo < 0:
                        self.remover_jogador(jogador)
            if self.verificar_apenas_um_jogador_restante():
                return

    def rolar_dado(self) -> int:
        return random.randint(1, 6)

    def remover_jogador(self, jogador: Jogador):
        jogador.ativo = False
        for p in jogador.propriedades:
            p.resetar_proprietario()
        jogador.propriedades.clear()

    def verificar_apenas_um_jogador_restante(self) -> bool:
        ativos = [j for j in self.jogadores if j.ativo]
        return len(ativos) == 1

    def esta_finalizado(self) -> bool:
        return self.verificar_apenas_um_jogador_restante() or all(not j.ativo for j in self.jogadores)

    def determinar_vencedor(self):
        ativos = [j for j in self.jogadores if j.ativo]
        if len(ativos) == 1:
            vencedor = ativos[0]
        else:
            ordenados = sorted(
                self.jogadores,
                key=lambda j: (j.saldo, -self.jogadores.index(j)),
                reverse=True
            )
            vencedor = ordenados[0]
        jogadores_ordenados = sorted(
            self.jogadores,
            key=lambda j: j.saldo,
            reverse=True
        )
        return {
            "vencedor": vencedor.nome,
            "jogadores": [j.nome for j in jogadores_ordenados]
        }
