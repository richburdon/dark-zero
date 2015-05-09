#
# Copyright 2014 Alien Laboratories, Inc.
#

from injector import Module, singleton
from py2neo import Graph
import os
import re


class Config(object):
    def __init__(self, host):
        self.graph_host = host
        self.graph = Graph('http://' + host + ':7474/db/data/')


class DevConfigModule(Module):
    """
    """
    def configure(self, binder):
        host = os.environ.get('DOCKER_HOST')
        if host:
            graphdb = re.match(r'(.*)://(.*):(.*)', host).group(1)
        else:
            # NOTE: When running from PyCharm, the environment variable is not set.
            import subprocess
            p = subprocess.Popen('/usr/local/bin/boot2docker ip', shell=True, stdout=subprocess.PIPE)
            graphdb = p.stdout.read().strip()

        binder.bind(Config, to=Config(graphdb), scope=singleton)


class ProdConfigModule(Module):
    """
    """
    def configure(self, binder):
        # https://docs.docker.com/userguide/dockerlinks/
        graphdb = os.environ['GRAPHDB_PORT_7474_TCP_ADDR']
        print graphdb
        binder.bind(Config, to=Config(graphdb), scope=singleton)
