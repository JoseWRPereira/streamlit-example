import pandas as pd
import streamlit as st
import numpy as np


dados = pd.read_excel('./dados/Dados_Saude_SP_2018_2022.xlsx', sheet_name="Base")

despesas = dados.Despesa.unique()
despesas.sort()
anos = dados.Ano.unique()
anos.sort()
municipios = dados.Município.unique()
municipios.sort()

dados = dados[['Ano','Despesa','Município','Total Despesas']]



st.title("Análise de Dados da Saúde de São Paulo")

st.sidebar.title("Menu")
ano = st.sidebar.selectbox("Ano",anos,index=None)
munic = st.sidebar.selectbox("Município",municipios,index=None)

#df = dados.loc[dados.Município==" SAO PAULO"]
df = dados

if ano is not None:
  df = df.loc[df.Ano==ano]

if munic is not None:
  df = df.loc[df.Município==munic]

df

