# train.py

import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

print("Carregando dados...")
df = pd.read_csv('data/carros.csv')

print("Processando dados...")

df_processed = pd.get_dummies(df, columns=['Marca', 'Modelo'], drop_first=True)

X = df_processed.drop('Preco', axis=1)
y = df_processed['Preco']

# Guardar as colunas usadas no treinamento é CRUCIAL

model_columns = X.columns.tolist()


print("Treinando o modelo...")
model = LinearRegression()
model.fit(X, y)


print("Salvando o modelo e as colunas em 'modelo_carro.joblib'...")

joblib.dump({'model': model, 'columns': model_columns}, 'modelo_carro.joblib')

print("Treinamento concluído com sucesso!")


print("\n--- Teste Rápido ---")
print(f"Colunas que o modelo espera: {model_columns}")

teste_data = {col: [0] for col in model_columns}
teste_data['Ano'] = [2020]
teste_data['Quilometragem'] = [30000]
teste_data['Marca_Ford'] = [0]
teste_data['Marca_VW'] = [0]

teste_data['Modelo_Ka'] = [0]
teste_data['Modelo_Mobi'] = [0]
teste_data['Modelo_Onix'] = [1]
teste_data['Modelo_Polo'] = [0]
teste_data['Modelo_Prisma'] = [0]
teste_data['Modelo_Uno'] = [0]

df_teste = pd.DataFrame(teste_data)
preco_estimado = model.predict(df_teste)
print(f"Preço estimado para o carro de teste: R$ {preco_estimado[0]:.2f}")