import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html
from services import config, application as app, values

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background": "#f8f9fa",
}

CONTENT_STYLE = {
    "marginLeft": "18rem",
    "marginRight": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.P("Космические фермеры", className="lead"),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink("Главная страница",
                            href="/", active="exact"),
            ],
            vertical=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)


def resources_remains():
    return html.Table(
        [html.Tr(html.Th('Ресурс', 'Остаток'))]
    )


distance_input = html.Div([dbc.input(id="input", placeholder="Введите дистанцию от предыдущей точки", type="int"),
                           html.Br(), html.P(id="output")])

SH_input = html.Div([dbc.input(id="input", placeholder="Введите кол-во Spatium herba", type="int"),
                     html.Br(), html.P(id="output")])

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])
