import pandas as pd
import numpy as np

df = pd.read_excel("dataset_desafio_trainees.xlsx")
arr = df["nota_final"].values

media   = np.mean(arr)
mediana = np.median(arr)
desvio  = np.std(arr, ddof=1)
q1      = np.percentile(arr, 25)
q2      = np.percentile(arr, 50)
q3      = np.percentile(arr, 75)

print("=" * 55)
print("ESTATÍSTICAS COM NUMPY – nota_final")
print("=" * 55)
print(f"Média          : {media:.4f}")
print(f"Mediana        : {mediana:.4f}")
print(f"Desvio padrão  : {desvio:.4f}")
print(f"Q1 (25%)       : {q1}")
print(f"Q2 (50%)       : {q2}")
print(f"Q3 (75%)       : {q3}")

print("\n" + "=" * 55)
print("COMPARAÇÃO: NUMPY vs EXCEL")
print("=" * 55)
print(f"{'Métrica':<18} {'NumPy':>10} {'Excel':>10} {'Igual?':>8}")
print("-" * 50)

excel_values = {
    "Média":   73.67,
    "Mediana": 74.50,
    "Q1":      63.00,
    "Q3":      85.00,
}

numpy_values = {
    "Média":   round(media, 2),
    "Mediana": round(mediana, 2),
    "Q1":      q1,
    "Q3":      q3,
}

for k in excel_values:
    igual = "✓" if abs(numpy_values[k] - excel_values[k]) < 0.01 else "✗"
    print(f"{k:<18} {numpy_values[k]:>10.2f} {excel_values[k]:>10.2f} {igual:>8}")
