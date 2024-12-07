import pandas as pd

# Criando um DataFrame maior
data = {
    "Nome": ["Ana", "Carlos", "Lucas", "Pedro"],
    "Idade": [22, 33, 28, 40],
    "Cidade": ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba"]
}

df = pd.DataFrame(data)

# Verificando as dimensões do DataFrame
print(df.shape)
