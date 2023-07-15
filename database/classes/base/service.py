#!/bin/python3

from neomodel import StructuredNode
from neomodel import StringProperty, IntegerProperty
from neomodel import RelationshipTo

class Service(StructuredNode):
    """
    Generic class for a service (aka. open ports).
    This class isn't meant for implementation on the entrypoint. 
    Search what fits best for your in the database.classes.protocols 
    package.
    """
    
    name = StringProperty()
    protocol = StringProperty()
    port = IntegerProperty()
    version = StringProperty()