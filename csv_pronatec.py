#!/usr/bin/env python
# coding: utf-8

# # Análise das Unidades da Rede Federal
# 
# URL: http://dadosabertos.mec.gov.br/images/conteudo/pronatec/Unidades_da_Rede_Federal_de_EPCT.csv
# 

# In[1]:


# Importação de bibliotecas
import pandas as pd


# In[13]:


#Importando o arquivo
arq = "Unidades_da_Rede_Federal_de_EPCT.csv"

# Leitura do arquivo csv
df = pd.read_csv(arq, sep = ",", encoding = "utf-8", header = 0)

# Mostra as 5 primeiras linhas do Dataframe
df.head()


# In[11]:


#Mostra o detalhe do Dataframe
df.describe()


# In[15]:


#Conta a quantidade únicos de registros por coluna
df.count()


# In[19]:


# Mostra o tipo de dados por colunas
df.dtypes


# In[20]:


# Mostra a quantidade de linhas e colunas, respectivamente
df.shape


# In[22]:


# Quantas escolas existem por UF
df['sigla_uf_unidade_ensino'].value_counts()


# In[74]:


#Mostrando os dados em gráficos
#Informar que queremos ver o gráfico no próprio jupiter notebook
get_ipython().run_line_magic('matplotlib', 'inline')

#Primeira forma de mostrar o gráfico de barras
df['sigla_uf_unidade_ensino'].value_counts().plot(kind="bar", title="Escolas por UF", legend=True)


# In[71]:


#Segunda forma de mostrar o gráfico de barra
df['sigla_uf_unidade_ensino'].value_counts().plot.bar(title="Estado por UF", legend=True, color="green")


# In[ ]:




