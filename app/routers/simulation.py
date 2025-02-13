
from fastapi import APIRouter
from app.src.game import Jogo
from app.src.player import JogadorImpulsivo, JogadorExigente, JogadorCauteloso, JogadorAleatorio
from app.src.property import Propriedade
from app.src.schemas import ResultadoSimulacao

router = APIRouter()

@router.get("/jogo/simular", response_model=ResultadoSimulacao)
def simular_jogo() -> ResultadoSimulacao:
    jogadores = [
        JogadorImpulsivo(nome="impulsivo"),
        JogadorExigente(nome="exigente"),
        JogadorCauteloso(nome="cauteloso"),
        JogadorAleatorio(nome="aleatorio"),
    ]

    tabuleiro = [
        Propriedade(nome=f"Propriedade {i}", custo=(i + 1) * 20, aluguel=(i + 1) * 10)
        for i in range(20)
    ]

    jogo = Jogo(jogadores=jogadores, propriedades=tabuleiro)
    resultado = jogo.executar()

    return ResultadoSimulacao(**resultado)
