#!/usr/bin/env python
#
# Copyright 2014 Alien Laboratories, Inc.
#

import flask.views


class HomeView(flask.views.MethodView):
    PATH = '/'

    def get(self):
        return flask.render_template('hello.html')
