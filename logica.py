import pandas as pd

# Criando um DataFrame de exemplo
data = {
    "Nome": ["Ana", "Bruno", "Carlos"],
    "Idade": [23, 35, 29],
    "Cidade": ["São Paulo", "Rio de Janeiro", "Belo Horizonte"]
}

df = pd.DataFrame(data)

# Usando .shape
print(df.shape)  # Saída: (3, 3)

# Interpretando
n_linhas, n_colunas = df.shape
print(f"O DataFrame tem {n_linhas} linhas e {n_colunas} colunas.")

# Selecionando uma coluna como Series
series_idade = df["Idade"]

# Usando .shape
print(series_idade.shape)  # Saída: (3,)

# Interpretando
n_elementos = series_idade.shape[0]
print(f"A Series tem {n_elementos} elementos.")
