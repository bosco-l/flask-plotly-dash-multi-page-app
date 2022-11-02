import dash
from dash import html

dash.register_page(__name__, path='/')

layout = html.Div('Home Page of Dash App')

# Alternative layout
# def layout():
#     return html.Div('Home Page of Dash App')

