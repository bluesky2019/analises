import streamlit as st
import pandas as pd

# Título do aplicativo
st.title('Análise de Dados do Mercado')

# Carregando os dados
@st.cache  # Cache para otimizar o carregamento em múltiplas execuções
def load_data():
    data = pd.read_csv('base_de_dados_mercado.csv')
    return data

data = load_data()

# Mostrar os primeiros registros da tabela
st.header('Primeiros registros da tabela de dados')
st.write(data.head())

# Mostrar estatísticas descritivas
st.header('Estatísticas Descritivas')
st.write(data.describe())

# Permitir ao usuário selecionar uma coluna para visualizar
if st.checkbox('Mostrar gráfico de barras'):
    colunas = data.columns.tolist()
    coluna_selecionada = st.selectbox('Selecione a coluna para o gráfico:', colunas)
    st.bar_chart(data[coluna_selecionada].value_counts())
