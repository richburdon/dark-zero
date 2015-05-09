#
# Copyright 2014 Alien Laboratories, Inc.
#

import flask
from flask_environments import Environments
from flask_injector import FlaskInjector
import os

from config import ConfigModule
from view import ViewModule
import service.twitter

#
# Flask App.
#
app = flask.Flask(__name__, template_folder='templates')

# Runtime environment (FLASK_ENV)
# https://pythonhosted.org/Flask-Environments
env = Environments(app)
env.from_yaml(os.path.join(os.getcwd(), 'config/config.yml'))

# Flask injection modules.
# https://github.com/alecthomas/injector
FlaskInjector(app=app, modules=[
    ConfigModule,
    ViewModule,
    service.twitter.ServiceModule
])

#
# Start-up.
#
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=app.config['PORT'])
