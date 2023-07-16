#!/bin/python3

from secrets import token_hex

from flask import Blueprint

from database.classes.base.machine import Host, Machine
from modules.net.util import getIPRange
from modules.net.scan import pingScan

netscan = Blueprint('netscan', __name__, url_prefix='/netscan')

@netscan.get("/")
def scanNetwork():
    host = Host.getInstance()
    
    ip_range = getIPRange()
    network: list = pingScan(ip_range)
    
    for address in network:
        machine = Machine(name=token_hex(5), address=address).save()
        host.network.connect(machine)

    return network