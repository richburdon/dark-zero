#!/usr/bin/env python
#
# Copyright 2014 Alien Laboratories, Inc.
#

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
        self.app.add_view(view.DataView, 'Data')


# Flask injector modules.
from flask_injector import FlaskInjector
FlaskInjector(app=app, modules=[
    AppModule,
    ViewModule,
])

# Start-up.
if __name__ == '__main__':
    LOG.info('Running...')
    app.run(host='0.0.0.0', port=80)
