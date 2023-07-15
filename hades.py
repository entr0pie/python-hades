#!/bin/python3

from secrets import token_hex
from flask import Flask

from modules.net.util import getIPRange
from modules.net.scan import pingScan

from database.setup import setupDatabase
from database.classes.base.machine import Machine

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

if __name__ == "__main__":
    app.run("0.0.0.0", 8000)