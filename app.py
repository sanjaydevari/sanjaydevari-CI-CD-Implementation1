# Import necessary libraries
import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
from flask import Flask
# Create a Dash application
server = Flask(__name__)
app = dash.Dash(__name__, server=server)
# Sample data
data = pd.DataFrame({
'x': [1, 2, 3, 4, 5],
'y': [10, 11, 12, 13, 14]
})
# Define the layout of your app
app.layout = html.Div([
html.H1("My First Dash Application"),
dcc.Graph(
id='scatter-plot',
figure={
'data': [
{'x': data['x'], 'y': data['y'], 'type': 'scatter', 'mode': 'markers'}
],
'layout': {
'title': 'Scatter Plot Example'
}
}
)
])
