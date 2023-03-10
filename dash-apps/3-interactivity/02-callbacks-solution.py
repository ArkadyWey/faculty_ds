import plotly.graph_objects as go
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
        html.H1(children="Title"),
        dcc.Dropdown(
            id="dropdown",
            options=[
                {"label": class_val, "value": class_val}
                for class_val in set(iris_df["class"])
            ],
            value="Iris Class",
        ),
        dcc.Graph(id="iris-graph"),
    ]
)


@app.callback(
    Output(component_id="iris-graph", component_property="figure"),
    Input(component_id="dropdown", component_property="value"),
)
def make_graph(iris_class: str):
    df = iris_df[iris_df["class"] == iris_class]

    data = [go.Scatter(x=df["sepal_wid"], y=df["petal_wid"], mode="markers")]
    layout = go.Layout(title=go.layout.Title(text="My first plotly graph"))
    iris_scatter_figure = go.Figure(data=data, layout=layout)
    return iris_scatter_figure


if __name__ == "__main__":
    # remember to run on port 8888 on Faculty platform
    # and set debug=True for hot reloading
    app.run_server(port=8888, debug=True)
