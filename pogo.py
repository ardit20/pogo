import pandas as pd
import streamlit as st
import plotly.express as px

# Load the dataset
df = pd.read_csv('pogo.csv')

# Add a default selection for the type filter
selected_type = st.sidebar.radio('Select a Pokemon type', ['All'] + df['Type 1'].unique().tolist())

# Filter the DataFrame based on the selected type
if selected_type != 'All':
    df_filtered = df[(df['Type 1'] == selected_type) | (df['Type 2'] == selected_type)]
else:
    df_filtered = df

# Display the filtered DataFrame
st.write(f"Showing {len(df_filtered)} Pokemons with type {selected_type}:")
st.table(df_filtered)

# Create a scatterplot of Pokemon scores
fig = px.scatter(df_filtered, x='Type 1', y='Score', color='Type 2', hover_name='Pokemon', 
                 title='Pokemon Scores by Type', width=800, height=500)
st.plotly_chart(fig)
