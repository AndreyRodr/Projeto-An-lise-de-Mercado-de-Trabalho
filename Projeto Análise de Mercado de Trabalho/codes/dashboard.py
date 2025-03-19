import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("./dataset/dados_limpos.csv")

st.title("Análise de Mercado de Trabalho")

# Seleção de cargo
cargo = st.selectbox("Selecione um cargo", df["job_title"].unique())

# Filtrar os dados
df_filtrado = df[df["job_title"] == cargo]

# Gráfico de salários
fig, ax = plt.subplots()
sns.histplot(df_filtrado["salary_in_usd"], bins=20, kde=True, ax=ax)
st.pyplot(fig)
