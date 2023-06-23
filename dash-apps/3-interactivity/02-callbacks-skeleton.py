import plotly.express as px
import dash
from dash import Dash, dcc, html, Input, Output
from sklearn.datasets import load_iris
import pandas as pd

# Get sample dataset
iris = load_iris()
iris_df = pd.DataFrame(iris.data)
iris_df["class"] = iris.target

iris_df.columns = ["sepal_len", "sepal_wid", "petal_len", "petal_wid", "class"]

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Title'),
    dcc.Dropdown() 
    # Change the dropdown to take the available options in set as an input
    # ideally make it dynamic to the values in the df but you can hardcode it
    # Link to the callback

    dcc.Graph()
    # Link to the callback
])


# Convert the graph code below to work as a function taking iris class as an input
# 1. subset the dataframe using class
# 2. Modify it with the app.callback decorator
iris_scatter_figure = px.scatter(x=df["sepal_wid"], y=df["petal_wid"], title="My first interactive Dash plot")


if __name__ == "__main__":
    # remember to run on port 8888 on Faculty platform
    # and set debug=True for hot reloading
    app.run_server(port=8888, debug=True)