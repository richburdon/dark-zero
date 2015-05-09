#
# Copyright 2014 Alien Laboratories, Inc.
#

from injector import inject
from config import Config
from py2neo import Node, Relationship
import random

# http://py2neo.org/2.0/cypher.html#cypher-resource

@inject(config=Config)
class Database(object):

    def __str__(self):
        items = self.config.graph.cypher.execute('MATCH (i:Item) RETURN i')
        return 'Graph({:d})'.format(len(items))

    def add(self):
        items = self.config.graph.cypher.execute('MATCH (i:Item) RETURN i')
        name = 'Item-{:d}'.format(len(items) + 1)
        item1 = Node('Item', name=name)

        if items:
            item2 = random.sample(items.to_subgraph().nodes, 1)[0]
            rel = Relationship(item2, 'linked', item1)
            self.config.graph.create(rel)
        else:
            self.config.graph.create(item1)


class UserDatabase(object):
    pass
