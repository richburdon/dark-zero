#!/usr/bin/env python
#
# Copyright 2014 Alien Laboratories, Inc.
#

import flask.views
from py2neo import Graph, Node, Relationship


class HomeView(flask.views.MethodView):
    PATH = '/'

    # TODO(burdon): Build table of instances and test connection to neo4j instance.
    def get(self):
        # https://cloud.google.com/appengine/docs/python/modules/functions
        from google.appengine.api import modules
        return flask.render_template('hello.html', modules=modules.get_modules())


class DataView(flask.views.MethodView):
    PATH = '/data'

    # TODO(burdon): Init + query paths
    def get(self):
        graph = Graph('http://192.168.99.100:32776/db/data/')
        import logging
        logging.info(graph)

        p1 = Node("Person", name="Alice")
        p2 = Node("Person", name="Bob")
        rel = Relationship(p1, "friend", p2)
        logging.info(rel)
        graph.create(rel)

        return flask.render_template('status.html')
