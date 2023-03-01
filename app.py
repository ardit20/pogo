import pandas as pd
import streamlit as st

# Load data
df = pd.DataFrame({
    'Pokemon': ['Medicham (XL)', 'Deoxys (Defense)', 'Azumarill (XL)', 'Stunfisk (Galarian)'],
    'Score': [95.8, 93.6, 93.5, 92.8],
    'Type 1': ['fighting', 'psychic', 'water', 'ground']
})

# Sidebar options
types = sorted(df['Type 1'].unique())
min_score, max_score = df['Score'].min(), df['Score'].max()

# Sidebar filters
st.sidebar.header('Filters')
selected_type = st.sidebar.selectbox('Pokemon Type', ['All'] + types)
score_range = st.sidebar.slider('Pokemon Score Range', min_score, max_score, (min_score, max_score))

# Apply filters
filtered_df = df[(df['Type 1'] == selected_type) | (selected_type == 'All')]
filtered_df = filtered_df[(filtered_df['Score'] >= score_range[0]) & (filtered_df['Score'] <= score_range[1])]

# Display table
st.table(filtered_df)
