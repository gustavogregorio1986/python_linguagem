import pandas as pd

# Criar um DataFrame de exemplo com dados temporais
data = {
    "Data": pd.date_range(start="2023-01-01", end="2023-03-31", freq="D"),
    "Vendas": [100 + i for i in range(90)]  # Valores de vendas crescentes
}
df = pd.DataFrame(data)

print(f"Tamanho original: {df.shape}")

# Agrupar por mês e somar as vendas
df["Mês"] = df["Data"].dt.to_period("M")
df_agrupado = df.groupby("Mês").agg({"Vendas": "sum"}).reset_index()

print(f"Tamanho após agrupar por mês: {df_agrupado.shape}")
