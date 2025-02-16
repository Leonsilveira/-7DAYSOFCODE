import pandas as pd
import plotly.express as px

# Carregar o dataset (substitua 'seu_arquivo.csv' pelo nome do seu arquivo)
df = pd.read_csv('E:\\Projetos 2025\\#7DaysOfCode\\dataset\\df_ceaps_limpo.csv')

# Exibir as primeiras linhas do dataset para entender sua estrutura
print(df.head())

# Contagem do número de ocorrências de cada senador
contagem_senadores = df['SENADOR'].value_counts()
print(contagem_senadores)

# Soma dos gastos declarados por senador
gastos_por_senador = df.groupby('SENADOR')['VALOR_REEMBOLSADO'].sum()
print(gastos_por_senador)

# Soma dos gastos por ano
gastos_por_ano = df.groupby('ANO')['VALOR_REEMBOLSADO'].sum()
print(gastos_por_ano)

# Criar um DataFrame para os gastos por senador
df_gastos_senador = gastos_por_senador.reset_index()
df_gastos_senador.columns = ['SENADOR', 'VALOR_REEMBOLSADO']

# Criar o gráfico de barras
fig_bar = px.bar(df_gastos_senador, x='SENADOR', y='VALOR_REEMBOLSADO', title='Gastos Declarados por Senador', labels={'VALOR_REEMBOLSADO':'Valor Reembolsado (R$)', 'SENADOR':'Senador'}, text='VALOR_REEMBOLSADO')

# Salvar o gráfico de barras como PNG e HTML
fig_bar.write_image('E:\\Projetos 2025\\#7DaysOfCode\\grafico_gastos_senador.png')
fig_bar.write_html('E:\\Projetos 2025\\#7DaysOfCode\\grafico_gastos_senador.html')

# Mostrar o gráfico de barras
fig_bar.show()

# Criar um DataFrame para os gastos por ano
df_gastos_ano = gastos_por_ano.reset_index()
df_gastos_ano.columns = ['ANO', 'VALOR_REEMBOLSADO']

# Criar o gráfico de linhas
fig_line = px.line(df_gastos_ano, x='ANO', y='VALOR_REEMBOLSADO', title='Gastos Declarados por Ano', labels={'VALOR_REEMBOLSADO':'Valor Reembolsado (R$)', 'ANO':'Ano'}, text='VALOR_REEMBOLSADO')

# Salvar o gráfico de linhas como PNG e HTML
fig_line.write_image('E:\\Projetos 2025\\#7DaysOfCode\\grafico_gastos_ano.png')
fig_line.write_html('E:\\Projetos 2025\\#7DaysOfCode\\grafico_gastos_ano.html')

# Mostrar o gráfico de linhas
fig_line.show()
