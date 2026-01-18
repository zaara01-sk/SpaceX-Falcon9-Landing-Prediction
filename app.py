"""
SpaceX Falcon 9 Launch Dashboard
Author: [Your Name]
Date: January 2026
Description: A production-ready Dash application visualizing SpaceX launch success
             rates and payload correlations.
"""

import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc, Input, Output

# =============================================================================
# 1. DATA LOADING & PREPARATION
# =============================================================================

def load_data():
    """Load and preprocess the SpaceX launch dataset."""
    url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_dash.csv"
    df = pd.read_csv(url)
    # Ensure any necessary cleaning is done here
    return df

spacex_df = load_data()
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# =============================================================================
# 2. APP INITIALIZATION
# =============================================================================

app = Dash(__name__)
server = app.server  # Essential for deployment (e.g., on Gunicorn/Heroku)

# =============================================================================
# 3. UI LAYOUT
# =============================================================================

app.layout = html.Div(children=[
    html.H1('SpaceX Launch Records Dashboard',
            style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),

    # TASK 1: Dropdown for Launch Site Selection
    dcc.Dropdown(
        id='site-dropdown',
        options=[
            {'label': 'All Sites', 'value': 'ALL'},
            {'label': 'CCAFS LC-40', 'value': 'CCAFS LC-40'},
            {'label': 'VAFB SLC-4E', 'value': 'VAFB SLC-4E'},
            {'label': 'KSC LC-39A', 'value': 'KSC LC-39A'},
            {'label': 'CCAFS SLC-40', 'value': 'CCAFS SLC-40'}
        ],
        value='ALL',
        placeholder="Select a Launch Site here",
        searchable=True
    ),
    html.Br(),

    # TASK 2: Success Pie Chart
    html.Div(dcc.Graph(id='success-pie-chart')),
    html.Br(),

    html.P("Payload range (Kg):"),
    # TASK 3: Payload Range Slider
    dcc.RangeSlider(
        id='payload-slider',
        min=0, max=10000, step=1000,
        marks={0: '0', 100: '100'},
        value=[min_payload, max_payload]
    ),

    # TASK 4: Payload vs. Success Scatter Chart
    html.Div(dcc.Graph(id='success-payload-scatter-chart')),
])

# =============================================================================
# 4. CALLBACKS
# =============================================================================

@app.callback(
    Output(component_id='success-pie-chart', component_property='figure'),
    Input(component_id='site-dropdown', component_property='value')
)
def get_pie_chart(entered_site):
    """Update success pie chart based on selected site."""
    filtered_df = spacex_df
    if entered_site == 'ALL':
        fig = px.pie(filtered_df, values='class', 
                     names='Launch Site', 
                     title='Total Success Launches By Site')
        return fig
    else:
        filtered_df = spacex_df[spacex_df['Launch Site'] == entered_site]
        # Count successes (1) and failures (0)
        success_counts = filtered_df['class'].value_counts().reset_index()
        fig = px.pie(success_counts, values='count', 
                     names='class', 
                     title=f'Total Success Launches for site {entered_site}')
        return fig

@app.callback(
    Output(component_id='success-payload-scatter-chart', component_property='figure'),
    [Input(component_id='site-dropdown', component_property='value'),
     Input(component_id='payload-slider', component_property='value')]
)
def get_scatter_chart(entered_site, payload_range):
    """Update scatter chart based on site and payload range."""
    low, high = payload_range
    mask = (spacex_df['Payload Mass (kg)'] >= low) & (spacex_df['Payload Mass (kg)'] <= high)
    filtered_df = spacex_df[mask]

    if entered_site == 'ALL':
        fig = px.scatter(filtered_df, x='Payload Mass (kg)', y='class',
                         color='Booster Version Category',
                         title='Correlation between Payload and Success for all Sites')
        return fig
    else:
        filtered_df = filtered_df[filtered_df['Launch Site'] == entered_site]
        fig = px.scatter(filtered_df, x='Payload Mass (kg)', y='class',
                         color='Booster Version Category',
                         title=f'Correlation between Payload and Success for {entered_site}')
        return fig

# =============================================================================
# 5. MAIN EXECUTION
# =============================================================================

if __name__ == '__main__':
    # Using 'debug=False' for a more stable terminal environment
    app.run(debug=True, port=8050)