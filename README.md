# 📊 Desafio Trainees — Análise de Dados Educacionais

Projeto desenvolvido como parte do Desafio Trainees, com o objetivo de analisar dados de alunos e prever a nota final com base em hábitos de estudo e características observáveis.

---

## 📁 Arquivos do Repositório

| Arquivo | Descrição |
|---|---|
| [📄 Relatorio e Respostas.pdf](./Relatorio%20e%20Respostas.pdf) | Relatório completo com interpretações e respostas de todas as etapas |
| [📊 Planilha - Estapas e Dados.xlsx](./Planilha%20-%20Estapas%20e%20Dados.xlsx) | Planilha com dataset, estatísticas, correlações e análise dos grupos |
| [🐍 Etapa 1.py](./Etapa%201.py) | Exploração do dataset com pandas |
| [🐍 Etapa 2.py](./Etapa%202.py) | Estatística descritiva com NumPy |
| [🐍 Etapa 3.py](./Etapa%203.py) | Análise de correlação entre variáveis |
| [🐍 Etapa 4.py](./Etapa%204.py) | Seleção de amostras para teste de hipótese |
| [🐍 Etapa 5.py](./Etapa%205.py) | Regressão linear com scikit-learn |

---

## 🗂️ Sobre o Dataset

O dataset contém informações de **86 alunos** com as seguintes variáveis:

| Variável | Tipo | Descrição |
|---|---|---|
| `nome_aluno` | Categórica | Nome completo do aluno |
| `matricula` | Numérica | Código de matrícula |
| `email` | Categórica | Endereço de e-mail |
| `horas_estudo` | Numérica | Horas de estudo por semana |
| `aulas_assistidas` | Numérica | Quantidade de aulas assistidas |
| `faltas` | Numérica | Número de faltas no período |
| `nota_final` | Numérica | Nota final do aluno *(variável-alvo)* |

---

## 🔢 Etapas do Desafio

### Etapa 1 — Exploração do Dataset
Familiarização com os dados, identificação dos tipos de variáveis e cálculo de estatísticas básicas como média, mediana, moda e quartis, utilizando Excel e Python.

### Etapa 2 — Estatística Descritiva com NumPy
Cálculo de média, mediana, desvio padrão e quartis com NumPy, seguido de comparação direta com os resultados obtidos no Excel para validar a consistência.

### Etapa 3 — Análise de Correlação
Cálculo das correlações entre horas de estudo, aulas assistidas e faltas em relação à nota final, com interpretação da força e direção de cada relação.

### Etapa 4 — Teste de Hipótese
Separação dos alunos em dois grupos (≤ 10h e > 10h de estudo por semana) com justificativa da escolha amostral e do teste estatístico mais adequado.

### Etapa 5 — Regressão Linear 
Implementação de regressão linear com `scikit-learn`, avaliação do modelo com as métricas MSE, MAE e R² Score, e comparação entre valores reais e preditos.

---

## 📈 Principais Resultados

- **Correlação** entre horas de estudo e nota final: **0,997** — relação quase linear
- **Diferença de média** entre grupos (≤10h vs >10h): **24,46 pontos**
- **R² Score** do modelo de regressão: **0,998** — o modelo explica 99,8% da variação nas notas

---

## ▶️ Como Executar os Scripts

Certifique-se de ter o Python instalado com as bibliotecas necessárias:

```bash
pip install pandas numpy scikit-learn openpyxl
```

Execute cada etapa individualmente:

```bash
python "Etapa 1.py"
python "Etapa 2.py"
python "Etapa 3.py"
python "Etapa 4.py"
python "Etapa 5.py"
```

> Todos os scripts devem estar na mesma pasta que o arquivo `dataset_desafio_trainees.xlsx`.
