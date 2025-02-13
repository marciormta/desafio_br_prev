from fastapi import FastAPI
from app.routers import simulation

def criar_aplicacao() -> FastAPI:
    aplicacao = FastAPI(
        title="Simulação de Jogo"
    )
    aplicacao.include_router(simulation.router)
    return aplicacao

app = criar_aplicacao()
