# app/model.py

import joblib
import pandas as pd

try:
    data = joblib.load("modelo_carro.joblib")
    model = data['model']
    model_columns = data['columns']
    print("Modelo e colunas carregados com sucesso.")
except FileNotFoundError:
    print("Arquivo do modelo não encontrado. Treine o modelo primeiro com 'train.py'.")
    model = None
    model_columns = None

def prever_preco(marca: str, modelo: str, ano: int, quilometragem: int) -> float:
    """
    Usa o modelo carregado para prever o preço de um carro.
    A função precisa replicar exatamente o pré-processamento feito no treinamento.
    """
    if model is None or model_columns is None:
        raise RuntimeError("Modelo não foi carregado. Execute o script de treinamento.")


    input_data = pd.DataFrame({
        'Marca': [marca],
        'Modelo': [modelo],
        'Ano': [ano],
        'Quilometragem': [quilometragem]
    })


    input_processed = pd.get_dummies(input_data, columns=['Marca', 'Modelo'])

    final_input = input_processed.reindex(columns=model_columns, fill_value=0)

    preco_previsto = model.predict(final_input)

    return float(preco_previsto[0])