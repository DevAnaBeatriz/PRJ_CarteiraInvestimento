import pandas as pd
import yfinance as yf
import pandas_datareader.data as pdr

yf.pdr_override()  # Configura o Yahoo Finance

# Lendo o arquivo carteira.txt
with open("../data/carteira.txt", "r") as arquivo:
    linhas = arquivo.readlines()

# Criando dicionário de ativos e valores investidos
carteira = {}
for linha in linhas:
    ticker, valor = linha.strip().split(" - ")
    ticker = f"{ticker}.SA"  # Adiciona .SA para ações brasileiras
    carteira[ticker] = float(valor)

# Definir período de análise
data_inicial = "2024-01-02"
data_final = "2024-12-15"

# Buscar cotações no Yahoo Finance
tickers = list(carteira.keys())
cotacoes = pdr.get_data_yahoo(tickers, start=data_inicial, end=data_final)["Adj Close"]

# Calcular rentabilidade de cada ativo
precos_iniciais = cotacoes.iloc[0]
precos_finais = cotacoes.iloc[-1]
variacao_percentual = (precos_finais - precos_iniciais) / precos_iniciais
rentabilidade_individual = variacao_percentual * pd.Series(carteira)

# Rentabilidade total da carteira
rentabilidade_total = rentabilidade_individual.sum() / sum(carteira.values()) * 100

# Comparação com o IBOV
cotacao_ibov = pdr.get_data_yahoo("^BVSP", start=data_inicial, end=data_final)["Adj Close"]
variacao_ibov = (cotacao_ibov.iloc[-1] - cotacao_ibov.iloc[0]) / cotacao_ibov.iloc[0] * 100

# Exibir resultados
print("\nRentabilidade de cada ativo na carteira (%):")
print(rentabilidade_individual * 100)
print(f"\nRentabilidade total da carteira: {rentabilidade_total:.2f}%")
print(f"\nRentabilidade do IBOV: {variacao_ibov:.2f}%")
print(f"A carteira {'GANHOU' if rentabilidade_total > variacao_ibov else 'PERDEU'} do IBOV.")
