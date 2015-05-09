#
# Copyright 2014 Alien Laboratories, Inc.
#

from flask import Flask
from injector import Module, inject, singleton
from py2neo import Graph
import os
import re
import subprocess


@singleton
class Config(object):
    def __init__(self, host):
        self.graph_host = host
        self.graph = Graph('http://' + host + ':7474/db/data/')


@singleton
class DevConfig(Config):
    def __init__(self):
        host = os.environ.get('DOCKER_HOST')
        if host:
            graphdb = re.match(r'(.*)://(.*):(.*)', host).group(1)
        else:
            # NOTE: When running from PyCharm, the environment variable is not set.
            p = subprocess.Popen('/usr/local/bin/boot2docker ip', shell=True, stdout=subprocess.PIPE)
            graphdb = p.stdout.read().strip()
        super(DevConfig, self).__init__(graphdb)


@singleton
class ProdConfig(Config):
    def __init__(self):
        # https://docs.docker.com/userguide/dockerlinks/
        graphdb = os.environ['GRAPHDB_PORT_7474_TCP_ADDR']
        super(ProdConfig, self).__init__(graphdb)


@inject(app=Flask)
class ConfigModule(Module):
    """
    """
    def configure(self, binder):
        if self.app.config['PROD']:
            config = ProdConfig()
        else:
            config = DevConfig()
        binder.bind(Config, to=config)
