import dash
from dash import html

# create an app
app = dash.Dash()

# define the layout
app.layout = html.Div("Hello, World!")

if __name__ == "__main__":
    # start the app server
    # use port 8888 on Faculty Platform
    # set debug = True for hot reloading
    app.run_server(debug=True, port=8888)
