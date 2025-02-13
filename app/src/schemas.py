from pydantic import BaseModel
from typing import List

class ResultadoSimulacao(BaseModel):
    vencedor: str
    jogadores: List[str]
