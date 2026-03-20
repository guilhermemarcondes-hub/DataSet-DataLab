import pandas as pd

df = pd.read_excel("dataset_desafio_trainees.xlsx")

grupo_ate_10h  = df[df["horas_estudo"] <= 10]["nota_final"]
grupo_mais_10h = df[df["horas_estudo"] > 10]["nota_final"]

print("=" * 58)
print("SELEÇÃO DE AMOSTRAS – TESTE DE HIPÓTESE")
print("=" * 58)
print(f"\nHipótese: Alunos com > 10h/semana têm nota média maior.\n")

print(f"{'Métrica':<22} {'Grupo ≤ 10h':>15} {'Grupo > 10h':>15}")
print("-" * 55)
print(f"{'Tamanho (n)':<22} {len(grupo_ate_10h):>15} {len(grupo_mais_10h):>15}")
print(f"{'Média':<22} {grupo_ate_10h.mean():>15.2f} {grupo_mais_10h.mean():>15.2f}")
print(f"{'Mediana':<22} {grupo_ate_10h.median():>15.2f} {grupo_mais_10h.median():>15.2f}")
print(f"{'Desvio Padrão':<22} {grupo_ate_10h.std():>15.2f} {grupo_mais_10h.std():>15.2f}")
print(f"{'Mínimo':<22} {grupo_ate_10h.min():>15} {grupo_mais_10h.min():>15}")
print(f"{'Máximo':<22} {grupo_ate_10h.max():>15} {grupo_mais_10h.max():>15}")

diferenca = grupo_mais_10h.mean() - grupo_ate_10h.mean()
print(f"\nDiferença entre médias: {diferenca:.2f} pontos")

print("\n" + "=" * 58)
print("JUSTIFICATIVA DA ESCOLHA DAS AMOSTRAS")
print("=" * 58)
print("""
Tipo de teste escolhido: Teste t de Student (amostras independentes)
ou Mann-Whitney U caso a normalidade não seja garantida.

Motivo da escolha:
  - A hipótese compara dois grupos distintos sem relação entre si,
    já que um aluno não pertence a ambos simultaneamente.
  - Isso caracteriza amostras independentes, ou seja, não pareadas.
  - O objetivo é comparar a média da nota_final entre os grupos,
    e o Teste t para amostras independentes é o mais adequado
    quando os dados seguem distribuição aproximadamente normal.
  - Se a normalidade não for verificada, o Mann-Whitney U
    é a alternativa não-paramétrica recomendada.

Critério de corte utilizado: horas_estudo > 10 (conforme enunciado).
""")
