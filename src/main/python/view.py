#!/usr/bin/env python
#
# Copyright 2014 Alien Laboratories, Inc.
#

import flask.views
from py2neo import Graph, Node, Relationship


class HomeView(flask.views.MethodView):
    PATH = '/'

    def get(self):
        # https://cloud.google.com/appengine/docs/python/modules/functions
        # https://cloud.google.com/appengine/docs/python/modules/routing
        from google.appengine.api import modules
        module_map = {}
        for module in modules.get_modules():
            version = modules.get_default_version(module)
            module_map[module] = {
                'version': version,
                'hostname': modules.get_hostname(module, version)
            }
        return flask.render_template('hello.html', modules=module_map)


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
