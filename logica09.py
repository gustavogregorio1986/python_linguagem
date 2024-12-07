import pandas as pd

# Criando um DataFrame de exemplo
data = {
    "Nome": ["Ana", "Carlos", "Lucas"],
    "Idade": [22, 34, 28],
}

df = pd.DataFrame(data)

# Verificando o tamanho do DataFrame
print(df.shape)
