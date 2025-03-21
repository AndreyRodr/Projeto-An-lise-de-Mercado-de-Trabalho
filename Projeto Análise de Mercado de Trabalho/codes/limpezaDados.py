import pandas as pd

class LimpezaDados:
    def __init__(self, arquivo_entrada, arquivo_saida):
        """Inicializa a classe com os arquivos de entrada e saída"""
        self.arquivo_entrada = arquivo_entrada
        self.arquivo_saida = arquivo_saida
        self.df = None

    def carregar_dados(self):
        """Carrega os dados do arquivo CSV"""
        self.df = pd.read_csv(self.arquivo_entrada)
        print("Dataset carregado com sucesso!")

    def verificar_valores_nulos(self):
        """Exibe a contagem de valores nulos por coluna"""
        nulos = self.df.isnull().sum()
        print("Valores nulos por coluna:\n", nulos)

    def remover_valores_nulos(self):
        """Remove todas as linhas com valores nulos"""
        self.df = self.df.dropna()
        print("Valores nulos removidos!")

    def verificar_duplicatas(self):
        """Exibe a quantidade de registros duplicados"""
        duplicatas = self.df.duplicated().sum()
        print(f"Valores duplicados: {duplicatas}")

    def remover_duplicatas(self):
        """Remove registros duplicados"""
        self.df = self.df.drop_duplicates()
        print("Valores duplicados removidos!")

    def salvar_dados_limpos(self):
        """Salva o dataset limpo em um novo arquivo"""
        self.df.to_csv(self.arquivo_saida, index=False)
        print(f"Dados limpos salvos em '{self.arquivo_saida}'.")

    def executar_limpeza(self):
        """Executa todas as etapas de limpeza"""
        self.carregar_dados()
        self.verificar_valores_nulos()
        self.remover_valores_nulos()
        self.verificar_duplicatas()
        self.remover_duplicatas()
        self.salvar_dados_limpos()

# Executando a limpeza dos dados
if __name__ == "__main__":
    limpeza = LimpezaDados("./dataset/dados_originais.csv", "./dataset/dados_limpos.csv")
    limpeza.executar_limpeza()
