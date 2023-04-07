from dash import html, dcc, dash_table, Input, State, Output
import plotly.graph_objs as go
from nsetools import Nse
import pandas as pd
import random

from helper_functions import *
from sql import TOP_MOVERS

nse = Nse()

# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')


def callbacks_tab1(app, client):

    @app.callback(Output('top_gainers_div', 'children'),
                  Input('i60', 'n_intervals'))
    def top_gainers(n):
        df = pd.DataFrame()
        df = TOP_MOVERS(client).get_top_gainers()
        data = df.to_dict(orient='records')
        table = dash_table.DataTable(columns=[{"name": i, "id": i} for i in df.columns], 
                                     data=data, 
                                    #  style_header={'backgroundColor': '#45df7e'},
                                     style_cell={'text-align':'center', 
                                                 'backgroundColor': plot_bg_color2, 
                                                 'color': text_color}, 
                                     style_data_conditional=[
                                         {"if": {"column_id": "Change"}, "color": green_color}, 
                                         {"if": {"column_id": "% Change"}, "color": green_color}
                                     ]
                )
        
        return [table]



def func1():
    ''''''
    
    
   