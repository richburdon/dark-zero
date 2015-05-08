#
# Copyright 2014 Alien Laboratories, Inc.
#

import flask
from flask_injector import FlaskInjector
from injector import inject, Module
import logging
import util

import config

LOG = logging.getLogger('main')


class Foo(object):
    pass


@inject(foo=Foo)
class Bar(object):
    pass


#
# App config
#
class AppModule(Module):
    def configure(self, binder):
        binder.bind(Foo, Foo())

#
# View config
#
import view
@inject(app=util.FlaskWrapper, bar=Bar)
class ViewModule(Module):
    def configure(self, binder):
        self.app.add_view(view.HomeView, 'Home')
        self.app.add_view(view.DataView, 'Data')

#
# Flask App
#
app = flask.Flask(__name__, template_folder='templates')
app.config.from_pyfile('config/flask_debug.py')

# Flask injection modules.
# https://github.com/alecthomas/injector
FlaskInjector(app=app, modules=[
    config.DevConfigModule,
    AppModule,
    ViewModule,
])

#
# Start-up.
#
if __name__ == '__main__':
    LOG.info('Running...')
    app.run(host='0.0.0.0', port=8080)  # TODO(burdon): Port from config.
