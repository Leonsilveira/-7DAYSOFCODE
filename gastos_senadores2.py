import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet
import os

# Carregar o dataset
df = pd.read_csv("E:\\Projetos 2025\\#7DaysOfCode\\dataset_forecasting\\dataset_ceaps_forecasting.csv")

# Converter a coluna 'ds' para datetime
df['ds'] = pd.to_datetime(df['ds'])

# Definir a coluna 'ds' como índice
df.set_index('ds', inplace=True)

# Calcular a média dos últimos três meses
last_three_months = df['y'].last('3ME')
mean_last_three_months = last_three_months.mean()

# Prever os próximos três meses com a média dos últimos três meses
future_dates = pd.date_range(start=df.index.max() + pd.Timedelta(days=1), periods=90, freq='D')
forecast_simple = pd.DataFrame(mean_last_three_months, index=future_dates, columns=['y'])

print(f"Previsão média dos últimos três meses: {mean_last_three_months}")
print(f"Previsão para os próximos três meses:\n{forecast_simple.head()}")

# Preparar o dataframe para o Prophet
df_prophet = df.reset_index()
df_prophet.columns = ['ds', 'y']

# Criar e ajustar o modelo
model = Prophet()
model.fit(df_prophet)

# Criar datas futuras para previsão (próximos 90 dias)
future = model.make_future_dataframe(periods=90)
forecast = model.predict(future)

# Exibir a previsão
print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail())

# Visualizar as previsões com matplotlib
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(df.index, df['y'], label='Dados Reais')
ax.plot(forecast['ds'], forecast['yhat'], label='Previsão')
ax.fill_between(forecast['ds'], forecast['yhat_lower'], forecast['yhat_upper'], color='gray', alpha=0.2)
ax.set_xlabel('Data')
ax.set_ylabel('Gastos')
ax.legend()
plt.title('Previsão de Gastos dos Senadores')
plt.savefig('E:\\Projetos 2025\\#7DaysOfCode\\previsao_gastos_senadores.png')  # Salvar a imagem

# Agrupar os dados por mês e somar os gastos
monthly_expenses = df['y'].resample('M').sum()

# Criar o gráfico de pizza
plt.figure(figsize=(8, 8))
plt.pie(monthly_expenses, labels=monthly_expenses.index.strftime('%B'), autopct='%1.1f%%', startangle=140)
plt.title('Distribuição dos Gastos por Mês')
plt.axis('equal')
plt.savefig('E:\\Projetos 2025\\#7DaysOfCode\\distribuicao_gastos_pizza.png')  # Salvar a imagem

# Listar arquivos no diretório para verificar se as imagens foram salvas
files = os.listdir("E:\\Projetos 2025\\#7DaysOfCode")
print(files)
