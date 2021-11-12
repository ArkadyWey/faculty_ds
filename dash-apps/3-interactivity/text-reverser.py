import dash
from dash import dcc, html
from dash.dependencies import Input, Output

app = dash.Dash()

app.layout = html.Div([dcc.Input(id="input"), html.Div(id="output")])


@app.callback(Output("output", "children"), [Input("input", "value")])
def reverse_text(text):
    return text[::-1]


if __name__ == "__main__":
    app.run_server(debug=True, port=8888)
