# Criar DataFrame de exemplo
import pandas as pd

data = {
    "Nome": ["Ana", "Bruno", "Carlos", "Diana"],
    "Idade": [23, 35, 29, 40],
    "Cidade": ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Salvador"],
    "Salário": [2500, 4000, 3000, 5000]
}
df = pd.DataFrame(data)

print(f"Tamanho antes: {df.shape}")

# Excluir coluna "Salário"
df = df.drop(columns=["Salário"])

print(f"Tamanho após excluir coluna: {df.shape}")

df_sp = df[df["Cidade"] == "São Paulo"]
df_rj = df[df["Cidade"] == "Rio de Janeiro"]

print(f"Registros em São Paulo: {df_sp.shape[0]}")
print(f"Registros no Rio de Janeiro: {df_rj.shape[0]}")

