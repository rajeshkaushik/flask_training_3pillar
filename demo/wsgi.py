import os

from my_app import create_app


config_name = os.getenv('APP_SETTINGS', 'development')
app = create_app(config_name)
