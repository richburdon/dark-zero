#
# Copyright 2014 Alien Laboratories, Inc.
#

import flask.views
import json
from injector import inject
from config import Config
from data import Database


@inject(config=Config)
class HomeView(flask.views.MethodView):

    PATH = '/'
    NAME = 'Home'

    def get(self):
        return flask.render_template('home.html', config=self.config)


@inject(config=Config)
class AdminView(flask.views.MethodView):

    PATH = '/admin'
    NAME = 'ADMIN'

    def get(self):
        # Load admin meta data.
        # TODO(burdon): Reconcile static and dynamic config (e.g., hostname).
        admin = json.loads(open('config/admin.json', 'r').read())
        return flask.render_template('admin.html', admin=admin)


@inject(db=Database)
class DataView(flask.views.MethodView):

    PATH = '/data'
    NAME = 'DATA'

    def get(self):
        self.db.add()
        info = str(self.db)
        return flask.render_template('data.html', info=info)
