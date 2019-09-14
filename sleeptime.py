import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Input, Output
import plotly.graph_objs as go

df = pd.read_csv('https://raw.githubusercontent.com/greenteabiscuit/pycon_sprint/master/sleep_prefectures.csv')

data = []
row_count = len(df.index)
cols = [col for col in df.columns]
for i in range(48):
    vals = [df.iloc[i][col] for col in df.columns]
    x = cols[2:]
    prefecture = vals[0]
    y = vals[2:]
    data.append({
        'x': x,
        'y': y,
        'type': 'bar',
        'name': prefecture
    })

options = [{'label': d['name'], 'value': d['name']} for d in data]


def generate_table(dataframe, max_rows=10):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H4(children='都道府県睡眠データ'),

    html.Label('Shown Prefectures:'),
    dcc.Dropdown(
        id='select-prefectures',
        options=options,
        value=['全国', '北海道', '青森県'],
        multi=True
    ),

    dcc.Graph(
        id='prefrectue-sleeptime-graph'
        # figure={
        #     'data': data,
        #     'layout': {
        #         'font': {
        #             'color': '#FFFFFF'
        #         }
        #     }
        # }
    ),

    # generate_table(df)

])


@app.callback(
    Output('prefrectue-sleeptime-graph', 'figure'),
    [Input('select-prefectures', 'value')])
def update_figure(selected_prefectures):
    _data = [d for d in data if d['name'] in selected_prefectures]

    return {
        'data': _data,
        'layout': go.Layout(
            xaxis={'title': 'Year'},
            yaxis={'title': 'Minutes'},
        )
    }


if __name__ == '__main__':
    app.run_server(debug=True)
