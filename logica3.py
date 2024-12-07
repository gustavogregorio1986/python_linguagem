import pandas as pd
import numpy as np

# Criar um DataFrame de exemplo com valores nulos
data = {
    "Produto": ["A", "B", np.nan, "D", "E", np.nan],
    "Vendas": [100, np.nan, 200, 300, np.nan, 500],
    "Ano": [2020, 2021, 2020, 2021, 2020, 2021]
}
df = pd.DataFrame(data)

print(f"Tamanho original do DataFrame: {df.shape}")

# Remover linhas com valores nulos
df_sem_nulos = df.dropna()

print(f"Tamanho após remoção de valores nulos: {df_sem_nulos.shape}")
