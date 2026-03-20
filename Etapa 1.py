import pandas as pd

df = pd.read_excel("dataset_desafio_trainees.xlsx")

print("=" * 55)
print("DIMENSÕES DO DATASET")
print("=" * 55)
print(f"Linhas  : {df.shape[0]}")
print(f"Colunas : {df.shape[1]}")
print(f"Nomes   : {df.columns.tolist()}")

print("\n" + "=" * 55)
print("TIPOS DE VARIÁVEIS")
print("=" * 55)
print("Numéricas  :", df.select_dtypes(include="number").columns.tolist())
print("Categóricas:", df.select_dtypes(exclude="number").columns.tolist())

nota = df["nota_final"]

print("\n" + "=" * 55)
print("ESTATÍSTICAS DA NOTA FINAL")
print("=" * 55)
print(f"Média   : {nota.mean():.2f}")
print(f"Mediana : {nota.median():.2f}")
print(f"Moda    : {nota.mode()[0]}")
print(f"Q1      : {nota.quantile(0.25)}")
print(f"Q2      : {nota.quantile(0.50)}")
print(f"Q3      : {nota.quantile(0.75)}")
print(f"Mínimo  : {nota.min()}")
print(f"Máximo  : {nota.max()}")

print("\n" + "=" * 55)
print("PRÉVIA DOS DADOS (5 primeiras linhas)")
print("=" * 55)
print(df.head().to_string(index=False))

print("\n" + "=" * 55)
print("VALORES NULOS POR COLUNA")
print("=" * 55)
print(df.isnull().sum())
