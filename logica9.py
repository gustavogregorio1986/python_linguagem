import pandas as pd

# Criando um DataFrame de exemplo
data = {
    "Produto": ["A", "B", "C"],
    "Preço": [10.5, 20.0, 15.5]
}

df = pd.DataFrame(data)

# Verificando o tamanho do DataFrame
print(df.shape)
