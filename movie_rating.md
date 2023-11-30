#import the necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#mount google drive
from google.colab import drive
drive.mount('/content/drive')

#load the dataset
df=pd.read_csv('/content/drive/MyDrive/IMDb Movies India.csv', encoding='latin1')

#display a few columns of the dataset
df.head()
print(df.info())

#plot a histogram for "rating" attribute
plt.figure(figsize=(12, 6))
sns.histplot(df['Rating'], bins=20, kde=True)
plt.title('Distribution of Ratings')
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.show()

#plot a histogram for the number of votes
plt.figure(figsize=(12, 6))
sns.histplot(df['Votes'].dropna(), bins=20, kde=True)
plt.title('Distribution of Votes')
plt.xlabel('Votes')
plt.ylabel('Frequency')
plt.xticks(range(0, int(df['Votes'].max()) + 1, 30))
plt.show()

#display the highly rated movies
top_rated_movies = df.sort_values(by='Rating', ascending=False).head(10)
print("Top 10 Rated Movies:")
print(top_rated_movies[['Name', 'Rating']])

#plot a countplot to display th number of movies released per year
plt.figure(figsize=(12, 6))
sns.countplot(x='Year', data=df)
plt.title('Number of Movies Released Each Year')
plt.xlabel('Year')
plt.ylabel('Number of Movies')
plt.xticks(rotation=45)
plt.show()

#display the correlation matrix
correlation_matrix = df[['Rating', 'Votes']].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=.5)
plt.title('Correlation Matrix: Rating vs Votes')
plt.show()
