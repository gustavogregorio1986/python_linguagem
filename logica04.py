import pandas as pd

# Criando um DataFrame simples
data = {
    "Nome": ["João", "Maria", "José"],
    "Idade": [28, 34, 23]
}
df = pd.DataFrame(data)

# Verificando as dimensões
print(df.shape)
