import pandas as pd

df = pd.read_csv('data/transacoes.csv')

suspeitas = df[(df['valor'] > 5000) | (df['score_risco'] > 80)]

print("Transações suspeitas:")
print(suspeitas)