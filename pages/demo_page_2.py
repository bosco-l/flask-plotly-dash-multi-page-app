import dash
from dash import dcc, html, Input, Output
import plotly.express as px

dash.register_page(__name__, path='/scatter-plot-demo')


@dash.callback(
    Output('demo-graph-2', 'figure'),
    Input('range-slider', 'value'))
def update_bar_chart(slider_range):
    df = px.data.iris()  # replace with your own data source
    low, high = slider_range
    mask = (df.petal_width > low) & (df.petal_width < high)

    fig = px.scatter_3d(df[mask],
                        x='sepal_length', y='sepal_width', z='petal_width',
                        color='species', hover_data=['petal_width'])
    return fig


def layout():
    return html.Div([
        # Chart source code: https://plotly.com/python/3d-scatter-plots/#3d-scatter-plots-in-dash
        html.H4('Iris samples filtered by petal width', className='chart-title'),
        dcc.Graph(id='demo-graph-2'),
        html.P('Petal Width:'),
        dcc.RangeSlider(
            id='range-slider',
            min=0, max=2.5, step=0.1,
            marks={0: '0', 2.5: '2.5'},
            value=[0.5, 2]
        ),
    ],
        style={'margin': '10px'}
    )
