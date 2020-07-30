#!/usr/bin/env python
# coding: utf-8

# # Análise dos dados do Auxilio Emergencial - 2020
# 
# ### Arquivos : Abril/Maio/Junho
# 
# ##### Origem :  http://www.portaltransparencia.gov.br/pagina-interna/603519-download-de-dados-auxilio-emergencial
# 

# In[1]:


import pandas as pd
import numpy as np

get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


# Importando o arquivo 
arquivo = '202004_AuxilioEmergencial.csv'

# Lendo o arquivo csv 
aux = pd.read_csv(arquivo, encoding = "latin", sep = ";", header = 0, nrows = 2000)

aux.head()


# In[3]:


# Detalhe da consulta
aux.describe()


# In[4]:


# Quantidade de linhas e colunas
aux.shape


# In[5]:


# Retirando as colunas que não serão usadas
# Limitando a quantidade de linhas que serão lidas
aux_resumo = pd.read_csv(arquivo, encoding = "latin", sep = ";", header = 0, nrows = 8000000, usecols = ['UF', 'NOME MUNICÍPIO','NOME BENEFICIÁRIO','ENQUADRAMENTO','VALOR BENEFÍCIO'])
aux_resumo.head()


# In[6]:


# Contando os registros por UF
aux_resumo['UF'].value_counts()


# In[ ]:




