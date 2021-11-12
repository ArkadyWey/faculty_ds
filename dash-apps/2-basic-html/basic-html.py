import dash
from dash import html

FACULTY_LOGO = "https://faculty.ai/wp-content/uploads/2019/01/logo-black.svg"

# create an app
app = dash.Dash()

# we recreate the html layout using dash-html-components
# first argument to the component is its children
app.layout = html.Div(
    [
        html.H1("This is a big heading"),
        html.H3("This is a sub-heading"),
        html.P(
            [
                "This is a paragraph with a ",
                html.A("link", href="https://google.com"),
                ".",
            ]
        ),
        html.Ul([html.Li("A list item"), html.Li("Another list item")]),
        html.Img(src=FACULTY_LOGO, alt="Powered by Faculty", width=400),
    ]
)

if __name__ == "__main__":
    # remember to run on port 8888 on Faculty platform
    # and set debug=True for hot reloading
    app.run_server(port=8888, debug=True)
