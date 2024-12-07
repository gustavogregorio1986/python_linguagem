import pandas as pd

# Criar um DataFrame inicial
data = {
    "Produto": ["A", "B", "C"],
    "Preço": [10, 20, 30],
    "Quantidade": [100, 150, 200]
}
df = pd.DataFrame(data)

print(f"Tamanho inicial do DataFrame: {df.shape}")

# Adicionar novas linhas
novos_dados = {
    "Produto": ["D", "E"],
    "Preço": [40, 50],
    "Quantidade": [250, 300]
}
df_novos = pd.DataFrame(novos_dados)

# Concatenar o DataFrame original com o novo
df_atualizado = pd.concat([df, df_novos], ignore_index=True)

print(f"Tamanho após adicionar novas linhas: {df_atualizado.shape}")
