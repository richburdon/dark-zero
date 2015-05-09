#
# Copyright 2014 Alien Laboratories, Inc.
#

import flask
from flask_injector import FlaskInjector
from injector import inject, singleton, Module


# NOTE: Objects MUST inherit from object.
# http://stackoverflow.com/questions/54867/what-is-the-difference-between-old-style-and-new-style-classes-in-python
@singleton
class Foo(object):
    def __init__(self):
        pass


class Zoo(Foo):
    pass


@inject(foo=Foo)
class Bar(object):
    def __init__(self):
        pass


class TestModule(Module):
    def configure(self, binder):
        binder.bind(Foo, Zoo())


app = flask.Flask(__name__)
FlaskInjector(app=app, modules=[
    TestModule
])
