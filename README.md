# 📊 Análise de Mercado de Trabalho - Data Science & TI

## 📌 Sobre o Projeto
Este projeto tem como objetivo analisar dados do mercado de trabalho na área de Data Science e Tecnologia da Informação (TI), explorando salários, cargos mais comuns e tendências salariais ao longo do tempo. As análises foram feitas utilizando Python e bibliotecas especializadas em ciência de dados.

## 🗂️ Dataset Utilizado
O dataset contém informações sobre:
- Cargo do profissional
- Localização da empresa
- Nível de experiência
- Salário em dólares (USD)
- Ano da coleta dos dados
- Tamanho da empresa

📌 Fonte dos dados: [Data Science Job Salaries - Kaggle](https://www.kaggle.com/datasets/ruchi798/data-science-job-salaries)

## 🛠️ Tecnologias Utilizadas
- **Python** → Linguagem principal para manipulação e análise dos dados.
- **Pandas** → Manipulação e limpeza de dados
- **Matplotlib** e **Seaborn** → Para criação de gráficos e visualizações.
- **Scikit-learn** → Para criação de modelos de Machine Learning para prever salários.
- **Jupyter Notebook** → Para exploração de dados e prototipação dos modelos.
- **Streamlit** → Para construir um dashboard interativo e visualização dos dados.

## 📊 Análises Realizadas
✔ **Distribuição de salários**: Verificação da faixa salarial predominante no setor.  
✔ **Cargos mais comuns**: Identificação dos cargos mais presentes no mercado.  
✔ **Média salarial por nível de experiência**: Comparação entre júnior, pleno e sênior.  
✔ **Média salarial por país**: Análise dos melhores países para remuneração.  
✔ **Evolução salarial ao longo dos anos**: Tendência do mercado de trabalho.   
✔ **Predição de salários (Machine Learning)**: Modelo de ML para prever salários futuros.

## 📈 Resultados e Insights
📍 **Os cargos mais bem pagos são:** Os cargos com as maiores remunerações são Data Analytics Lead ($405,000), Principal Data Engineer ($328,333) e Financial Data Analyst ($275,000), demonstrando que posições de liderança e áreas estratégicas tendem a oferecer salários elevados.       
📍 **O salário médio varia significativamente por país:** Os países com os maiores salários médios são Rússia ($157,500), Estados Unidos ($144,055) e Nova Zelândia ($125,000), indicando que oportunidades bem remuneradas não se limitam aos mercados tradicionais da América do Norte e Europa.  
📍 **A experiência impacta diretamente a remuneração:** Profissionais sêniores ganham, em média, 2,2x mais do que juniores, enquanto executivos recebem até 3,2x mais. Isso destaca a importância do avanço na carreira e da especialização para melhores salários.                       
📍 **Tendência de crescimento salarial:** Os salários na área aumentaram nos últimos anos, indicando um setor aquecido e com alta demanda.  
📍 **Empresas de grande porte tendem a pagar mais:** Empresas com mais de 500 funcionários oferecem salários superiores, especialmente em cargos de liderança.  
📍 **Áreas de especialização fazem diferença:** Profissionais com foco em Machine Learning e Cloud Computing recebem salários mais altos.

## 📊 Dashboard Interativo
O dashboard permite visualizar os seguintes gráficos:

- **Distribuição Salarial** 📊
- **Média Salarial por Cargo** 💼
- **Evolução Salarial ao Longo do Tempo** ⏳
- **Média Salarial por País** 🌍

🔗 Para executar o dashboard, utilize o seguinte comando:
```bash
streamlit run dashboard.py
```

## 🚀 Como Executar o Projeto
1️⃣ Clone este repositório:
```bash
 git clone https://github.com/AndreyRodr/Projeto-An-lise-de-Mercado-de-Trabalho.git
```
2️⃣ Instale as dependências:
```bash
 pip install -r requirements.txt
```
3️⃣ Execute os scripts de análise:
```bash
 python main.py
```
4️⃣ (Opcional) Rode a aplicação interativa com Streamlit:
```bash
 streamlit run dashboard.py
```

## 📌 Próximos Passos
🔹 Refinar o modelo de previsão salarial  
🔹 Integrar mais fontes de dados para análises mais completas  
🔹 Melhorar a organização do código

---
📢 **Contribuições são bem-vindas!** Caso tenha sugestões ou melhorias, fique à vontade para abrir uma issue ou pull request. 😊
