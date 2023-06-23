import plotly.graph_objects as go
import dash
from dash import html, dcc
from sklearn.datasets import load_iris
import pandas as pd

# Get sample dataset

app = dash.Dash()

# Make a plot and store is as figure


app.layout = html.Div(
    children=[html.H1(children="Title"),
    dcc.Graph(id="iris-graph", figure=fig)]
)

if __name__ == "__main__":
    # remember to run on port 8888 on Faculty platform
    # and set debug=True for hot reloading
    app.run_server(port=8888, debug=True)
