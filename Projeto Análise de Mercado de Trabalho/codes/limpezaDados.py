# Importando bibliotecas
import pandas as pd

# Carregando o dataset original
df = pd.read_csv("./dataset/dados_originais.csv")

# Verificando valores nulos
print("Valores nulos por coluna:")
print(df.isnull().sum())

# Removendo valores nulos
df = df.dropna()

# Verificando valores duplicados
print("Valores duplicados:", df.duplicated().sum())

# Removendo duplicatas
df = df.drop_duplicates()

# Salvando o dataset limpo
df.to_csv("dados_limpos.csv", index=False)

print("Dados limpos e salvos em 'dados_limpos.csv'.")
