#
# Copyright 2014 Alien Laboratories, Inc.
#

import flask.views
from flask import Flask
from injector import inject
import json
import os

from config import Config
from data import Database


@inject(config=Config)
class HomeView(flask.views.MethodView):

    PATH = '/'
    NAME = 'Home'

    def get(self):
        return flask.render_template('home.html', config=self.config)


@inject(config=Config, app=Flask)
class AdminView(flask.views.MethodView):

    PATH = '/admin'
    NAME = 'ADMIN'

    MAP = {'SERVER': ''}

    def get(self):
        # Update map.
        from urlparse import urlparse
        AdminView.MAP['SERVER'] = urlparse(flask.request.url_root).netloc.split(':')[0]
        print AdminView.MAP

        # Load admin meta data.
        # TODO(burdon): Reconcile static and dynamic config (e.g., hostname).
        # TODO(burdon): Make each object with title, etc.
        admin = json.loads(open(os.path.join(os.getcwd(), 'config/admin.json'), 'r').read())
        for key in admin['links']:
            value = admin['links'][key]
            for i in AdminView.MAP:
                match = '__' + i + '__'
                if value.find(match) != -1:
                    admin['links'][key] = value.replace(match, AdminView.MAP[i])
                    print value

        return flask.render_template('admin.html', app=self.app, config=self.config, admin=admin)


@inject(db=Database)
class DataView(flask.views.MethodView):

    PATH = '/data'
    NAME = 'DATA'

    def get(self):
        self.db.add()
        info = str(self.db)
        return flask.render_template('data.html', info=info)
