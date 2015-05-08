#
# Copyright 2014 Alien Laboratories, Inc.
#

import flask
from injector import inject


# TODO(burdon): Import from nexus.
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
