import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output
from sklearn import datasets
from sklearn.cluster import KMeans

# we load the data we need into global scope
iris_raw = datasets.load_iris()
iris = pd.DataFrame(iris_raw["data"], columns=iris_raw["feature_names"])

app = dash.Dash()

# layouts can get large and unwieldy, break it down into groups of components
controls = html.Div(
    [
        dcc.Dropdown(
            id="x-variable",
            options=[{"label": col, "value": col} for col in iris.columns],
            value="sepal length (cm)",
        ),
        dcc.Dropdown(
            id="y-variable",
            options=[{"label": col, "value": col} for col in iris.columns],
            value="sepal width (cm)",
        ),
        dcc.Input(id="cluster-count", type="number", value=3),
    ]
)
app.layout = html.Div(
    [html.H1("K-means clustering"), controls, dcc.Graph(id="cluster-graph")]
)


# this callback slices the data according to the two dropdown,
# runs kmeans clustering on it, and plots the results
@app.callback(
    Output("cluster-graph", "figure"),
    [
        Input("x-variable", "value"),
        Input("y-variable", "value"),
        Input("cluster-count", "value"),
    ],
)
def make_graph(x, y, n_clusters):
    # minimal input validation, make sure there's at least one cluster
    km = KMeans(n_clusters=max(n_clusters, 1))
    df = iris.loc[:, [x, y]]
    km.fit(df.values)
    df["cluster"] = km.labels_

    centers = km.cluster_centers_

    data = [
        go.Scatter(
            x=df.loc[df.cluster == c, x],
            y=df.loc[df.cluster == c, y],
            mode="markers",
            marker={"size": 8},
            name="Cluster {}".format(c),
        )
        for c in range(n_clusters)
    ]

    data.append(
        go.Scatter(
            x=centers[:, 0],
            y=centers[:, 1],
            mode="markers",
            marker={"color": "#000", "size": 12, "symbol": "diamond"},
            name="Cluster centers",
        )
    )

    layout = {"xaxis": {"title": x}, "yaxis": {"title": y}}

    return go.Figure(data=data, layout=layout)


if __name__ == "__main__":
    app.run_server(debug=True, port=8888)
