#!/bin/python3

from secrets import token_hex
from flask import Flask
from markupsafe import escape

from modules.net.util import getIPRange
from modules.net.scan import pingScan, synScan

from database.setup import setupDatabase
from database.classes.base.machine import Machine
from database.classes.protocols.http import HTTPServer
from database.classes.protocols.ssh import SSHServer

app = Flask(__name__)

setupDatabase()

@app.get("/netscan")
def networkScan():
    host = Machine(name="hackerspace", address="127.0.0.1").save()
    
    network: list = pingScan(getIPRange()).all_hosts()
    for address in network:
        machine = Machine(name=token_hex(5), address=address).save()
        host.network.connect(machine)
    
    return "Database changes made!"

@app.get("/portscan/tcp/syn/<name>")
def serviceDiscovery(name):
    host = Machine.nodes.get(name='hackerspace')
    
    machine = Machine.nodes.get_or_none(address=name)
    if machine == None:
        machine = Machine(name=token_hex(5), address=name).save()

    host.network.connect(machine)

    nm = synScan(name)
    services = nm[name]['tcp']

    for port in services.keys():
        if services[port]['name'] == "ssh":
            ssh = SSHServer(name="OpenSSH", version="8.2").save()
            machine.services.connect(ssh)

        if services[port]['name'] == "http":
            http = HTTPServer(name="Flask", version="").save()
            machine.services.connect(http)

    return services

if __name__ == "__main__":
    app.run("0.0.0.0", 8000)