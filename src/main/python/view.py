#
# Copyright 2014 Alien Laboratories, Inc.
#

import flask.views
from injector import inject
from config import Config
from data import Database


@inject(config=Config)
class HomeView(flask.views.MethodView):

    PATH = '/'

    def get(self):
        return flask.render_template('home.html', config=self.config)


@inject(db=Database)
class DataView(flask.views.MethodView):

    PATH = '/data'

    def get(self):
        self.db.add()
        info = str(self.db)
        return flask.render_template('data.html', info=info)
