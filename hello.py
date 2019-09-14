import dash
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div(id="first",n_clicks=0,children=
    [html.H1(id="second",children=["hello world"])]
    )

@app.callback(dash.dependencies.Output("second", "style"),
        [dash.dependencies.Input("first", "n_clicks")])

def change_font(n_clicks):
    if n_clicks % 2 ==1:
        return {"fontSize":80}

app.run_server(debug=True)
