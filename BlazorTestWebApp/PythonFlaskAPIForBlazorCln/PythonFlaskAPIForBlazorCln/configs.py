import os
import konfig

_HERE = os.path.dirname(__file__)
_SETTINGS_FILE = os.path.join(_HERE, 'settings.ini')
CONFS = konfig.Config(_SETTINGS_FILE)
db_settings_map = CONFS.get_map('db')

prod_configs_from_file = [db_settings_map,]