#!/usr/bin/env python
#
# Copyright 2014 Alien Laboratories, Inc.
#

# Initial set-up (must happen first).
import os
import config
config.init_paths(os.path.dirname(__file__))

# Initial set-up.
import logging
LOG = logging.getLogger('main')

# Main App.
import flask
app = flask.Flask(__name__, template_folder='templates')
app.debug = True

from injector import inject, Module
import util


class AppModule(Module):
    def configure(self, binder):
        pass

@inject(app=util.FlaskWrapper)
class ViewModule(Module):
    def configure(self, binder):
        import view
        self.app.add_view(view.HomeView, 'Home')


# Flask injector modules.
from flask_injector import FlaskInjector
FlaskInjector(app=app, modules=[
    AppModule,
    ViewModule,
])


# Note: We don't need to call app.run() since we are embedded within the App Engine WSGI application server.
LOG.info('Running...')
