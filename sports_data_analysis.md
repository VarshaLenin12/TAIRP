# Importing necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Mounting Google Drive to access the dataset
from google.colab import drive
drive.mount('/content/drive')

# Reading the FIFA dataset
df = pd.read_csv('/content/drive/MyDrive/fifa_eda_stats.csv')

# Displaying basic information about the dataset
df.head()
print(df.columns)
df.info()
df.describe()
df.isnull().sum()

# Handling missing values by filling with mode for columns with 48 missing values
for column in df.columns:
    if df[column].isnull().sum() == 48:
        mode_value = df[column].mode()[0]
        df[column].fillna(mode_value, inplace=True)

# Displaying the updated dataset after handling missing values
df.isnull().sum()

# Histogram of player ages
plt.figure(figsize=(10, 6))
plt.hist(df['Age'], bins=20, color='skyblue', edgecolor='black')
plt.title('Distribution of Player Ages')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()

# Swarmplot and Bar Chart for Top Countries based on Overall Rating
plt.figure(figsize=(12, 8))
sns.swarmplot(x='Overall', y='Nationality', data=df_sorted.head(top_countries), palette='viridis')
fig = px.bar(df_sorted.head(top_countries), x='Overall', y='Nationality', orientation='h')
fig.show()

# Distribution of Overall and Potential Ratings
plt.figure(figsize=(12, 6))
sns.histplot(df[['Overall', 'Potential']], bins=20, kde=True)
plt.title('Distribution of Overall and Potential Ratings')
plt.xlabel('Rating')
plt.ylabel('Count')
plt.legend(['Overall', 'Potential'])
plt.show()

# Distribution of specific skills like Crossing, Finishing, Dribbling
skills = ['Crossing', 'Finishing', 'Dribbling']
plt.figure(figsize=(14, 8))
for skill in skills:
    sns.histplot(df[skill], bins=20, kde=True, label=skill)
plt.title('Distribution of Specific Skills')
plt.xlabel('Skill Level')
plt.ylabel('Count')
plt.legend()
plt.show()

# Pie chart for Distribution of Players' Preferred Foot
preferred_foot_counts = df['Preferred Foot'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(preferred_foot_counts, labels=preferred_foot_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Distribution of Players\' Preferred Foot')
plt.show()

# Pie chart for Distribution of Players' Work Rate
work_rate_counts = df['Work Rate'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(work_rate_counts, labels=work_rate_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Distribution of Players\' Work Rate')
plt.show()

# Line plot for Player Ratings Over Age
plt.figure(figsize=(14, 8))
sns.lineplot(x='Age', y='Overall', data=df, label='Overall Rating')
sns.lineplot(x='Age', y='Potential', data=df, label='Potential Rating')
plt.title('Player Ratings Over Age')
plt.xlabel('Age')
plt.ylabel('Rating')
plt.legend()
plt.show()

# Count plot for Count of Players in Different Positions
plt.figure(figsize=(12, 6))
sns.countplot(x='Position', data=df)
plt.title('Count of Players in Different Positions')
plt.xlabel('Position')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

# Count plot for Count of Players from Different Nationalities
plt.figure(figsize=(14, 8))
sns.countplot(y='Nationality', data=df, order=df['Nationality'].value_counts().index[:15])
plt.title('Top 15 Nationalities of Players')
plt.xlabel('Count')
plt.ylabel('Nationality')
plt.show()

# Count plot for Count of Players in Different Clubs
plt.figure(figsize=(14, 8))
sns.countplot(y='Club', data=df, order=df['Club'].value_counts().index[:15])
plt.title('Top 15 Clubs with Most Players')
plt.xlabel('Count')
plt.ylabel('Club')
plt.show()

# Correlation Heatmap for a subset of columns
subset_columns = ['Overall', 'Potential', 'Value', 'Wage', 'Age', 'Crossing', 'Finishing', 'Dribbling']
correlation_matrix_subset = df[subset_columns].corr()

# Plotting the subset correlation heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix_subset, annot=True, cmap='coolwarm', linewidths=.5)
plt.title('Subset Correlation Heatmap')
plt.show()
