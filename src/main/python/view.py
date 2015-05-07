#!/usr/bin/env python
#
# Copyright 2014 Alien Laboratories, Inc.
#

import flask.views
from py2neo import Graph, Node, Relationship


class HomeView(flask.views.MethodView):
    PATH = '/'

    def get(self):
        return flask.render_template('hello.html')


class DataView(flask.views.MethodView):
    PATH = '/data'

    # TODO(burdon): Init + query paths
    def get(self):
        graph = Graph('http://0.0.0.0:7474/db/data/')
        import logging
        logging.info(graph)

        p1 = Node("Person", name="Alice")
        p2 = Node("Person", name="Bob")
        rel = Relationship(p1, "friend", p2)
        logging.info(rel)
        graph.create(rel)

        return flask.render_template('status.html')
