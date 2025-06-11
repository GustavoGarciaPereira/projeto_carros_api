# API de Previsão de Preços de Carros Usados 🚗

![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-green.svg)
![Scikit-learn](https://img.shields.io/badge/scikit--learn-1.2%2B-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

Este projeto consiste em uma API RESTful desenvolvida com **FastAPI** para servir um modelo de Machine Learning. O modelo, treinado com **Scikit-learn**, é capaz de prever o preço de um carro usado com base em suas características, como marca, modelo, ano e quilometragem.

O projeto demonstra um fluxo completo de MLOps em pequena escala: desde a análise exploratória e treinamento do modelo até sua "produção" através de uma API web.

## ✨ Features

-   **Análise Exploratória de Dados (EDA):** Um notebook Jupyter (`exploracao.ipynb`) para entender os dados.
-   **Treinamento de Modelo:** Um script (`train.py`) para treinar um modelo de Regressão Linear Múltipla e salvá-lo.
-   **API RESTful:** Endpoints para receber dados de um carro e retornar a previsão de preço.
-   **Validação de Dados:** Uso de Pydantic para garantir que os dados de entrada e saída da API estejam no formato correto.
-   **Documentação Interativa:** Geração automática de documentação da API com Swagger UI e ReDoc.

## 📂 Estrutura do Projeto

```
/projeto_carros_api
|
|-- app/
|   |-- __init__.py
|   |-- main.py             # Lógica do FastAPI (endpoints)
|   |-- model.py            # Lógica para carregar e usar o modelo de ML
|   |-- schemas.py          # Schemas Pydantic (validação de dados)
|
|-- data/
|   |-- carros.csv          # Dados para treinamento
|
|-- notebooks/
|   |-- exploracao.ipynb    # Análise exploratória dos dados
|
|-- modelo_carro.joblib     # Arquivo do modelo treinado
|
|-- requirements.txt        # Dependências do projeto
|
|-- train.py                # Script para treinar o modelo
|
|-- README.md               # Este arquivo
```

## 🛠️ Tecnologias Utilizadas

-   **Python 3.9+**
-   **FastAPI:** Framework web para construir a API.
-   **Uvicorn:** Servidor ASGI para rodar a API.
-   **Scikit-learn:** Para treinar o modelo de Regressão Linear.
-   **Pandas:** Para manipulação e pré-processamento dos dados.
-   **Joblib:** Para salvar e carregar o modelo treinado.
-   **Jupyter Notebook:** Para a análise exploratória de dados.

## 🚀 Como Executar

Siga os passos abaixo para configurar e rodar o projeto localmente.

### 1. Pré-requisitos

-   Python 3.9 ou superior
-   Git

### 2. Instalação

Clone o repositório e instale as dependências:

```bash
# 1. Clone o repositório
git clone https://github.com/seu-usuario/projeto_carros_api.git

# 2. Navegue até a pasta do projeto
cd projeto_carros_api

# 3. Crie e ative um ambiente virtual (recomendado)
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

# 4. Instale as dependências
pip install -r requirements.txt
```

### 3. Treinamento do Modelo

Antes de iniciar a API, você precisa treinar o modelo. O script `train.py` irá ler os dados de `data/carros.csv`, treinar o modelo e salvar o arquivo `modelo_carro.joblib` na raiz do projeto.

```bash
python train.py
```

Você deverá ver uma mensagem indicando que o treinamento foi concluído com sucesso.

### 4. Iniciando a API

Com o modelo treinado, inicie o servidor da API com Uvicorn:

```bash
uvicorn app.main:app --reload
```

-   `app.main`: Refere-se ao arquivo `main.py` dentro da pasta `app`.
-   `:app`: Refere-se ao objeto `app = FastAPI()` dentro do arquivo.
-   `--reload`: Reinicia o servidor automaticamente após qualquer alteração no código.

O servidor estará rodando em `http://127.0.0.1:8000`.

## 🕹️ Como Usar a API

A maneira mais fácil de interagir com a API é através da documentação interativa gerada pelo FastAPI.

1.  Abra seu navegador e acesse: **http://127.0.0.1:8000/docs**

2.  Você verá a documentação do Swagger UI. Expanda o endpoint `POST /prever_preco_carro`.

3.  Clique em "Try it out" e preencha o corpo da requisição com os dados do carro que deseja prever.

    **Exemplo de Request Body:**
    ```json
    {
      "marca": "Ford",
      "modelo": "Ka",
      "ano": 2018,
      "quilometragem": 50000
    }
    ```

4.  Clique em "Execute". A API retornará o preço estimado.

    **Exemplo de Response Body:**
    ```json
    {
      "preco_estimado": 43166.67
    }
    ```

Você também pode usar ferramentas como `curl` ou Postman para fazer requisições:

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/prever_preco_carro' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "marca": "VW",
  "modelo": "Gol",
  "ano": 2016,
  "quilometragem": 80000
}'
```

## 📈 Possíveis Melhorias
-   [ ] Adicionar testes unitários e de integração com `pytest`.
-   [ ] "Dockerizar" a aplicação para facilitar o deploy.
-   [ ] Fazer o deploy da API em um serviço de nuvem (Heroku, AWS, Google Cloud).
