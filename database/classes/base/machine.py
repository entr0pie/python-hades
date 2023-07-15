#!/bin/python3

from neomodel import StructuredNode
from neomodel import StringProperty
from neomodel import RelationshipTo

from database.classes.base.service import Service

class Machine(StructuredNode):
    """
    Generic class for a internet-conected device.
    Usage: host = Machine(name="hostname", address="192.168.0.1")
    """
    
    name = StringProperty()
    address = StringProperty()
    network = RelationshipTo('Machine', 'CONNECT')
    services = RelationshipTo('Service', 'HOSTS')
