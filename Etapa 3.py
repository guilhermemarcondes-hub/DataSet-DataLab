import pandas as pd

df = pd.read_excel("dataset_desafio_trainees.xlsx")

corr_horas  = df["horas_estudo"].corr(df["nota_final"])
corr_aulas  = df["aulas_assistidas"].corr(df["nota_final"])
corr_faltas = df["faltas"].corr(df["nota_final"])

def classificar(r):
    magnitude = abs(r)
    sinal = "positiva" if r > 0 else "negativa"
    if magnitude >= 0.9:
        return f"Muito forte ({sinal})"
    elif magnitude >= 0.7:
        return f"Forte ({sinal})"
    elif magnitude >= 0.5:
        return f"Moderada ({sinal})"
    else:
        return f"Fraca ({sinal})"

print("=" * 58)
print("CORRELAÇÃO COM NOTA FINAL")
print("=" * 58)
print(f"{'Variável':<25} {'Correlação (r)':>15} {'Força':>15}")
print("-" * 58)

for var, corr in [("horas_estudo", corr_horas),
                  ("aulas_assistidas", corr_aulas),
                  ("faltas", corr_faltas)]:
    print(f"{var:<25} {corr:>15.4f} {classificar(corr):>15}")

print("\n" + "=" * 58)
print("MATRIZ DE CORRELAÇÃO (VARIÁVEIS NUMÉRICAS RELEVANTES)")
print("=" * 58)
cols = ["horas_estudo", "aulas_assistidas", "faltas", "nota_final"]
print(df[cols].corr().round(4).to_string())
