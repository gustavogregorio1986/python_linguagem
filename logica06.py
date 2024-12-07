import pandas as pd

# Criando um DataFrame
data = {
    "Nome": ["João", "Maria", "José"],
    "Idade": [28, 34, 23]
}
df = pd.DataFrame(data)

# Verificando o tamanho do DataFrame
print(df.shape)
