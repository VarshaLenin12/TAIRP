import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from google.colab import drive
drive.mount('/content/drive')

directory_path = '/content/drive/MyDrive/archive (2)'
os.chdir(directory_path)

files = os.listdir()
print(files)

csv_file1 = 'olist_customers_dataset.csv'  
df1 = pd.read_csv(csv_file1)

csv_file2 = 'olist_geolocation_dataset.csv'  
df2 = pd.read_csv(csv_file2)

csv_file3 = 'olist_order_items_dataset.csv'  
df3 = pd.read_csv(csv_file3)

csv_file4 = 'olist_order_payments_dataset.csv'  
df4 = pd.read_csv(csv_file4)

csv_file5 = 'olist_order_reviews_dataset.csv'  
df5 = pd.read_csv(csv_file5)

csv_file6 = 'olist_orders_dataset.csv'  
df6 = pd.read_csv(csv_file6)

csv_file7 = 'olist_products_dataset.csv'  
df7 = pd.read_csv(csv_file7)

csv_file8 = 'olist_sellers_dataset.csv'  
df8 = pd.read_csv(csv_file8)

csv_file9 = 'product_category_name_translation.csv'  
df9 = pd.read_csv(csv_file9)

#to display the dimensions
dimensions=df1.shape
print("Dimensions of the customers dataset: ",dimensions)

#to check summary statistics
summary_stats=df2.describe()
print("Summary statistics of order items dataset:\n",summary_stats)

#to check data types
data_types=df3.info()
print("Missing values of order reviews dataset:\n", data_types)

#to identify correlations
correlation_matrix = df4.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=.5)
plt.title('Correlation Matrix for Order Payments dataset')
plt.show()

df5.head()
print(df5.columns)
columns = ['review_id', 'order_id', 'review_score']
sns.pairplot(df5[columns])
plt.suptitle('Pair Plot of Selected Columns', y=1.02)  
plt.show()

df7.head()
sns.countplot(x='product_length_cm', data=df7)
plt.title('Distribution of Product length')
plt.show()

sns.countplot(x='product_height_cm', data=df7)
plt.title('Distribution of Product height')
plt.show()

df3.head()
df3['freight_value'].hist(bins=20, color='blue', alpha=0.7)
plt.title('Histogram of Freight Value')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

df4.head()
sns.boxplot(x='payment_type', y='payment_installments', data=df4)
plt.title('Box Plot of Payment Installment by Payment Type')
plt.show()

