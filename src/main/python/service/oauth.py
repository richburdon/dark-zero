#
# Copyright 2014 Alien Laboratories, Inc.
#

# https://flask-oauthlib.readthedocs.org/en/latest/client.html#oauth2-client

from flask import Flask
from injector import inject, MappingKey, singleton

from flask_oauthlib.client import OAuth


OAUTH_CONFIG_KEY = MappingKey('oauth.OAuthRegistry')

@singleton
@inject(
    app=Flask,
    configs=OAUTH_CONFIG_KEY
)
class OAuthRegistry(object):

    def __init__(self):
        self.oauth = OAuth(self.app)

        # Map of remote apps indexed by service ID.
        self.remote = dict()

        # Create remote apps.
        for config_id in self.configs:
            print 'Registered OAuth: {0}'.format(config_id)
            self.app.config[config_id] = self.configs[config_id]
            remote = self.oauth.remote_app(config_id, app_key=config_id)
            self.remote[config_id] = remote
