### PRJ_CarteiraInvestimento

### Este projeto tem como objetivo analisar a rentabilidade de uma carteira de investimentos utilizando **Python, Pandas e YFinance**. Ele busca cotações históricas de ativos da bolsa de valores e compara a performance da carteira com o índice **IBOVESPA (IBOV)**.

### Funcionalidades
- Obtenção de cotações históricas do Yahoo Finance.
- Cálculo da rentabilidade individual de cada ativo.
- Comparação da performance da carteira com o IBOVESPA.
- Geração de gráficos para visualizar a evolução dos ativos.

### Tecnologias Utilizadas
- **Python 3.12.4**
- **Pandas**
- **Matplotlib**
- **YFinance**
- **Pandas DataReader**

### Pré-requisitos
Antes de rodar o projeto, instale as dependências necessárias:

```bash
pip install -r requirements.txt
```

Caso esteja rodando no Jupyter Notebook, certifique-se de ativar o ambiente correto:

```bash
pip install notebook
jupyter notebook
```

### Como Usar

#### 1. Configurar a carteira
No arquivo `carteira.txt`, insira os ativos e os valores investidos no seguinte formato:

```
ITUB4 - 2000
BBAS3 - 1500
VALE3 - 3000
PETR4 - 2500
```

#### 2. Executar a análise no Jupyter Notebook
Abra o arquivo `rentabilidade.ipynb` e execute todas as células para visualizar a análise da carteira:

```bash
jupyter notebook
```

Depois, abra o notebook `rentabilidade.ipynb` no Jupyter e rode as células para gerar os cálculos e gráficos.

#### 3. Rodar o script principal
Se preferir, execute o script Python diretamente pelo terminal:

```bash
python main.py
```

O terminal exibirá a rentabilidade da carteira, e um gráfico será gerado mostrando a evolução dos ativos.

---

### Desafio
Se quiser se desafiar, siga este tutorial do YouTube e adapte a solução para rodar no Jupyter Notebook:
🔗 **[Tutorial de Automação em Python](https://www.youtube.com/watch?v=fMafQl9J4V0)**

#### Regras do Desafio
- Utilize o kernel do **Jupyter 3.12.4**.
- Adapte o código conforme necessário para evitar incompatibilidades.

### Contribuição
Quer melhorar o projeto? Sinta-se à vontade para contribuir!

1. Faça um **fork** do repositório.
2. Crie um **branch** para sua feature: `git checkout -b minha-feature`.
3. Faça o **commit** das suas alterações: `git commit -m "Adicionei uma nova funcionalidade"`.
4. Envie para o repositório remoto: `git push origin minha-feature`.
5. Abra um **Pull Request**.
