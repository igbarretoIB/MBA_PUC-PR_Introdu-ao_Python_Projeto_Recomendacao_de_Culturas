# Importando as bibliotecas
import streamlit as st
import os
import time
from joblib import dump, load
import pandas as pd
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
import numpy as np
from sklearn.ensemble import RandomForestClassifier






if not 'N_select' in st.session_state:
    st.session_state['N_select']=[]

if not 'P_select' in st.session_state:
    st.session_state['P_select']=[]

if not 'K_select' in st.session_state:
    st.session_state['K_select']=[]

if not 'pH_select' in st.session_state:
    st.session_state['pH_select']=[]

if not 'Temperatura_select' in st.session_state:
    st.session_state['Temperatura_select']=[]

if not 'Umidade_select' in st.session_state:
    st.session_state['Umidade_select']=[]

if not 'Precipitacao_select' in st.session_state:
    st.session_state['Precipitacao_select']=[]

if not 'scaler' in st.session_state:
    st.session_state['scaler']={}

if not 'culturas' in st.session_state:
    st.session_state['culturas']={}


if not 'dados_area' in st.session_state:
    st.session_state['dados_area']=''

if not 'predictions' in st.session_state:
    st.session_state['predictions']=[]

if not 'pred' in st.session_state:
    st.session_state['pred']=[]

if not 'variaveis' in st.session_state:
    st.session_state['variaveis']={}




st.set_page_config(page_title= 'Recomendação de Culruras Agrícolas', page_icon =':ear_of_rice:')

st.subheader('Recomendação de Culruras Agrícolas :ear_of_rice:')
st.write('')

time.sleep(2)
st.subheader(" :male-farmer: Qual a melhor cultura para você...")
time.sleep(2)
st.subheader(" :male-farmer: Por favor, preencha os campos abaixo de N, P, K, pH, Temperatura, Umidade e Precipitação")


# Carrega os dados do dataset
crop_recomendation = pd.read_csv('Crop_recommendation.csv', sep= ',')
colunas = list(crop_recomendation.columns)

# Realiza o scalling dos dados 
X_df= crop_recomendation.drop('label', axis=1)
st.session_state.scaler = preprocessing.StandardScaler()
df_scale = st.session_state.scaler.fit_transform(X_df)
# Carrega o modelo do random forest 
st.session_state.modelo=  load('random_forest_model.joblib')


st.session_state.culturas={ 'rice':'Arroz :ear_of_rice:', 
        'maize': 'Milho :corn:', 
        'chickpea':'Grão de bico 🥔', 
        'kidneybeans': 'Feijão 🫘', 
        'pigeonpeas':'Feijão guandú 🫛',
        'mothbeans':'Feijão mariposa 🫘', 
        'mungbean':'Feijão mungu 🫘', 
        'blackgram':'Grama preta   🌿  ', 
        'lentil':'Lentilha 🫛 ', 
        'pomegranate':'Romã 🍅',
        'banana':'Banana ', 
        'mango':'Morango 🍓', 
        'grapes':'Uva 🍇 ', 
        'watermelon': 'Melância :watermelon:', 
        'muskmelon':'Melão 🍈 ', 
        'apple':'Maçã 🍎',
        'orange':'Laranja :tangerine:', 
        'papaya':'Mamão  🏉', 
        'coconut':'Coco :coconut:', 
        'cotton':'Algodão ☁️', 
        'jute':'Juta 🌿', 
        'coffe':'Café ☕',
        'mango': 'Manga 🥭'
    
        }


st.session_state.variaveis={}
if N:= st.text_input('Nitrogênio(N) (aperte o Enter após inserir a variável)'):
    try:
        N_float = float(N)
        st.session_state.N_select = [N_float]
        st.session_state.predictions =[]
        st.session_state.dados_area=''
    except ValueError:
        st.write(':male-farmer: Digite apenas valores numéricos!')
    



if P:= st.text_input('Fósforo (P) (aperte o Enter após inserir a variável)'):
    try:
        P_float= float(P)
        st.session_state.P_select=[P_float]
        st.session_state.predictions =[]
        st.session_state.dados_area=''

    except ValueError:
        st.write(':male-farmer: Digite apenas valores numéricos!')
    
   

if K:= st.text_input('Potássio(K) (aperte o Enter após inserir a variável)'):
    try:
        K_float= float(K)
        st.session_state.K_select=[K_float]
        st.session_state.predictions =[]
        st.session_state.dados_area=''

    except ValueError:
        st.write(':male-farmer: Digite apenas valores numéricos!')
 

if Temperatura:= st.text_input('Temperatura(ºC) (aperte o Enter após inserir a variável)', value=""):
    try:
        Temperatura_float= float(Temperatura)
        st.session_state.Temperatura_select=[Temperatura_float]
        st.session_state.predictions =[]
        st.session_state.dados_area=''

    except ValueError:
        st.write(':male-farmer: Digite apenas valores numéricos!')
   
   

if Umidade:= st.text_input('Umidade(%) (aperte o Enter após inserir a variável)', value=""):
    try:
        Umidade_float= float(Umidade)
        st.session_state.Umidade_select=[Umidade_float]
        st.session_state.predictions =[]
        st.session_state.dados_area=''

    except ValueError:
        st.write(':male-farmer: Digite apenas valores numéricos!')

if pH:= st.text_input('pH (aperte o Enter após inserir a variável)' ):
    try:
        pH_float= float(pH)
        st.session_state.pH_select=[pH_float]
        st.session_state.predictions =[]
        st.session_state.dados_area=''

    except ValueError:
        st.write(':male-farmer: Digite apenas valores numéricos!')

if Precipitacao:= st.text_input('Precipitação(mm) (aperte o Enter após inserir a variável)'):
    try:
        Precipitacao_float= float(Precipitacao)
        st.session_state.Precipitacao_select=[Precipitacao_float]
        st.session_state.predictions =[]
        st.session_state.dados_area=''

    except ValueError:
        st.write(':male-farmer: Digite apenas valores numéricos!')

st.session_state.variaveis['N']=st.session_state.N_select
st.session_state.variaveis['P']=st.session_state.P_select
st.session_state.variaveis['K']=st.session_state.K_select
st.session_state.variaveis['temperature']=st.session_state.Temperatura_select
st.session_state.variaveis['humidity']=st.session_state.Umidade_select
st.session_state.variaveis['ph']=st.session_state.pH_select
st.session_state.variaveis['rainfall']=st.session_state.Precipitacao_select

print(st.session_state.variaveis)

if all(v for v in st.session_state.variaveis.values()):
    pred =[]
    print("Todas as listas estão preenchidas.")
    st.session_state.dados_area= pd.DataFrame(st.session_state.variaveis)
    print(st.session_state.dados_area.shape)
    colunas= st.session_state.dados_area.columns

    st.session_state.dados_area = st.session_state.scaler.transform(st.session_state.dados_area)
    st.session_state.dados_area=pd.DataFrame(st.session_state.dados_area, columns=colunas)
    st.session_state.pred=[1]
else:
    pass

if st.button('Recomendar Cultura'):
    if len(st.session_state.pred)==1:
        st.session_state.predictions = st.session_state.modelo.predict(st.session_state.dados_area).tolist()
    else:
        pass


if len(st.session_state.predictions)>0:
    cultura_ = st.session_state.culturas.get(st.session_state.predictions[0])
    print(cultura_)
    st.subheader(f':male-farmer: A Cultura recomendada para as suas condições é:')
    st.subheader(f'{cultura_}')
else:
    st.write(f':male-farmer: Preencha os dados acima para prever a melhor cultura para suas condições')


with st.sidebar:
    
    if st.button(':broom: Limpar dados'):
        st.session_state.predictions=[]
        st.session_state.variaveis={}
        st.session_state.N_select=[]
        st.session_state.P_select=[]
        st.session_state.K_select=[]
        st.session_state.Temperatura_select=[]
        st.session_state.Umidade_select=[]
        st.session_state.pH_select=[]
        st.session_state.Precipitacao_select=[]
        st.session_state.dados_area=[] 