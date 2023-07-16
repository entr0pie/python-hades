#!/bin/python3

from neomodel.util import Database
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

    @staticmethod
    def getAllRelationships():
        edges: list = []
        
        database = Database()
        result, _ = database.cypher_query("MATCH ()-[r]->() RETURN r")

        for relationship in result:
            edges.append(relationship[0])

        return edges

    @staticmethod
    def getJSONRelationships():
        rels: list = Machine.getAllRelationships()
        json_edges: list = []

        for rel in rels:
            json_rel: dict = {}
            json_rel['id'] = rel.id
            json_rel['from'] = rel.nodes[0].id
            json_rel['to'] = rel.nodes[1].id
            json_rel['type'] = rel.type
            json_rel['properties'] = rel._properties

            json_edges.append(json_rel)

        return json_edges


class Host(Machine):
    """
    Special class for the Host Machine.
    Designed with Singleton.
    Usage: host = Host.getHost()
    """

    _instance = None

    @staticmethod
    def getInstance():
        if Host._instance == None:
            Host._instance = Machine.nodes.get(name='Hades')

        return Host._instance

