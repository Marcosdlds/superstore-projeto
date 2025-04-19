import pandas as pd

# Caminho do arquivo CSV
file_path = './data/superstore.xlsx'  # Mantenha o nome, mas sabemos que o conteúdo é CSV

try:
    df = pd.read_csv(file_path)
    print("Arquivo CSV lido com sucesso!")
    # Aqui você pode continuar com a análise dos seus dados (usando o DataFrame 'df')
    print(df.head()) # Exibe as primeiras linhas do DataFrame como exemplo
    print("\n📊 Informações do DataFrame:")
    print(df.info())
    print("\n📈 Estatísticas descritivas:")
    print(df.describe(include='all'))
    print("\n🔎 Valores ausentes por coluna:")
    print(df.isnull().sum())

except FileNotFoundError:
    print(f"Erro: O arquivo não foi encontrado no caminho: {file_path}")
except Exception as e:
    print(f"Erro ao ler o arquivo CSV: {e}")
    print("Certifique-se de que o arquivo é realmente um CSV.")

# Lê os dados
df = pd.read_csv('./data/superstore.xlsx')

# Converte colunas de data
df['Order Date'] = pd.to_datetime(df['Order Date'], format='%d/%m/%Y')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], format='%d/%m/%Y')

# Cria nova feature: tempo de envio
df['Delivery Days'] = (df['Ship Date'] - df['Order Date']).dt.days

# Trata valores nulos
df['Postal Code'] = df['Postal Code'].fillna(0)

# Remove colunas que não são úteis para o modelo
df.drop(['Row ID', 'Order ID', 'Customer ID', 'Customer Name', 'Product ID', 'Product Name'], axis=1, inplace=True)

# Mostra os dados tratados
print("✅ Dados prontos para análise!")
print(df.head())
