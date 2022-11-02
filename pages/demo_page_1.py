import dash
from dash import dcc, html, Input, Output
import plotly.express as px

dash.register_page(__name__, path='/line-chart-demo')


@dash.callback(
    Output('demo-graph-1', 'figure'),
    Input('checklist', 'value'))
def update_line_chart(continents):
    df = px.data.gapminder()  # replace with your own data source
    mask = df.continent.isin(continents)
    fig = px.line(df[mask], x='year', y='lifeExp', color='country')
    return fig


def layout():
    return html.Div([
        # Chart source code: https://plotly.com/python/line-charts/#line-charts-in-dash
        html.H4('Life expentancy progression of countries per continents', className='chart-title'),
        dcc.Graph(id='demo-graph-1'),
        dcc.Checklist(
            id='checklist',
            options=['Asia', 'Europe', 'Africa', 'Americas', 'Oceania'],
            value=['Americas', 'Oceania'],
            inline=True
        ),
    ],
        style={'margin': '10px'}
    )
