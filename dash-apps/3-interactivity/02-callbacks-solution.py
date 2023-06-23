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

app.layout = html.Div(
    children=[
        html.H1(children="My first interactive dash app"),
        dcc.Dropdown(
            id="dropdown",
            options=[
                {"label": class_val, "value": class_val}
                for class_val in set(iris_df["class"])
            ],
            value=0, # Default value
        ),
        dcc.Graph(id="iris-graph"),
    ]
)

@app.callback(
    Output(component_id="iris-graph", component_property="figure"),
    Input(component_id="dropdown", component_property="value"),
)
def make_graph(iris_class):
    df = iris_df[iris_df["class"] == iris_class]
    iris_scatter_figure = px.scatter(x=df["sepal_wid"], y=df["petal_wid"], title="My first interactive Dash plot")
    return iris_scatter_figure


if __name__ == "__main__":
    # remember to run on port 8888 on Faculty platform
    # and set debug=True for hot reloading
    app.run_server(port=8888, debug=True)
