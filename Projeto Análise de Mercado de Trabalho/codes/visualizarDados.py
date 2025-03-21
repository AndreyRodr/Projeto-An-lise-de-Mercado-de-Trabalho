import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class VisualizacaoDados:
    def __init__(self, arquivo_dados):
        """Carrega os dados e configura o estilo dos gráficos"""
        self.df = pd.read_csv(arquivo_dados)
        sns.set(style="whitegrid")
    
    def plot_distribuicao_salarial(self):
        """Gera um gráfico de distribuição de salários"""
        plt.figure(figsize=(10, 5))
        sns.histplot(self.df["salary_in_usd"], bins=30, kde=True)
        plt.title("Distribuição de Salários")
        plt.xlabel("Salário (USD)")
        plt.ylabel("Frequência")
        plt.show()
    
    def plot_salario_por_experiencia(self):
        """Gera um gráfico de média salarial por nível de experiência"""
        salario_por_experiencia = self.df.groupby("experience_level")["salary_in_usd"].mean()
        plt.figure(figsize=(8, 4))
        sns.barplot(x=salario_por_experiencia.index, y=salario_por_experiencia.values)
        plt.title("Média Salarial por Nível de Experiência")
        plt.xlabel("Nível de Experiência")
        plt.ylabel("Salário Médio (USD)")
        plt.show()
    
    def plot_salario_por_pais(self, top_n=10):
        """Gera um gráfico da média salarial por país (Top N países)"""
        salario_por_pais = self.df.groupby("company_location")["salary_in_usd"].mean().sort_values(ascending=False)
        plt.figure(figsize=(10, 5))
        sns.barplot(x=salario_por_pais.index[:top_n], y=salario_por_pais.values[:top_n])
        plt.xticks(rotation=45)
        plt.title(f"Média Salarial por País (Top {top_n})")
        plt.xlabel("País")
        plt.ylabel("Salário Médio (USD)")
        plt.show()
    
    def plot_salario_por_tamanho_empresa(self):
        """Gera um gráfico da média salarial por tamanho de empresa"""
        salario_por_tamanho = self.df.groupby("company_size")["salary_in_usd"].mean()
        plt.figure(figsize=(6, 4))
        sns.barplot(x=salario_por_tamanho.index, y=salario_por_tamanho.values)
        plt.title("Média Salarial por Tamanho da Empresa")
        plt.xlabel("Tamanho da Empresa")
        plt.ylabel("Salário Médio (USD)")
        plt.show()

# Executando os gráficos
if __name__ == "__main__":
    viz = VisualizacaoDados("./dataset/dados_limpos.csv")
    viz.plot_distribuicao_salarial()
    viz.plot_salario_por_experiencia()
    viz.plot_salario_por_pais()
    viz.plot_salario_por_tamanho_empresa()
