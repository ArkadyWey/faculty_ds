import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State

app = dash.Dash()

app.layout = html.Div(
    [
        dcc.Input(id="input"),
        html.Button("reverse!", id="button"),
        html.Div(id="output"),
    ]
)


@app.callback(
    Output("output", "children"),
    [Input("button", "n_clicks")],
    [State("input", "value")],
)
def reverse_text(n, text):
    if n and isinstance(text, str):
        return text[::-1]
    return text


if __name__ == "__main__":
    app.run_server(debug=True, port=8888)
