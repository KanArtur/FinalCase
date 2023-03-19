import dash
import dash_bootstrap_components as dbc
from config import config

theme = dbc.themes.BOOTSTRAP

application = dash.Dash(external_stylesheets=[theme])