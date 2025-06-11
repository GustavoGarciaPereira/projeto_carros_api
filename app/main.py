# app/main.py

from fastapi import FastAPI, HTTPException
from .schemas import CarInput, CarOutput
from .model import prever_preco

app = FastAPI(
    title="API de Previsão de Preços de Carros",
    description="API para estimar o preço de um carro usado com base em suas características.",
    version="1.0.0"
)

@app.get("/", summary="Mensagem de boas-vindas")
def read_root():
    return {"message": "Bem-vindo à API de Previsão de Preços de Carros! Acesse /docs para testar."}


@app.post("/prever_preco_carro", response_model=CarOutput, summary="Prevê o preço de um carro")
def post_prever_preco_carro(dados_carro: CarInput):
    """
    Recebe os dados de um carro e retorna uma estimativa de preço.

    - **marca**: Marca do carro (ex: "Ford")
    - **modelo**: Modelo do carro (ex: "Ka")
    - **ano**: Ano de fabricação
    - **quilometragem**: Quilometragem do carro
    """
    try:
        preco = prever_preco(
            marca=dados_carro.marca,
            modelo=dados_carro.modelo,
            ano=dados_carro.ano,
            quilometragem=dados_carro.quilometragem
        )
        return CarOutput(preco_estimado=preco)
    except RuntimeError as e:
        raise HTTPException(status_code=503, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erro ao processar a requisição. Verifique se a marca e modelo são válidos. Detalhe: {e}")