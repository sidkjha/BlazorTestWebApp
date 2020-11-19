"""
The flask application package.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from PythonFlaskAPIForBlazorCln import configs
#from flask_migrate import Migrate

app = Flask(__name__)
if configs.prod_configs_from_file:
    for m in configs.prod_configs_from_file:
        app.config.update(m)
db = SQLAlchemy(app)
#migrate = Migrate()

import PythonFlaskAPIForBlazorCln.views

def create_app(config_map_list=None, blue_print_list=None):
    #app = Flask(__name__)
    #if config_map_list:
    #    for m in config_map_list:
    #        app.config.update(m)
        
    #db.init_app(app)
    #migrate.init_app(app, db)
    #db.create_all()
    
    if blue_print_list:
        for bp in blue_print_list:
            app.register_blueprint(bp)
    
    return app
