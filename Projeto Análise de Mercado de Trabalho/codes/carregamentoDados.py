import pandas as pd

class CarregamentoDados:
    def __init__(self, caminho_arquivo):
        """Inicializa a classe com o caminho do arquivo"""
        self.caminho_arquivo = caminho_arquivo
        self.df = None

    def carregar_dados(self):
        """Carrega o dataset e exibe as primeiras linhas"""
        self.df = pd.read_csv(self.caminho_arquivo)
        print("Primeiras linhas do dataset:")
        print(self.df.head())

    def salvar_copia(self, caminho_saida="dados_originais.csv"):
        """Salva uma cópia do dataset para referência futura"""
        if self.df is not None:
            self.df.to_csv(caminho_saida, index=False)
            print(f"Dataset carregado e salvo como '{caminho_saida}'.")
        else:
            print("Erro: Nenhum dado foi carregado para salvar.")

# Executando o carregamento de dados
if __name__ == "__main__":
    carregador = CarregamentoDados("./dataset/ds_salaries.csv")
    carregador.carregar_dados()
    carregador.salvar_copia()
