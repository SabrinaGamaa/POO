import pandas as pd
pd.set_option('display.max_columns', None)
arquivo = 'salarios.csv'
df = pd.read_csv(arquivo)

df.head()

print(df['Position Title'].value_counts())





