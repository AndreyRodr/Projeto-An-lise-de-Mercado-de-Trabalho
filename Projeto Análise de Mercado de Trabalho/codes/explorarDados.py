# Importando bibliotecas
import pandas as pd

# Carregando o dataset limpo
df = pd.read_csv("./dataset/dados_limpos.csv")

# Exibindo as primeiras linhas
print(df.head())

# Exibir os principais cargos
top_cargos = df["job_title"].value_counts().head(10)
print("Top 10 cargos mais comuns:")
print(top_cargos)

# Média salarial por cargo
salario_por_cargo = df.groupby("job_title")["salary_in_usd"].mean().sort_values(ascending=False)
print("Top 10 cargos com maior média salarial:")
print(salario_por_cargo.head(10))

# Média salarial por nível de experiência
salario_por_experiencia = df.groupby("experience_level")["salary_in_usd"].mean()
print("Média Salarial por Nível de Experiência:")
print(salario_por_experiencia)
