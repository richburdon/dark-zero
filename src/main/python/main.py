#
# Copyright 2014 Alien Laboratories, Inc.
#

import flask
from flask_environments import Environments
from flask_injector import FlaskInjector
from injector import inject, Module
import logging
import os

from config import ConfigModule
import util

LOG = logging.getLogger('main')


#
# App config.
#
class AppModule(Module):
    def configure(self, binder):
        pass

#
# View config.
#
import view
@inject(app=util.FlaskWrapper)
class ViewModule(Module):
    def configure(self, binder):
        self.app.add_view(view.HomeView)
        self.app.add_view(view.AdminView)
        self.app.add_view(view.DataView)

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
    AppModule,
    ViewModule,
])

#
# Start-up.
#
if __name__ == '__main__':
    LOG.info('Running...')
    app.run(host='0.0.0.0', port=app.config['PORT'])
