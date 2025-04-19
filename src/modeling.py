import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import OneHotEncoder
import joblib

# Carrega os dados
df = pd.read_csv('./data/superstore.xlsx')
df['Order Date'] = pd.to_datetime(df['Order Date'], format='%d/%m/%Y')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], format='%d/%m/%Y')
df['Delivery Days'] = (df['Ship Date'] - df['Order Date']).dt.days
df['Postal Code'] = df['Postal Code'].fillna(0)

# Seleciona colunas úteis
df_model = df[['Category', 'Sub-Category', 'Region', 'Delivery Days', 'Sales']]

# Separando X (features) e y (target)
X = df_model.drop('Sales', axis=1)
y = df_model['Sales']

# One-hot encoding nas variáveis categóricas
X_encoded = pd.get_dummies(X, drop_first=True)

# Divide entre treino e teste
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

# Modelo de regressão linear
model = LinearRegression()
print("Nomes das colunas de X_encoded (durante o treinamento):", X_encoded.columns.tolist())
model.fit(X_train, y_train)

# Previsão e avaliação
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"📉 Erro Quadrático Médio (MSE): {mse:.2f}")
print(f"📈 Coeficiente de Determinação (R²): {r2:.2f}")

print(f"Diretório de trabalho atual: {os.getcwd()}")

# Verifica se a pasta 'models' existe e a cria se não existir
if not os.path.exists('./models'):
    os.makedirs('./models')

# Salva o modelo para uso no dashboard
joblib.dump(model, './src/models/regressor.joblib')
print("✅ Modelo salvo com sucesso em './models/regressor.joblib'")