import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Configura visualização
sns.set(style="whitegrid")

# Carrega os dados tratados
df = pd.read_csv('./data/superstore.xlsx')
df['Order Date'] = pd.to_datetime(df['Order Date'], format='%d/%m/%Y')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], format='%d/%m/%Y')
df['Delivery Days'] = (df['Ship Date'] - df['Order Date']).dt.days
df['Postal Code'] = df['Postal Code'].fillna(0)

# 1. Vendas por Categoria
plt.figure(figsize=(8, 5))
sns.barplot(data=df, x='Category', y='Sales', estimator=sum)
plt.title("Total de Vendas por Categoria")
plt.tight_layout()
plt.show()

# 2. Vendas por Região
plt.figure(figsize=(8, 5))
sns.barplot(data=df, x='Region', y='Sales', estimator=sum)
plt.title("Total de Vendas por Região")
plt.tight_layout()
plt.show()

# 3. Distribuição de Vendas
plt.figure(figsize=(8, 5))
sns.histplot(df['Sales'], bins=50, kde=True)
plt.title("Distribuição de Vendas")
plt.tight_layout()
plt.show()

# 4. Correlação entre variáveis numéricas
plt.figure(figsize=(8, 6))
sns.heatmap(df[['Sales', 'Postal Code', 'Delivery Days']].corr(), annot=True, cmap='coolwarm')
plt.title("Correlação entre Variáveis Numéricas")
plt.tight_layout()
plt.show()