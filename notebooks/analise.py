import pandas as pd

df = pd.read_csv('data/transacoes.csv')

suspeitas = df[(df['valor'] >= 5000) | (df['score_risco'] > 80)]

print("Total de transações:", len(df))
print("Total de transações suspeitas:", len(suspeitas))
print("\nTransações suspeitas:")
print(suspeitas)

percentual = (len(suspeitas) / len(df)) * 100
print(f"\nPercentual de transações suspeitas: {percentual:.2f}%")