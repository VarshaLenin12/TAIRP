# Install Dash library
pip install dash

# Import necessary libraries
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Mount Google Drive for dataset access (for Colab)
from google.colab import drive
drive.mount('/content/drive')

# Load the COVID-19 dataset
df = pd.read_csv('/content/drive/MyDrive/owid-covid-data.csv')

# Display basic information about the dataset
df.head()
df.info()

# Display the count of missing values for each column
print(df.isnull().sum())

# Display descriptive statistics of the dataset
print(df.describe())

# Display the column names in the dataset
print(df.columns)

# Drop unnecessary columns
columns_to_drop = ['excess_mortality_cumulative_absolute', 'excess_mortality_cumulative_absolute', 'excess_mortality', 'excess_mortality_cumulative_per_million']
df = df.drop(columns=columns_to_drop, axis=1)

# Convert the 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'])

# Plot a histogram to visualize the distribution of fully vaccinated people per hundred
plt.figure(figsize=(10, 6))
sns.histplot(df['people_fully_vaccinated_per_hundred'], bins=30, kde=True)
plt.title('Distribution of People Fully Vaccinated per Hundred')
plt.show()

# Display the correlation matrix between ICU patients and hospital patients
correlation_matrix = df[['icu_patients', 'hosp_patients']].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=.5)
plt.title('Correlation Heatmap: ICU Patients vs Hospital Patients')
plt.show()

# Visualize daily cases, deaths, and vaccinations over time
plt.figure(figsize=(14, 7))
sns.lineplot(x='date', y='new_cases', data=df, label='Daily Cases')
sns.lineplot(x='date', y='new_deaths', data=df, label='Daily Deaths')
sns.lineplot(x='date', y='new_vaccinations', data=df, label='Daily Vaccinations')
plt.title('Daily Cases, Deaths, and Vaccinations Over Time')
plt.xlabel('Date')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

# Compare total cases and deaths across countries or regions
plt.figure(figsize=(12, 6))
top_countries = df.groupby('location')['total_cases'].max().sort_values(ascending=False).head(10)
top_countries.plot(kind='bar', color='skyblue')
plt.title('Top 10 Countries by Total Cases')
plt.xlabel('Country')
plt.ylabel('Total Cases')
plt.show()

# Compare vaccination rates and infection rates using a scatter plot
plt.figure(figsize=(12, 6))
sns.scatterplot(x='total_vaccinations_per_hundred', y='total_cases_per_million', data=df)
plt.title('Vaccination Rate vs. Infection Rate')
plt.xlabel('Total Vaccinations per Hundred People')
plt.ylabel('Total Cases per Million People')
plt.show()

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the dashboard
app.layout = html.Div([
    html.H1("COVID-19 Data Analysis Dashboard"),

    html.Label("Select Country:"),
    dcc.Dropdown(
        id='country-dropdown',
        options=[{'label': country, 'value': country} for country in df['location'].unique()],
        value='United States'),
    dcc.Graph(id='cases-deaths-plot')])

# Define callback to update the graph based on user input
@app.callback(
    Output('cases-deaths-plot', 'figure'),
    [Input('country-dropdown', 'value')])
def update_graph(selected_country):

    # Filter data for the selected country
    country_data = df[df['location'] == selected_country]

    # Create a plot
    fig = {'data': [{'x': country_data['date'], 'y': country_data['total_cases'], 'type': 'line', 'name': 'Total Cases'},
                    {'x': country_data['date'], 'y': country_data['total_deaths'], 'type': 'line', 'name': 'Total Deaths'}],
           'layout': {'title': f'Total Cases and Deaths in {selected_country}',
                      'xaxis': {'title': 'Date'},
                      'yaxis': {'title': 'Count'}}}
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
