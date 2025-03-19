# Importando bibliotecas
import pandas as pd

# Carregando o dataset
df = pd.read_csv("./dataset/ds_salaries.csv")

# Exibindo as primeiras linhas do dataset
print("Primeiras linhas do dataset:")
print(df.head())

# Salvando cópia inicial para referência
df.to_csv("dados_originais.csv", index=False)

print("Dataset carregado e salvo como 'dados_originais.csv'.")