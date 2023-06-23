import plotly.express as px
import dash
from dash import html, dcc
from sklearn.datasets import load_iris
import pandas as pd

# Get sample dataset
iris = load_iris()
iris_df = pd.DataFrame(iris.data)
iris_df["class"] = iris.target

iris_df.columns = ["sepal_len", "sepal_wid", "petal_len", "petal_wid", "class"]

app = dash.Dash()

fig = px.scatter(x=iris_df["sepal_wid"], y=iris_df["petal_wid"], title="My first Dash app")

app.layout = html.Div(
    children=[
        html.H1(children="App title"),
        dcc.Dropdown(
            ["New York City", "Montréal", "San Francisco"], "Montréal", multi=True
        ),
        dcc.Graph(id="iris-graph", figure=fig),
    ]
)


if __name__ == "__main__":
    # remember to run on port 8888 on Faculty platform
    # and set debug=True for hot reloading
    app.run_server(port=8888, debug=True)
