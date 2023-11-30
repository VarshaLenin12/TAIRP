# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
from google.colab import drive
drive.mount('/content/drive')

# Display basic information about the dataset
df=pd.read_csv('/content/drive/MyDrive/e_commerce/Amazon Sale Report.csv')

df.head()
print(df.info())

df['Amount'].fillna(df['Amount'].median(), inplace=True)

# Data Cleaning
# 1. Check for Missing Values
print(df.isnull().sum())

# 2. Remove Unnecessary Columns
column_to_drop = ['Unnamed: 22']
df = df.drop(columns=column_to_drop, axis=1)

# 3. Convert 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Exploratory Data Analysis (EDA)
# 1. Customer Demographics
plt.figure(figsize=(15, 6)) 
sns.countplot(x='ship-state', data=df)
plt.title('Distribution of Customers by State')
plt.xticks(rotation=45, ha='right')  
plt.show()

# 2. Purchase Patterns
df['Month'] = df['Date'].dt.month
sns.countplot(x='Month', data=df)
plt.title('Monthly Purchase Patterns')
plt.show()

# 3. Popular Products
top_products = df['SKU'].value_counts().head(5)
print('Top 5 Products:\n', top_products)

# Time Series Analysis
# 1. Sales Trends Over Time
df.set_index('Date', inplace=True)
df.resample('M').sum()['Amount'].plot()
plt.title('Monthly Sales Trends')
plt.show()

# 2. Peak Sales Periods
daily_sales = df.resample('D').sum()['Amount']
peak_sales_day = daily_sales.idxmax()
print('Peak Sales Day:', peak_sales_day)

# Statistical Analysis
# 1. Correlation Analysis
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

