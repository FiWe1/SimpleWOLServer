from flask import Flask

import wol
from constant_address import PC_MAC


app = Flask(__name__)


@app.route("/wake")
def wake():
    wol.wol(PC_MAC)  # Change this to your desktop’s Ethernet MAC
    return "Wake-on-LAN packet sent!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1950)
