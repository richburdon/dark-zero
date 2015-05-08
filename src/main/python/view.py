#!/usr/bin/env python
#
# Copyright 2014 Alien Laboratories, Inc.
#

import flask.views
import os
from py2neo import Graph, Node, Relationship


class HomeView(flask.views.MethodView):
    PATH = '/'

    def get(self):
        graphdb = os.environ['GRAPHDB_PORT_7474_TCP_ADDR']
        return flask.render_template('home.html', graphdb=graphdb)


class DataView(flask.views.MethodView):
    PATH = '/data'

    # TODO(burdon): Init + query paths
    def get(self):
        graphdb = os.environ['GRAPHDB_PORT_7474_TCP_ADDR']
        graph = Graph('http://' + graphdb + ':7474/db/data/')

        p1 = Node("Person", name="Alice")
        p2 = Node("Person", name="Bob")
        rel = Relationship(p1, "friend", p2)
        graph.create(rel)

        info = str(rel)
        return flask.render_template('status.html', info=info)
