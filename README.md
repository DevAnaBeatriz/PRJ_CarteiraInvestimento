# PRJ_CarteiraInvestimento

## Sobre o Projeto
Este projeto tem como objetivo analisar a rentabilidade de uma carteira de investimentos utilizando **Python (Flask), Pandas, YFinance e Angular**. Ele busca cotações históricas de ativos da bolsa de valores e compara a performance da carteira com o índice **IBOVESPA (IBOV)**.

## Funcionalidades
- Obtenção de cotações históricas do Yahoo Finance via **Flask API**.
- Cálculo da rentabilidade individual de cada ativo.
- Comparação da performance da carteira com o **IBOVESPA**.
- **Frontend em Angular** para exibir os dados da carteira e gráficos.

## Tecnologias Utilizadas
### Backend (API)
- **Python 3.12.4**
- **Flask**
- **Flask-CORS**
- **Pandas**
- **Matplotlib**
- **YFinance**
- **Pandas DataReader**

### Frontend (Web)
- **Angular**
- **TypeScript**
- **Bootstrap**
- **HttpClient para comunicação com API**

## Pré-requisitos
Antes de rodar o projeto, instale as dependências necessárias.

### Clonar o Repositório
```bash
git clone https://github.com/DevAnaBeatriz/PRJ_CarteiraInvestimento.git
cd PRJ_CarteiraInvestimento
```

## Como Usar

### 1. Configurar a carteira
No arquivo `carteira.txt`, insira os ativos e os valores investidos no seguinte formato:
```text
ITUB4 - 2000
BBAS3 - 1500
VALE3 - 3000
PETR4 - 2500
```

### 2. Executar o Backend (Flask API)
Entre na pasta do backend e rode:
```bash
cd backend
pip install -r requirements.txt
python api.py
```
A API será iniciada em `http://127.0.0.1:5000/api/rentabilidade`.

### 3. Executar o Frontend (Angular)
Entre na pasta do frontend e rode:
```bash
cd frontend
npm install
ng serve --open
```
O aplicativo será iniciado em `http://localhost:4200/`.

### 4. Rodar a análise no Jupyter Notebook
Caso queira visualizar a análise diretamente pelo Jupyter Notebook:
```bash
jupyter notebook
```
Depois, abra o notebook `rentabilidade.ipynb` no Jupyter e rode as células para gerar os cálculos e gráficos.

### 5. Rodar o script principal
Se preferir, execute o script Python diretamente pelo terminal:
```bash
python main.py
```
O terminal exibirá a rentabilidade da carteira, e um gráfico será gerado mostrando a evolução dos ativos.

---

## Desafio
Se quiser se desafiar, siga este tutorial do YouTube e adapte a solução para rodar no Jupyter Notebook:
🔗 **[Tutorial de Automação em Python](https://www.youtube.com/watch?v=fMafQl9J4V0)**

### Regras do Desafio
- Utilize o kernel do **Jupyter 3.12.4**.
- Adapte o código conforme necessário para evitar incompatibilidades.

## Contribuição
Quer melhorar o projeto? Sinta-se à vontade para contribuir!

1. Faça um **fork** do repositório.
2. Crie um **branch** para sua feature: `git checkout -b minha-feature`.
3. Faça o **commit** das suas alterações: `git commit -m "Adicionei uma nova funcionalidade"`.
4. Envie para o repositório remoto: `git push origin minha-feature`.
5. Abra um **Pull Request**.
