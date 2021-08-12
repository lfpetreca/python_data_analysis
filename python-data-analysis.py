import pandas as pd
import plotly.express as px

#Importar a Base de Dados
tabela = pd.read_csv('./telecom_users.csv')
#Visualizar a base de dados
tabela = tabela.drop(['Unnamed: 0', 'IDCliente'], axis=1) 
# Tratamento da base de dados -- Remover colunas interamente vazias, linhas com pelo menos um campo vazio
tabela['TotalGasto'] = pd.to_numeric(tabela['TotalGasto'], errors='coerce')
# Excluir colunas completamente vazias
tabela = tabela.dropna(how='all', axis=1)
# Excluir linhas com pelo menos um valor vazio 
tabela = tabela.dropna(how='any', axis=0)
# Análise Exploratória -> Análise Geral -> Ver como estão os cancelamentos
display(tabela['Churn'].value_counts())
display(tabela['Churn'].value_counts(normalize=True).map('{:.1%}'.format))
# Análise -> Identificar o motivo dos clientes cancelarem
for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color='Churn')
    grafico.show()