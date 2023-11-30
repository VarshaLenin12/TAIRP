import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from google.colab import drive
drive.mount('/content/drive')

df=pd.read_csv('/content/drive/MyDrive/IMDb Movies India.csv', encoding='latin1')

df.head()
print(df.info())

plt.figure(figsize=(12, 6))
sns.histplot(df['Rating'], bins=20, kde=True)
plt.title('Distribution of Ratings')
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(12, 6))
sns.histplot(df['Votes'].dropna(), bins=20, kde=True)
plt.title('Distribution of Votes')
plt.xlabel('Votes')
plt.ylabel('Frequency')
plt.xticks(range(0, int(df['Votes'].max()) + 1, 30))
plt.show()

top_rated_movies = df.sort_values(by='Rating', ascending=False).head(10)
print("Top 10 Rated Movies:")
print(top_rated_movies[['Name', 'Rating']])

plt.figure(figsize=(12, 6))
sns.countplot(x='Year', data=df)
plt.title('Number of Movies Released Each Year')
plt.xlabel('Year')
plt.ylabel('Number of Movies')
plt.xticks(rotation=45)
plt.show()

correlation_matrix = df[['Rating', 'Votes']].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=.5)
plt.title('Correlation Matrix: Rating vs Votes')
plt.show()
