Perfeito! Agora que você já confirmou o nome do seu usuário no GitHub, aqui está como o `README.md` atualizado deve ficar, já com o link correto para o seu repositório:

---

```markdown
# 📈 Previsão de Vendas - Superstore

Aplicação interativa desenvolvida em Python com Streamlit, que permite filtrar dados de vendas e realizar predições com base em variáveis como região, categoria e tempo de entrega.

---

## 🚀 Tecnologias Utilizadas

- Python 3.10+
- Pandas
- Streamlit
- Scikit-learn
- Joblib

---

## 📦 Instalação e Execução Local

1. Clone este repositório:
```bash
git clone https://github.com/Marcosdlds/superstore-projeto.git
```

2. Acesse a pasta do projeto:
```bash
cd superstore-projeto
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Execute a aplicação:
```bash
streamlit run app.py
```

---

## 📊 Sobre o Projeto

Este projeto utiliza dados do [Superstore Sales Dataset](https://www.kaggle.com/datasets/rohitsahoo/sales-forecasting) e aplica técnicas de análise de dados e machine learning para prever o valor de vendas com base em variáveis filtradas pelo usuário, como:

- Região
- Categoria e Subcategoria
- Dias para entrega

---

## 🧠 Previsão com Machine Learning

O modelo de regressão foi treinado utilizando `scikit-learn` e salvo com `joblib`. A previsão é realizada com base em variáveis transformadas via one-hot encoding e variáveis temporais derivadas da data do pedido.

---

## 📂 Estrutura do Projeto

```
superstore-projeto/
│
├── app.py                  # Aplicação principal (Streamlit)
├── src/
│   ├── modeling.py         # Script de modelagem e salvamento do modelo
│   └── models/
│       └── regressor.joblib # Modelo treinado
├── data/
│   └── superstore.csv      # Base de dados
├── requirements.txt        # Dependências do projeto
└── README.md
```

---

## 📬 Contato

Projeto desenvolvido por [Marcosdlds](https://github.com/Marcosdlds) 🚀
```