#
# Copyright 2014 Alien Laboratories, Inc.
#

import flask.views
from py2neo import Node, Relationship
from injector import inject
from config import Config


@inject(config=Config)
class HomeView(flask.views.MethodView):

    PATH = '/'

    def get(self):
        return flask.render_template('home.html', config=self.config)


@inject(config=Config)
class DataView(flask.views.MethodView):

    PATH = '/data'

    def get(self):
        p1 = Node("Person", name="Alice")
        p2 = Node("Person", name="Bob")
        rel = Relationship(p1, "friend", p2)
        self.config.graph.create(rel)

        # TODO(burdon): find root node and auto-init.
        for record in self.config.graph.cypher.execute("MATCH (p:Person) RETURN p.name AS name"):
            print(record[0])

        info = str(rel)
        return flask.render_template('data.html', info=info)
