from flask import Flask, jsonify
from flask_cors import CORS
import os
import pandas as pd
import yfinance as yf
import pandas_datareader.data as pdr
import warnings

app = Flask(__name__)
CORS(app)

warnings.simplefilter(action='ignore', category=FutureWarning)
pdr.get_data_yahoo = yf.download

caminho_arquivo = "carteira.txt"

if not os.path.exists(caminho_arquivo):
    raise FileNotFoundError(f"O arquivo {caminho_arquivo} não foi encontrado.")

carteira = {}
with open(caminho_arquivo, "r") as arquivo:
    for linha in arquivo.readlines():
        try:
            ticker, valor = linha.strip().split(" - ")
            ticker = f"{ticker}.SA"
            carteira[ticker] = float(valor)
        except ValueError:
            raise ValueError(f"Erro ao processar linha: {linha.strip()} - Verifique o formato do arquivo.")

data_inicial = "2024-12-01"
data_final = "2025-02-07"

tickers = list(carteira.keys())

try:
    cotacoes = pdr.get_data_yahoo(tickers, start=data_inicial, end=data_final)["Adj Close"]
except Exception as e:
    raise Exception(f"Erro ao buscar cotações: {e}")

if cotacoes.empty:
    raise Exception("Nenhuma cotação foi baixada. Verifique a conexão com o Yahoo Finance.")

cotacoes = cotacoes.dropna(axis=1, how='all')

precos_iniciais = cotacoes.iloc[0]
precos_finais = cotacoes.iloc[-1]
variacao_percentual = ((precos_finais - precos_iniciais) / precos_iniciais) * 100

rentabilidade_individual = (variacao_percentual / 100) * pd.Series(carteira)
rentabilidade_total = rentabilidade_individual.sum() / sum(carteira.values()) * 100

try:
    cotacao_ibov = pdr.get_data_yahoo("^BVSP", start=data_inicial, end=data_final)["Adj Close"]
    variacao_ibov = ((cotacao_ibov.iloc[-1] - cotacao_ibov.iloc[0]) / cotacao_ibov.iloc[0]) * 100
except Exception as e:
    variacao_ibov = None

@app.route('/api/rentabilidade', methods=['GET'])
def get_rentabilidade():
    df_resultados = pd.DataFrame({
        "Valor Investido (R$)": carteira,
        "Preço Inicial (R$)": precos_iniciais,
        "Preço Final (R$)": precos_finais,
        "Rentabilidade (%)": variacao_percentual
    }).round(2)

    resultado = {
        "detalhes": df_resultados.to_dict(orient="index"),
        "rentabilidade_total": round(rentabilidade_total, 2),
        "rentabilidade_ibov": round(variacao_ibov, 2) if variacao_ibov is not None else "N/A"
    }

    return jsonify(resultado)

if __name__ == '__main__':
    app.run(debug=True)
