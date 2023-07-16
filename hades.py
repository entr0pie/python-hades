#!/bin/python3

from secrets import token_hex
from flask import Flask
from markupsafe import escape

from modules.net.util import getIPRange
from modules.net.scan import pingScan, synScan

from database.setup import setupDatabase
from database.classes.base.machine import Machine, Host
from database.classes.protocols.http import HTTPServer
from database.classes.protocols.ssh import SSHServer

from blueprints.netscan import netscan
from blueprints.portscan import portscan

setupDatabase()
host = Host(name='Hades').save()

app = Flask(__name__)
app.register_blueprint(netscan)
app.register_blueprint(portscan)

if __name__ == "__main__":
    app.run("0.0.0.0", 8000)