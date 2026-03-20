import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

df = pd.read_excel("dataset_desafio_trainees.xlsx")

print("=" * 55)
print("INSPEÇÃO DO DATASET")
print("=" * 55)
print(df.describe())
print("\nInfo:")
df.info()
print("\nColunas:", df.columns.tolist())
print("\nTipos:\n", df.dtypes)
print("\nContagem de valores – horas_estudo:")
print(df["horas_estudo"].value_counts().sort_index())

X = df[["horas_estudo", "aulas_assistidas", "faltas"]]
y = df["nota_final"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42
)

print("\n" + "=" * 55)
print("DIVISÃO TREINO / TESTE")
print("=" * 55)
print(f"Total de amostras : {len(df)}")
print(f"Treino            : {len(X_train)} amostras ({len(X_train)/len(df)*100:.0f}%)")
print(f"Teste             : {len(X_test)} amostras  ({len(X_test)/len(df)*100:.0f}%)")

model = LinearRegression()
model.fit(X_train, y_train)

print("\n" + "=" * 55)
print("COEFICIENTES DO MODELO")
print("=" * 55)
print(f"Intercepto  : {model.intercept_:.4f}")
for feat, coef in zip(X.columns, model.coef_):
    print(f"{feat:<22}: {coef:.4f}")

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
r2  = r2_score(y_test, y_pred)

print("\n" + "=" * 55)
print("MÉTRICAS DE AVALIAÇÃO")
print("=" * 55)
print(f"MSE (Mean Squared Error)   : {mse:.4f}")
print(f"MAE (Mean Absolute Error)  : {mae:.4f}")
print(f"R² Score                   : {r2:.4f}")

print("\n" + "=" * 55)
print("REAL vs PREDITO (primeiras 10 amostras do teste)")
print("=" * 55)
resultados = pd.DataFrame({
    "Real":    y_test.values,
    "Predito": y_pred.round(2),
    "Erro":    (y_test.values - y_pred).round(2)
})
print(resultados.head(10).to_string(index=False))
