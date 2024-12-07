import pandas as pd

# Criando um DataFrame de exemplo
data = {
    "Nome": ["Ana", "Bruno", "Carlos", "Diana"],
    "Idade": [23, 35, 29, 40],
    "Cidade": ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Salvador"]
}
df = pd.DataFrame(data)

# Verificar tamanho inicial
print("Tamanho inicial:", df.shape)

# Filtrar pessoas com idade maior que 30
df_filtrado = df[df["Idade"] > 30]

# Verificar tamanho após filtro
print("Tamanho após filtro:", df_filtrado.shape)
