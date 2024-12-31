import pandas as pd
pd.set_option('display.max_columns', None)
arquivo = '/Users/Sabrina Gama/Downloads/python/POO/manipulacao-de-arquivo-2/arquivos/salarios.csv'
df = pd.read_csv(arquivo)

df.head()

print(df['Position Title'].value_counts())





