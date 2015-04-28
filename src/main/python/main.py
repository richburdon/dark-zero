#!/usr/bin/env python
#
# Copyright 2014 Alien Laboratories, Inc.
#

# Initial set-up (must happen first).
import os
import env
env.init_paths(os.path.dirname(__file__))

# Initial set-up.
import logging
LOG = logging.getLogger('main')


# Main App.
import flask
app = flask.Flask(__name__, template_folder='templates')
app.debug = True


from injector import inject, Module


class AppModule(Module):
    def configure(self, binder):
        pass


@inject(app=flask.Flask)
class FlaskWrapper(object):

    def add_view(self, view, name):
        """
        http://flask.pocoo.org/docs/views
        http://flask.pocoo.org/docs/api/?highlight=add_url_rule#flask.Flask.add_url_rule
        """

        route = view.PATH
        assert route

        view_func = view.as_view(name)
        if isinstance(route, str):
            self.app.add_url_rule(route, view_func=view_func)
        else:
            for r in route:
                if isinstance(route, list):
                    self.app.add_url_rule(r, view_func=view_func)
                else:
                    self.app.add_url_rule(r, view_func=view_func, defaults=route[r])


import flask.views


class HomeView(flask.views.MethodView):
    PATH = '/'

    def get(self):
        return flask.render_template('hello.html')


@inject(app=FlaskWrapper)
class ViewModule(Module):
    def configure(self, binder):
        self.app.add_view(HomeView, 'Home')


# Flask injector modules.
from flask_injector import FlaskInjector
FlaskInjector(app=app, modules=[
    AppModule,
    ViewModule,
])


# Note: We don't need to call app.run() since we are embedded within the App Engine WSGI application server.
LOG.info('Running...')
