from flask import Flask

import wol
from config import PC_MAC, PORT


app = Flask(__name__)


@app.route("/")
def home():
    return "Go to <a href='/wake'>/wake</a> to WOL your device."

@app.route("/wake")
def wake():
    wol.wol(PC_MAC)  # Change this to your desktop’s Ethernet MAC
    return "Wake-on-LAN packet sent!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
