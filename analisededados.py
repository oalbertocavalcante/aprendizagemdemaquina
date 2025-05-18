import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carrega o dataset
url = "https://raw.githubusercontent.com/oalbertocavalcante/aprendizagemdemaquina/main/iris.csv"
df = pd.read_csv(url)

# Mostra as 5 primeiras linhas do dataset
print(df.head())

# Gráfico 1 - Relação entre comprimento e largura das pétalas, colorido por espécie
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x="petal_length", y="petal_width", hue="species", palette="Set1")
plt.title("Pétala - Comprimento x Largura")
plt.grid(True)
plt.show()

# Gráfico 2 - Boxplot para comparar distribuições de sépalas

plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x="species", y="sepal_length", palette="Set2")
plt.title("Comprimento da Sépala por Espécie")
plt.grid(True)
plt.show()

# Gráfico 3 - Matriz de correlação

sns.pairplot(df, hue="species", palette="Set1")
plt.suptitle("Relações entre Atributos", y=1.02)
plt.show()

