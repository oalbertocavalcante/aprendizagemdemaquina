# 📊 Atividade Ativa – Análise Visual do Dataset Iris

---

## 1. 📝 Descrição

Nesta atividade, você atuará como cientista de dados em uma empresa de **biotecnologia**, que busca desenvolver um sistema inteligente para **identificar automaticamente espécies de flores** com base em características físicas.

Antes da aplicação de qualquer modelo de Machine Learning, será realizada uma **análise visual exploratória** com o objetivo de:

- Compreender padrões nos dados
- Identificar os atributos mais relevantes
- Justificar as escolhas com base em evidências gráficas

---

## 2. 🧩 Situação-Problema

A empresa está criando um aplicativo de **identificação de flores via IA**, que auxiliará **biólogos e jardineiros**. Sua missão como parte da equipe de dados é:

- Analisar o conjunto de dados `iris.csv`
- Identificar atributos relevantes para distinguir as espécies (Setosa, Versicolor, Virginica)
- Propor um modelo adequado de machine learning com base na análise

### 🧐 Perguntas Norteadoras

- Quais atributos são mais relevantes para distinguir as espécies?
- Existem padrões claros entre as classes?
- Há sobreposição entre espécies em algum gráfico?
- Que tipo de modelo você recomendaria e por quê?

---

## 3. 🎯 Objetivos

### 3.1 Geral

Explorar visualmente o conjunto de dados **Iris** para identificar padrões entre espécies de flores.

### 3.2 Específicos

- 📊 Desenvolver habilidades de visualização e interpretação de dados
- 🧠 Estimular o pensamento crítico na escolha de atributos e modelos
- 🔍 Compreender a importância da análise exploratória
- 🤖 Relacionar teoria com a prática em Machine Learning

---

## 4. ⚙️ Atividade

### 4.1 Requisitos

- Python instalado ou uso do [Google Colab](https://colab.research.google.com/drive/1Hijw59F8Bz9EQqi0HQRRsyZ-dEr4dIcy?usp=sharing)
- Bibliotecas: `pandas`, `matplotlib`, `seaborn`

### 4.2 Execução

1. **Carregamento do dataset:**
   ```python
   import pandas as pd
   url = "https://raw.githubusercontent.com/oalbertocavalcante/aprendizagemdemaquina/main/iris.csv"
   df = pd.read_csv(url)
   ```
