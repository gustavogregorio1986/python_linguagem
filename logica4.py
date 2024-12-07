import pandas as pd

# Criando um DataFrame de exemplo
data = {
    "Nome": ["Alice", "Bob", "Charlie"],
    "Idade": [25, 30, 35],
    "Cidade": ["São Paulo", "Rio de Janeiro", "Belo Horizonte"]
}

df = pd.DataFrame(data)

# Verificando o tamanho do DataFrame
print(df.shape)
