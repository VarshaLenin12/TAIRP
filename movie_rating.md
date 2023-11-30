# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Mount Google Drive for dataset access
from google.colab import drive
drive.mount('/content/drive')

# Load the dataset
df = pd.read_csv('/content/drive/MyDrive/IMDb Movies India.csv', encoding='latin1')

# Display basic information about the dataset
df.head()  # Displaying the first few rows of the dataset
print(df.info())  # Displaying summary information about the dataset

# Plot a histogram to visualize the distribution of movie ratings
plt.figure(figsize=(12, 6))
sns.histplot(df['Rating'], bins=20, kde=True)
plt.title('Distribution of Ratings')
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.show()

# Plot a histogram for the number of votes to understand audience engagement
plt.figure(figsize=(12, 6))
sns.histplot(df['Votes'].dropna(), bins=20, kde=True)
plt.title('Distribution of Votes')
plt.xlabel('Votes')
plt.ylabel('Frequency')
plt.xticks(range(0, int(df['Votes'].max()) + 1, 30))
plt.show()

# Identify and display the top-rated movies
top_rated_movies = df.sort_values(by='Rating', ascending=False).head(10)
print("Top 10 Rated Movies:")
print(top_rated_movies[['Name', 'Rating']])

# Plot a countplot to visualize the number of movies released each year
plt.figure(figsize=(12, 6))
sns.countplot(x='Year', data=df)
plt.title('Number of Movies Released Each Year')
plt.xlabel('Year')
plt.ylabel('Number of Movies')
plt.xticks(rotation=45)
plt.show()

# Display the correlation matrix between ratings and votes
correlation_matrix = df[['Rating', 'Votes']].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=.5)
plt.title('Correlation Matrix: Rating vs Votes')
plt.show()
