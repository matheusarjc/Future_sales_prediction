import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel('dados_MAC_Clothes.xlsx')

pd.set_option('display.max_columns', None)

# Fazendo uma cópia do DataFrame
df_original = df.copy()

# Removendo a coluna Date
df = df.drop(['Date'], axis=1)
# Obtém estatísticas descritivas para as colunas numéricas
print(df.describe())

# Verificando as primeiras linhas do DataFrame
print(df.head())

# Verificando o tipo das variáveis
print(df.info())

# Estatísticas descritivas
print(df.describe())
