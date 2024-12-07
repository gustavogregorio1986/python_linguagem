import pandas as pd

# Criar DataFrame com valores ausentes
data = {
    "Nome": ["Ana", "Bruno", "Carlos", "Diana"],
    "Idade": [23, None, 29, 40],
    "Cidade": ["São Paulo", "Rio de Janeiro", None, "Salvador"]
}
df = pd.DataFrame(data)

print(f"Tamanho original: {df.shape}")

# Remover linhas com valores nulos
df_clean = df.dropna()

print(f"Tamanho após limpeza: {df_clean.shape}")
