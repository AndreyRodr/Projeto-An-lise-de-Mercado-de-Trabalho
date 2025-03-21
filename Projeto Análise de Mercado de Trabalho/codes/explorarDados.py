import pandas as pd

class AnaliseDados:
    def __init__(self, arquivo_dados):
        """Inicializa a classe com o caminho do arquivo CSV"""
        self.arquivo_dados = arquivo_dados
        self.df = None

    def carregar_dados(self):
        """Carrega os dados do CSV"""
        self.df = pd.read_csv(self.arquivo_dados)
        print("Dataset carregado com sucesso!")

    def exibir_primeiras_linhas(self, n=5):
        """Exibe as primeiras linhas do dataset"""
        print(self.df.head(n))

    def top_cargos_mais_comuns(self, top_n=10):
        """Exibe os cargos mais comuns"""
        top_cargos = self.df["job_title"].value_counts().head(top_n)
        print(f"Top {top_n} cargos mais comuns:")
        print(top_cargos)

    def media_salarial_por_cargo(self, top_n=10):
        """Exibe os cargos com maior média salarial"""
        salario_por_cargo = self.df.groupby("job_title")["salary_in_usd"].mean().sort_values(ascending=False)
        print(f"Top {top_n} cargos com maior média salarial:")
        print(salario_por_cargo.head(top_n))

    def media_salarial_por_experiencia(self):
        """Exibe a média salarial por nível de experiência"""
        salario_por_experiencia = self.df.groupby("experience_level")["salary_in_usd"].mean()
        print("Média Salarial por Nível de Experiência:")
        print(salario_por_experiencia)

    def executar_analise(self):
        """Executa todas as análises em sequência"""
        self.carregar_dados()
        self.exibir_primeiras_linhas()
        self.top_cargos_mais_comuns()
        self.media_salarial_por_cargo()
        self.media_salarial_por_experiencia()

# Executando a análise
if __name__ == "__main__":
    analise = AnaliseDados("./dataset/dados_limpos.csv")
    analise.executar_analise()
