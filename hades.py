#!/bin/python3

from flask import Flask

from modules.net.util import getIPRange
from modules.net.scan import pingScan

app = Flask(__name__)

@app.route("/netscan")
def networkScan():
    network: str = getIPRange()
    return pingScan(network).all_hosts()

if __name__ == "__main__":
    app.run("0.0.0.0", 8000)