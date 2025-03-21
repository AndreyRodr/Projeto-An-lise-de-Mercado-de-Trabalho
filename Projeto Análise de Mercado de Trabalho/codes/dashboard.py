import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class DashboardSalarios:
    def __init__(self, arquivo_dados):
        """Inicializa a classe carregando os dados"""
        self.df = pd.read_csv(arquivo_dados)

    def configurar_dashboard(self):
        """Configura título e filtros do Streamlit"""
        st.title("📊 Dashboard de Análise de Mercado de Trabalho")

        # Sidebar para filtros
        st.sidebar.header("Filtros")
        self.filtros()

    def filtros(self):
        """Aplica filtros baseados na escolha do usuário"""
        pais_selecionado = st.sidebar.multiselect("Selecione o país", self.df['company_location'].unique())
        cargo_selecionado = st.sidebar.multiselect("Selecione o cargo", self.df['job_title'].unique())

        if pais_selecionado:
            self.df = self.df[self.df['company_location'].isin(pais_selecionado)]
        if cargo_selecionado:
            self.df = self.df[self.df['job_title'].isin(cargo_selecionado)]

    def plot_graph(self, fig):
        """Exibe gráficos no Streamlit"""
        st.pyplot(fig)

    def distribuicao_salarial(self):
        """Gera gráfico da distribuição salarial"""
        st.subheader("Distribuição Salarial")
        fig, ax = plt.subplots(figsize=(8, 4))
        sns.histplot(self.df['salary_in_usd'], bins=30, kde=True, ax=ax)
        ax.set_xlabel("Salário em USD")
        self.plot_graph(fig)

    def media_salarial_por_cargo(self):
        """Gera gráfico da média salarial por cargo"""
        st.subheader("Média Salarial por Cargo")
        fig, ax = plt.subplots(figsize=(8, 4))
        media_por_cargo = self.df.groupby('job_title')['salary_in_usd'].mean().sort_values(ascending=False)
        media_por_cargo.head(10).plot(kind='bar', ax=ax, color='royalblue')
        ax.set_xlabel("Cargo")
        ax.set_ylabel("Salário Médio (USD)")
        self.plot_graph(fig)

    def evolucao_salarial(self):
        """Gera gráfico da evolução salarial ao longo do tempo"""
        st.subheader("Evolução Salarial ao Longo do Tempo")
        fig, ax = plt.subplots(figsize=(8, 4))
        self.df.groupby('work_year')['salary_in_usd'].mean().plot(ax=ax, marker='o', color='green')
        ax.set_ylabel("Salário Médio (USD)")
        ax.set_xlabel("Ano")
        self.plot_graph(fig)

    def media_salarial_por_pais(self):
        """Gera gráfico da média salarial por país"""
        st.subheader("Média Salarial por País")
        fig, ax = plt.subplots(figsize=(8, 4))
        media_por_pais = self.df.groupby('company_location')['salary_in_usd'].mean().sort_values(ascending=False)
        media_por_pais.head(10).plot(kind='bar', ax=ax, color='orange')
        ax.set_ylabel("Salário Médio (USD)")
        ax.set_xlabel("País")
        self.plot_graph(fig)

    def executar_dashboard(self):
        """Executa todas as funções do dashboard"""
        self.configurar_dashboard()
        self.distribuicao_salarial()
        self.media_salarial_por_cargo()
        self.evolucao_salarial()
        self.media_salarial_por_pais()

# Executando o dashboard
if __name__ == "__main__":
    dashboard = DashboardSalarios("./dataset/dados_limpos.csv")
    dashboard.executar_dashboard()
