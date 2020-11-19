"""
This script runs the PythonFlaskAPIForBlazorCln application using a development server.
"""

import PythonFlaskAPIForBlazorCln
from PythonFlaskAPIForBlazorCln import configs


from PythonFlaskAPIForBlazorCln.views import employee, department

bp_list = [employee, department]

app = PythonFlaskAPIForBlazorCln.create_app(config_map_list= configs.prod_configs_from_file,
                      blue_print_list=bp_list)

#from os import environ
#from PythonFlaskAPIForBlazorCln import app

#if __name__ == '__main__':
#    HOST = environ.get('SERVER_HOST', 'localhost')
#    try:
#        PORT = int(environ.get('SERVER_PORT', '5555'))
#    except ValueError:
#        PORT = 5555
#    app.run(HOST, PORT)
