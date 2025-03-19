# Importando bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregando o dataset limpo
df = pd.read_csv("./dataset/dados_limpos.csv")

# Configuração do estilo dos gráficos
sns.set(style="whitegrid")

# Distribuição dos salários
plt.figure(figsize=(10,5))
sns.histplot(df["salary_in_usd"], bins=30, kde=True)
plt.title("Distribuição de Salários")
plt.xlabel("Salário (USD)")
plt.ylabel("Frequência")
plt.show()

# Média salarial por nível de experiência
salario_por_experiencia = df.groupby("experience_level")["salary_in_usd"].mean()
plt.figure(figsize=(8,4))
sns.barplot(x=salario_por_experiencia.index, y=salario_por_experiencia.values)
plt.title("Média Salarial por Nível de Experiência")
plt.xlabel("Nível de Experiência")
plt.ylabel("Salário Médio (USD)")
plt.show()

# Média salarial por país
salario_por_pais = df.groupby("company_location")["salary_in_usd"].mean().sort_values(ascending=False)
plt.figure(figsize=(10,5))
sns.barplot(x=salario_por_pais.index[:10], y=salario_por_pais.values[:10])
plt.xticks(rotation=45)
plt.title("Média Salarial por País (Top 10)")
plt.xlabel("País")
plt.ylabel("Salário Médio (USD)")
plt.show()

# Média salarial por tamanho de empresa
salario_por_tamanho = df.groupby("company_size")["salary_in_usd"].mean()
plt.figure(figsize=(6,4))
sns.barplot(x=salario_por_tamanho.index, y=salario_por_tamanho.values)
plt.title("Média Salarial por Tamanho da Empresa")
plt.xlabel("Tamanho da Empresa")
plt.ylabel("Salário Médio (USD)")
plt.show()
