import pandas as pd

# Criar um DataFrame com MultiIndex
data = {
    "Produto": ["A", "A", "B", "B", "C", "C"],
    "Ano": [2020, 2021, 2020, 2021, 2020, 2021],
    "Vendas": [100, 150, 200, 250, 300, 350]
}

df = pd.DataFrame(data).set_index(["Produto", "Ano"])

# Verificar o tamanho do DataFrame
print(f"Tamanho do DataFrame com MultiIndex: {df.shape}")

# Resetar os índices para transformar em DataFrame "plano"
df_resetado = df.reset_index()

print(f"Tamanho após resetar o índice: {df_resetado.shape}")
