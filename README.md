# 📊 Desafio Trainees — Análise de Dados Educacionais

Projeto desenvolvido como parte do Desafio Trainees, com o objetivo de prever a nota final de alunos com base em hábitos de estudo e características observáveis.

---

## 📁 Arquivos

- [📄 Relatório Completo (Word)](./Relatorio_Desafio_Trainees.docx)
- [📊 Planilha de Estatísticas (Excel)](./Etapa1_Estatisticas.xlsx)

---

## 🗂️ Estrutura do Projeto

```
📦 desafio-trainees
├── 📄 Relatorio_Desafio_Trainees.docx
├── 📊 Etapa1_Estatisticas.xlsx
├── 📊 dataset_desafio_trainees.xlsx
├── 🐍 etapa1_exploracao.py
├── 🐍 etapa2_numpy.py
├── 🐍 etapa3_correlacao.py
├── 🐍 etapa4_hipotese.py
└── 🐍 etapa5_regressao.py
```

---

## 🔢 Etapas

### Etapa 1 — Exploração do Dataset
Familiarização com os dados, identificação de tipos de variáveis e cálculo de estatísticas básicas (média, mediana, moda, quartis) via Excel e Python.

### Etapa 2 — Estatística Descritiva com NumPy
Cálculo de média, mediana, desvio padrão e quartis utilizando NumPy, com comparação direta dos resultados obtidos no Excel.

### Etapa 3 — Análise de Correlação
Cálculo das correlações entre horas de estudo, aulas assistidas e faltas em relação à nota final.

### Etapa 4 — Teste de Hipótese
Separação dos alunos em dois grupos (≤ 10h e > 10h de estudo por semana) com justificativa da escolha amostral.

### Etapa 5 — Regressão Linear *(opcional)*
Implementação de regressão linear com `sklearn`, avaliação do modelo com MSE, MAE e R² Score.

---

## ▶️ Como Executar

Certifique-se de ter o Python instalado com as bibliotecas necessárias:

```bash
pip install pandas numpy scikit-learn openpyxl
```

Execute cada etapa individualmente:

```bash
python etapa1_exploracao.py
python etapa2_numpy.py
python etapa3_correlacao.py
python etapa4_hipotese.py
python etapa5_regressao.py
```

> Todos os scripts devem estar na mesma pasta que o arquivo `dataset_desafio_trainees.xlsx`.
