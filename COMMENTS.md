# Este repositório contém a implementação de uma aplicação desenvolvida com o framework FastAPI, gerenciada pelo gerenciador de pacotes uv.

## Requisitos

- **Python 3.12 ou superior**: Download Python: https://www.python.org/downloads/

- **uv**: Gerenciador de pacotes e projetos para Python. Instruções de instalação: https://github.com/astral-sh/uv#installation

  - **Windows**: Execute o seguinte comando no PowerShell com privilégios de administrador:

    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

## Passos para Configuração e Execução

1. **Clonar o Repositório**

   git clone https://github.com/marciormta/desafio_br_prev.git
   cd desafio_br_prev

2. **Gerar Ambiente virtual**

  uv venv
  
3. **Instalar as Dependências**

   uv sync

   *Nota*: O comando `uv sync` instala todas as dependências listadas no `pyproject.toml'.

4. **Ativar o Ambiente Virtual**

     .venv\Scripts\activate

5. **Executar a Aplicação**

   uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8080 ou apenas uvicorn app.main:app --reload --host 0.0.0.0 --port 8080

   A aplicação estará disponível em: http://127.0.0.1:8080

6. **Acessar a Documentação Interativa**

   Acesse a documentação interativa (Swagger UI) em: http://127.0.0.1:8080/docs

   Nesta interface, você pode testar o endpoint da aplicação.

 

