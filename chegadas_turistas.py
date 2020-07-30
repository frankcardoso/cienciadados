#!/usr/bin/env python
# coding: utf-8

# # Análise dos dados da chegada de turistas ao Brasil
# ### Ano: 2018 e 2019
# site: http://dados.turismo.gov.br/index.php/chegada-de-turistas-internacionais

# In[1]:


# Importar as bibliotecas
import pandas as pd
import numpy as np

get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


# Importar os dados
# Lendo arquivo csv
arq19 = 'chegadas_2019.csv'

# Detalhando os parametros do arquivo csv( encoding, sep, header)
chegadas = pd.read_csv(arq19, sep=';', encoding='latin', header =0)

chegadas.head()


# In[3]:


# Alterar as os nomes das colunas

chegadas.columns = ['Continente', 'Código Continente', 'País', 'Código País', 'UF', 'Código UF', 'Via', 'Código Via', 'Ano','Mês', 'Código Mês', 'Chegadas']


# In[12]:


chegadas.describe()


# In[65]:


# Quantidade de chegadas por Continente
chegadas_total = chegadas['Continente','Chegadas']
chegadas.groupby(['Continente']).sum()


# In[ ]:




