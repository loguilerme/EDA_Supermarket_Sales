import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Substitua 'arquivo.csv' pelo caminho do seu ficheiro CSV
caminho_arquivo = "D:\\Udemy\\python\\Sales\\archive\\supermarket_sales.csv"

# Importar o CSV para um DataFrame
df = pd.read_csv(caminho_arquivo, sep=",")

##DATA UNDERSTANDING

# Exibir as primeiras linhas do DataFrame
print(df.head())
print(df.describe())
#Verificar informações sobre as colunas 


##-------------------------------
##DATA PREPARATION
#Mudar coluna date para tipo de dados de data
df['Date'] = pd.to_datetime(df['Date'])


#Eliminar as colunas que não são necessárias para responder às questões
df.drop(['Tax 5%','gross margin percentage','cogs','Time'], axis="columns")
df.info()
print('--------------------------')
##-------------------------------------
#Determinar qual é o Branch que gera mais valor 
print('DETERMINAR QUAL É O BRANCH QUE GERA MAIS GROSS INCOME')
branch_gross_income=df.groupby('Branch')['gross income'].sum()
print(branch_gross_income)
print('--------------------------')
#Determinar qual é o brunch que tem mais quantidade de produtos vendidos
print('DETERMINAR QUAL É O BRANCH QUE TEM MAIS QUANTIDADE DE PRODUTOS VENDIDOS')
branch_quantity =df.groupby('Branch')['Quantity'].sum()
print(branch_quantity)
print('--------------------------')
#Determinar a média de income por cada fatura em cada branch
print('DETERMINAR QUAL É A MÉDIA DE GROSS INCOME POR CADA FATURA')
branch_avg_gross_income=df.groupby('Branch')['gross income'].mean()
print(branch_avg_gross_income)
print('--------------------------')
#Determinar qual é o branch que está melhor avaliado
print('DETERMINAR QUAL É O BRANCH QUE ESTÁ MELHOR AVALIADO')
branch_rating = df.groupby('Branch')['Rating'].mean()
print(branch_rating)
#Determinar qual é o metodo de pagamento mais utilizado
print('DETERMINAR QUAL É O METODO DE PAGAMENTO MAIS UTILIZADO')
payment_method = df['Payment'].value_counts()
print(payment_method)

#Análise de clientes
print('ANALISE DE CLIENTES')
customers = df.groupby('Gender')['Customer type'].value_counts()
print(customers)

#Product lines
print('Quais as product lines que tem mais quantidade de produtos vendidos')
product_type_amounts = df.groupby('Product line')['Quantity'].sum()
print(product_type_amounts)


#agrupar as vendas por dia
sales_by_day = df.groupby('Date')['Total'].sum()
# Plot
plt.figure(figsize=(12, 4))
plt.plot(sales_by_day, marker="o")

plt.title("Sales Trend Over 3 Months", fontsize=14, fontweight="bold")
plt.xlabel("Date", fontsize=14)
plt.ylabel("Total Sales", fontsize=14)

plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.xticks(rotation=45)
plt.show()

