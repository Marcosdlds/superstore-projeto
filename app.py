import pandas as pd
import joblib
import streamlit as st

# Carrega o modelo treinado
model = joblib.load('./src/models/regressor.joblib')

# Carrega os dados
df = pd.read_csv('./data/superstore.xlsx')  # Arquivo é .csv, mesmo com nome .xlsx
df['Order Date'] = pd.to_datetime(df['Order Date'], format='%d/%m/%Y')

# Extrai informações de data
df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.month
df['DayOfWeek'] = df['Order Date'].dt.dayofweek
df['DayOfYear'] = df['Order Date'].dt.dayofyear

# Aplica one-hot encoding
encoded_df = pd.get_dummies(df[['Category', 'Sub-Category', 'Region']], drop_first=True)
df = pd.concat([df, encoded_df], axis=1)

# Define os filtros na interface
st.set_page_config(page_title='Previsão de Vendas - Superstore', layout='wide')
st.title('📈 Previsão de Vendas - Superstore')

st.sidebar.header('🎯 Filtros de Entrada')
selected_year = st.sidebar.selectbox('Ano', sorted(df['Year'].unique()))
selected_region = st.sidebar.selectbox('Região', df['Region'].unique())
selected_category = st.sidebar.selectbox('Categoria', df['Category'].unique())
selected_subcategory = st.sidebar.selectbox('Sub-Categoria', df['Sub-Category'].unique())
delivery_days = st.sidebar.slider('Dias para Entrega', 1, 30, 7)

# Filtra o DataFrame de acordo com os filtros selecionados
filtered_df = df[(df['Year'] == selected_year) &
                 (df['Region'] == selected_region) &
                 (df['Category'] == selected_category) &
                 (df['Sub-Category'] == selected_subcategory)].copy()

if not filtered_df.empty:
    # Adiciona a coluna de input manual
    filtered_df['Delivery Days'] = delivery_days

    # Seleciona as colunas usadas pelo modelo
    feature_columns = [
        'Delivery Days',
        'Category_Office Supplies',
        'Category_Technology',
        'Sub-Category_Appliances',
        'Sub-Category_Art',
        'Sub-Category_Binders',
        'Sub-Category_Bookcases',
        'Sub-Category_Chairs',
        'Sub-Category_Copiers',
        'Sub-Category_Envelopes',
        'Sub-Category_Fasteners',
        'Sub-Category_Furnishings',
        'Sub-Category_Labels',
        'Sub-Category_Machines',
        'Sub-Category_Paper',
        'Sub-Category_Phones',
        'Sub-Category_Storage',
        'Sub-Category_Supplies',
        'Sub-Category_Tables',
        'Region_East',
        'Region_South',
        'Region_West'
    ]

    # Garante que todas as colunas estejam presentes
    for col in feature_columns:
        if col not in filtered_df.columns:
            filtered_df[col] = 0  # Adiciona coluna faltante com 0

    # Cria um DataFrame com os nomes das colunas corretos
    input_data = pd.DataFrame([filtered_df[feature_columns].iloc[0].values], columns=feature_columns)

    # *** ADICIONANDO ESTAS LINHAS PARA INSPEÇÃO (CORRIGIDO) ***
    print("Nomes das colunas de input_data:", input_data.columns.tolist())
    print("Valores de input_data:", input_data.values)

    with st.spinner('Calculando previsão...'):
        prediction = model.predict(input_data)[0]
        st.success(f'💰 Previsão de Vendas: **${prediction:.2f}**')

    # Mostra dados selecionados
    st.markdown("### 📋 Detalhes do Registro Selecionado")
    st.dataframe(filtered_df[['Order Date', 'Region', 'Category', 'Sub-Category', 'Delivery Days']])
else:
    st.warning('⚠️ Nenhum dado encontrado com os filtros selecionados.')