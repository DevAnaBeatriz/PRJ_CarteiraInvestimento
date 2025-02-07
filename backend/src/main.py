import os
import pandas as pd
import yfinance as yf
import pandas_datareader.data as pdr
import warnings
import matplotlib.pyplot as plt

warnings.simplefilter(action='ignore', category=FutureWarning)
pdr.get_data_yahoo = yf.download

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
caminho_arquivo = os.path.join(base_dir, "carteira.txt")

if not os.path.exists(caminho_arquivo):
    print(f"Erro: O arquivo {caminho_arquivo} não foi encontrado.")
    exit(1)

carteira = {}
with open(caminho_arquivo, "r") as arquivo:
    for linha in arquivo.readlines():
        try:
            ticker, valor = linha.strip().split(" - ")
            ticker = f"{ticker}.SA"
            carteira[ticker] = float(valor)
        except ValueError:
            print(f"Erro ao processar linha: {linha.strip()} - Verifique o formato do arquivo.")
            exit(1)

data_inicial = "2024-12-01"
data_final = "2025-02-07"

tickers = list(carteira.keys())
try:
    cotacoes = pdr.get_data_yahoo(tickers, start=data_inicial, end=data_final)["Adj Close"]
except Exception as e:
    print(f"Erro ao buscar cotações: {e}")
    exit(1)

if cotacoes.empty:
    print("Erro: Nenhuma cotação foi baixada. Verifique a conexão com o Yahoo Finance.")
    exit(1)

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
    print(f"Erro ao buscar cotação do IBOV: {e}")
    variacao_ibov = None

df_resultados = pd.DataFrame({
    "Valor Investido (R$)": carteira,
    "Preço Inicial (R$)": precos_iniciais,
    "Preço Final (R$)": precos_finais,
    "Rentabilidade (%)": variacao_percentual
}).round(2)

print("\nDetalhes da Carteira de Investimentos:\n")
print(df_resultados.to_string())

print(f"\nRentabilidade total da carteira: {rentabilidade_total:.2f}%")

if variacao_ibov is not None:
    print(f"\nRentabilidade do IBOV: {variacao_ibov:.2f}%")
    print(f"A carteira {'+ GANHOU' if rentabilidade_total > variacao_ibov else '- PERDEU'} do IBOV.")
else:
    print("\nNão foi possível obter a rentabilidade do IBOV.")

plt.figure(figsize=(12, 6))
cotacoes.plot(title=f"Evolução dos Ativos da Carteira ({data_inicial} a {data_final})")
plt.xlabel("Data")
plt.ylabel("Preço Ajustado (R$)")
plt.legend(title="Ativos", loc="upper left", bbox_to_anchor=(1, 1))
plt.grid()
plt.tight_layout()
plt.show()
