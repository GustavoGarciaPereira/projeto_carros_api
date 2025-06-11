# app/schemas.py

from pydantic import BaseModel, Field

# Schema para os dados de entrada da API
class CarInput(BaseModel):
    marca: str = Field(..., example="Ford")
    modelo: str = Field(..., example="Ka")
    ano: int = Field(..., example=2018)
    quilometragem: int = Field(..., example=50000)

# Schema para os dados de saída da API
class CarOutput(BaseModel):
    preco_estimado: float