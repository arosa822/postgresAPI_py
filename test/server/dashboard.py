#! /usr/bin/env python3
import dash 
import dash_core_components as dcc
import dash_html_components as html
from data_api import getData_4

def pullData():
    
    device_1 = getData_4('device_01')
    device_2 = getData_4('device_02')
    return device_1, device_2 


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Sample Dash'),
    
    # refresh button 
    html.Button('Refresh', id='button'),
    html.Div(id='container-button-basic',children='Loading...'),

])

@app.callback(
        dash.dependencies.Output('container-button-basic','children'),
        [dash.dependencies.Input('button','n_clicks')]
        )
def refreshChart(n_clicks):
    [d1,d2] = pullData()
    
    plot = html.Div(children = ''),dcc.Graph(id = 'Combined data',
            figure={
                'data':[ 
                    {'x': d1['x'], 'y' : d1['y'], 'type': 'line', 'name' : 'd_1'},
                    {'x': d2['x'], 'y' : d2['y'], 'type': 'line', 'name' : 'd_2'},
                ],
                    'layout': {'title':'this is a test'}
            }
        )
    return plot

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port = 8084)
