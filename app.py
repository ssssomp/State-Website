import dash
import dash_bootstrap_components as dbc

from layouts import Layout, register_app_pages
from callbacks import Callbacks
from apis import AppAPIs
from sql import MongoConnector


client = MongoConnector().connect()
app = dash.Dash(__name__, 
           update_title=None,
           title='Analysis', 
           external_stylesheets=[dbc.themes.BOOTSTRAP, 
                                 'https://use.fontawesome.com/releases/v6.2.1/css/all.css'], 
           pages_folder="layouts",
           use_pages=True)

app.config["suppress_callback_exceptions"] = True
server = app.server 

AppAPIs(server)

# Enable Whitenoise for serving static files from Heroku (the /static folder is seen as root by Heroku) 
# server.wsgi_app = WhiteNoise(server.wsgi_app, root='static/') 

register_app_pages()
app.layout = Layout(app)
Callbacks(app, client)

if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0", port=8050)