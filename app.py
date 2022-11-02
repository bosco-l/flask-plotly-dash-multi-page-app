import dash
from dash import Dash, html
import flask
import dash_bootstrap_components as dbc

DASH_APP_URL = '/dashapp'

# Web app
app_flask = flask.Flask(__name__)  # Flask
app_dash = Dash(__name__,
                use_pages=True,
                external_stylesheets=[dbc.themes.BOOTSTRAP],  # 1st: add external stylesheet
                url_base_pathname=f'{DASH_APP_URL}/',
                server=app_flask,
                )


# Flask app
@app_flask.route(rule='/')
def home_page():
    return 'This is the home page served with Flask'


@app_flask.route(rule=f'{DASH_APP_URL}/')
def my_dash_app():
    return app_dash.index()


# Dash app
app_dash.layout = html.Div(children=[
    html.H2(children='Multi-page Dash App Demo', style={'text-align': 'center'}),
    dbc.Nav([dbc.NavItem(dbc.NavLink('Home', id='style-demo', href=f'{DASH_APP_URL}/')),
             # 2nd: assign id for styling with style.css
             dbc.NavItem(dbc.NavLink('Line Chart', href=f'{DASH_APP_URL}/line-chart-demo')),
             dbc.NavItem(dbc.NavLink('3D Scatter Plot', href=f'{DASH_APP_URL}/scatter-plot-demo')),
             ]),
    html.Hr(),
    dash.page_container
],
    # 3rd: style argument in dash components
    style={'margin': '20px'}
)

if __name__ == '__main__':
    port = 5000
    print(f'Flask: http://localhost:{port}/')
    print(f'Dash: http://localhost:{port}{DASH_APP_URL}')

    # Run Flask
    app_flask.run(debug=False, port=port, host='0.0.0.0')
    # app_dash.run_server(debug=False)
