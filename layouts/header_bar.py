import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
from assets import dropdown_values
from dash_bootstrap_templates import ThemeChangerAIO

size_dict = {"xs": 10, "sm": 10, "md": 10, "lg": 3}
size_dict_1 = {"xs": 10, "sm": 10, "md": 10, "lg": 9}

def build_header_bar(app):
    return dbc.Navbar(className="banner", sticky="top", children=[
        build_banner(app),
        build_intervals_div()
    ])
    
    
def build_banner(app):
    
    return dbc.Container(children=[
        dbc.Row([
            dbc.Col(html.Img(src=app.get_asset_url("logo.png")), width=3), 
            dbc.Col(width="auto", children=[
                html.H1("SRI SATHYA SAI SEVA ORGANIZATION", ),
                html.H4("Madhya Pradesh", className="logo")
            ]),
        ]),
        dbc.Row(id="header_tabs_1", children=
            dbc.Col(children=[
                build_tabs()
                # dbc.NavbarToggler(id="navbar-toggler11", className="pull-right"),
                # dbc.Collapse(dbc.Nav(build_tabs(), navbar=True), id="navbar-collapse11", navbar=True),
            ]),
        ),
        dbc.Row([
        
            dbc.Col(html.Img(src=app.get_asset_url("logo.png")), width=1), 
            dbc.Col(width="auto", children=[
                html.H6("SRI SATHYA SAI SEVA", className="logo"),
                html.H6("ORGANIZATION, MP", className="logo")
            ]),
            # dbc.Col(html.I(className="fa fa-home"),),
            dbc.Col(width="auto", class_name="center", children=[
                dbc.NavbarToggler(id="navbar-toggler11", className="pull-right"),
                dbc.Collapse(dbc.Nav(build_tabs_2(), navbar=True), id="navbar-collapse11", navbar=True),
            ]),

        ]),
        
        # ],**size_dict),
        # ThemeChangerAIO(aio_id="theme", 
        #                 button_props={"color": "primary", "style": {"height": "auto", "width": "5vw"}},
        #                 radio_props={"value": dbc.themes.CERULEAN})
    ])


def build_tabs():
    # The keys of this dictionary should be same as module defined in 
    # layouts/__init__.py while registering pages 

    header_tabs = ["Sri Sathya Sai Baba", "Organisation", "Wings", 
                   "Activities", "Gallery", "Services", "Contact Us"]
    
    # fa-duotone fa-square-chevron-down
    tabs = [dbc.Col(html.H6([i, " ", html.I(className="fa fa-chevron-down fa-2xs fa-beat")]), id=i, class_name="tab_name", width="auto") 
            for i in header_tabs]

    return html.Div(children=[
        dbc.Row(tabs),
        *get_popover_data()
    ])

def build_tabs_2():
    # The keys of this dictionary should be same as module defined in 
    # layouts/__init__.py while registering pages 

    header_tabs = ["Sri Sathya Sai Baba", "Organisation", "Wings", 
                   "Activities", "Gallery", "Services", "Contact Us"]
    
    # fa-duotone fa-square-chevron-down
    tabs = [dbc.Col(html.H6([i, " ", html.I(className="fa fa-chevron-down fa-2xs fa-beat")]), id=i+'2', class_name="tab_name", width="auto") 
            for i in header_tabs]

    return html.Div(children=[
        dbc.Row(tabs),
        *get_popover_data()
    ])



def get_popover_data():
    popover_data = []

    for name in ["Sri Sathya Sai Baba", "Wings", "Activities", "Services"]:

        start = "sss" if name == "Sri Sathya Sai Baba" else name.lower()
        popover_content = dbc.PopoverBody([
            # dbc.DropdownMenuItem(divider=True),
            *[_get_nav_link(i) for i in dash.page_registry.keys() if i.startswith(start)]
        ])
        popover = dbc.Popover(popover_content, offset=0, hide_arrow=True,
                              target=name, trigger="hover", placement="bottom-start"
                             )
        popover_data.append(popover)

    return popover_data

def _get_nav_link(page):
    data = dash.page_registry[page]
    return dbc.NavLink(data['name'], href=data["relative_path"])

    
def build_intervals_div():
    return html.Div(id='interval_div', children=[
        dcc.Interval(id="i1", interval=1 * 1000, n_intervals=0),
        dcc.Interval(id="i2", interval=2 * 1000, n_intervals=0),
        dcc.Interval(id="i5", interval=5 * 1000, n_intervals=0),
        dcc.Interval(id="i60", interval=60 * 1000, n_intervals=0),
    ])



    # logo_dict = {
    #     "tab1": html.I(className="fa fa-home"),
    #     "tab2": html.I(className="fa fa-regular fa-sun"),
    #     "tab3": html.I(className="fa fa-thin fa-book"),
    #     "tab4": html.I(className="fa fa-brands fa-windows"),
    #     "tab5": html.I(className="fa fa-home"),
    #     "tab6": html.I(className="fa fa-thin fa-face-smile"),
    #     "tab7": html.I(className="fa fa-thin fa-computer"),
    #     "tab8": html.I(className="fa fa-thin fa-cloud-arrow-down"),
    # }

