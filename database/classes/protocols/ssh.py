#!/bin/python3

from database.classes.base.service import Service

class SSHServer(Service):
    """
    Class for SSH Servers, such as OpenSSH.
    
    Usage: SSHServer(name="OpenSSH", version="8.2")
    """
    
    def __init__(self, **kwargs):
        kwargs['protocol'] = 'ssh'
        super().__init__(**kwargs)