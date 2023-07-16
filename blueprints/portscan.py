#!/bin/python3

from secrets import token_hex

from flask import Blueprint

from modules.net.scan import synScan

from database.classes.base.machine import Host, Machine
from database.classes.base.service import Service
from database.classes.protocols.http import HTTPServer
from database.classes.protocols.ssh import SSHServer

portscan = Blueprint('portscan', __name__, url_prefix="/portscan")

@portscan.get("/tcp/syn/<address>")
def serviceDiscovery(address):
    host = Host.getInstance()
    machine = Machine.nodes.get_or_none(address=address)
    
    if machine == None:
        machine = Machine(name=token_hex(5), address=address).save()

    host.network.connect(machine)
    services = synScan(address)

    for port, info in services.items():
        if info['name'] == 'http':
            service = HTTPServer(name="HTTP Server", port=port)
        elif info['name'] == 'ssh':
            service = SSHServer(name="OpenSSH", port=port)
        else:
            service = Service(name=info['name'], port=port)

        service.save()
        machine.services.connect(service)

    return services


