from flask import Flask, redirect, url_for

import wol
from config import PC_MAC, PORT


app = Flask(__name__)


@app.route("/")
def home():
    return "Go to <a href='/wake'>/wake</a> to WOL your device."


@app.route("/wake")
def wake():
    try:
        wol.wol(PC_MAC, times=3)  # Edit your desktop’s Ethernet MAC in config.py
    except Exception:
        return redirect(url_for("failure"))
    
    return redirect(url_for("success"))


@app.route("/success")
def success():
    return "Wake-on-LAN packet sent!\n" + "<a href='/wake'>Click</a> to resend."


@app.route("/failure")
def failure():
    return "Failed to send WOL packet. Try again: \n" + "<a href='/wake'>Click</a> to resend."


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
