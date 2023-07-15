#!/bin/python3

from neomodel import Relationship
from neomodel.util import Database

from database.setup import setupDatabase
from database.classes.base.machine import Machine
from json import dumps

setupDatabase()

machines = Machine.nodes.all()

for node in machines:
    if node.name == 'hackerspace':
        host = node
        machines.pop(machines.index(host))
        break

relationships = Machine.getAllRelationships()

print(relationships)

