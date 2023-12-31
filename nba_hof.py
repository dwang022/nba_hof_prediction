
import streamlit as st
import pandas as pd
import plotly.express as px

# Sample data
df = pd.read_csv("hof.csv")

# Streamlit App
st.set_page_config(page_title="Basketball Hall of Fame Prediction App", page_icon="🏀", layout="wide")

# Dropdown for Player Selection
selected_player = st.selectbox("Select a player:", df['player'])

# Display Player Information
player_info = df[df['player'] == selected_player]

# Define the order and names of the variables for awards
award_order = ['AllStarCount', 'All-NBA 1st Team', 'All-NBA 2nd Team', 'All-NBA 3rd Team', 'All-Defense 1st Team', 'All-Defense 2nd Team', 'nba roy', 'dpoy', 'nba mvp', 'Championships', 'Finals MVP']
award_names = {
    'nba roy': 'NBA Rookie of the Year',
    'dpoy': 'Defensive Player of the Year',
    'nba mvp': 'NBA Most Valuable Player',
    'All-NBA 1st Team': 'All-NBA 1st Team',
    'All-NBA 2nd Team': 'All-NBA 2nd Team',
    'All-NBA 3rd Team': 'All-NBA 3rd Team',
    'All-Defense 1st Team': 'All-Defense 1st Team',
    'All-Defense 2nd Team': 'All-Defense 2nd Team',
    'Championships': 'Championships',
    'Finals MVP': 'Finals MVP',
    'AllStarCount': 'All-Star Count'
}

player_info_awards = player_info[['player'] + award_order].rename(columns=award_names)



# Customize the order and names of variables for career statistics
career_stats_order = ['ppg', 'apg', 'rpg']
career_stats_names = {
    'ppg': 'Points Per Game',
    'rpg': 'Rebounds Per Game',
    'apg': 'Assists Per Game'
}

# Customize the order and names of variables for career statistics
player_info_career_stats = player_info[['player'] + career_stats_order].rename(columns=career_stats_names)




st.subheader(f"Career Statistics and Accolades for {selected_player}")
column_labels = {'hof': 'In the HOF?', 'first_seas': 'First Season', 'last_seas': 'Last Season', 'ppg': 'Points Per Game', 'apg': 'Assists Per Game', 'rpg': 'Rebounds Per Game', 'AllStarCount': 'All-Star Count', 'nba mvp': 'NBA Most Valuable Player', 'championships': 'Championships', 'dpoy': 'Defensive Player of the Year', 'nba roy': 'NBA Rookie of the Year'}
st.table(player_info.drop(columns=['player_id', 'player', 'hof_probability', 'All-Rookie 1st Team', 'All-Rookie 2nd Team'], errors='ignore')[['hof', 'first_seas', 'last_seas', 'ppg', 'apg', 'rpg', 'AllStarCount', 'All-NBA 1st Team', 'All-NBA 2nd Team', 'All-NBA 3rd Team', 'All-Defense 1st Team', 'All-Defense 2nd Team', 'nba roy', 'dpoy', 'nba mvp', 'Championships', 'Finals MVP']].rename(columns=column_labels))

# Display Hall of Fame Probability
hof_probability = player_info['hof_probability'].values[0]
hof_percentage = min(max(hof_probability * 100, 0), 100)

st.subheader("Hall of Fame Probability:")
st.progress(int(hof_percentage))

# Additional information about Hall of Fame Probability
st.text(f"Hall of Fame Probability: {hof_probability:.2%}")

# Plotly Express Bar Chart for Awards
fig = px.bar(
    player_info_awards.melt(id_vars=['player'], var_name='Award', value_name='Count'),
    x='Award',
    y='Count',
    color='Award',
    title=f"Awards for {selected_player}",
    color_discrete_sequence=['#ffcc00']
)

# Update layout for better aesthetics
fig.update_layout(
    xaxis_title=None,
    yaxis_title="Count",
    legend_title=None
)

# Show the Plotly chart
st.plotly_chart(fig)



# Plotly Express Bar Chart for Career Statistics
fig_career_stats = px.bar(
    player_info_career_stats.melt(id_vars=['player'], var_name='Statistic', value_name='Value'),
    x='Statistic',
    y='Value',
    color='Statistic',
    title=f"Career Statistics for {selected_player}",
    color_discrete_map={'ppg': '#00cc66', 'rpg': '#3366ff', 'apg': '#ff5050'},  # Set colors for each variable
    barmode='group'  # Display bars side by side
)

# Update layout for better aesthetics
fig_career_stats.update_layout(
    xaxis_title=None,
    yaxis_title="Value",
    legend_title=None
)

# Show the Plotly chart for Career Statistics
st.plotly_chart(fig_career_stats)

