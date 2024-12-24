import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import sqlite3

# Load data from SQLite
conn = sqlite3.connect('C:/Users/Mark Rozenberg/Foobal-Climate/Data/Main_DB.db')
df = pd.read_sql_query("SELECT * FROM goal_scorers_summary", conn)
conn.close()

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    html.H1("Top Scorers by Tournament"),
    dcc.Dropdown(
        id='tournament-dropdown',
        options=[{'label': i, 'value': i} for i in df['tournament'].unique()],
        value=df['tournament'].unique()[0]
    ),
    dcc.Graph(id='score-graph')
])

# Define callback to update graph
@app.callback(
    Output('score-graph', 'figure'),
    [Input('tournament-dropdown', 'value')]
)
def update_graph(selected_tournament):
    filtered_df = df[df['tournament'] == selected_tournament]
    fig = {
        'data': [
            {'x': filtered_df['player_id'], 'y': filtered_df['goals'], 'type': 'bar', 'name': selected_tournament}
        ],
        'layout': {
            'title': f'Top Scorers in {selected_tournament}'
        }
    }
    return fig
    
# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)