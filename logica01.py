import pandas as pd

# Criar um DataFrame de exemplo
data = {"Nome": ["Alice", "Bruno", "Carla"], "Idade": [25, 30, 35]}
df = pd.DataFrame(data)

print(f"Tamanho inicial: {df.shape}")

# Adicionar colunas dinamicamente
for i in range(1, 4):
    df[f"Nota_{i}"] = [7 + i, 6 + i, 8 + i]
    print(f"Tamanho após adicionar Nota_{i}: {df.shape}")

# Filtrar apenas nomes que começam com "A" ou "C"
filtro = df[df["Nome"].str.startswith(("A", "C"))]
print(f"Antes do filtro: {df.shape}")
print(f"Depois do filtro: {filtro.shape}")


# Criar subconjuntos para cada loja
lojas = {loja: df[df["Loja"] == loja] for loja in df["Loja"].unique()}

for loja, subset in lojas.items():
    print(f"Tamanho do subset da loja {loja}: {subset.shape}")


