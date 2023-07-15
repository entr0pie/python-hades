#!/bin/python3

from database.classes.base.service import Service

class HTTPServer(Service):
    """
    Class for the HTTPServer node. Nginx, Flask, Apache,
    Express, and any other backend server is represented
    here.

    Usage: HTTPServer(name="Nginx", version="1.18.0")
    """
    
    def __init__(self, **kwargs):
        kwargs['protocol'] = 'http'
        super().__init__(**kwargs)
    