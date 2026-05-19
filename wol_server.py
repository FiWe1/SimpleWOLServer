from flask import Flask, redirect, url_for, render_template

import wol
from config import PC_MAC, PC_NAME, PORT


PC_MAC_BIN = bytes.fromhex(PC_MAC.replace(":", ""))
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("wake.html", pc_name=PC_NAME)


@app.route("/wake")
def wake():
    try:
        wol.wol(PC_MAC_BIN, times=3)  # Edit your desktop’s Ethernet MAC in config.py
    except Exception as e:
        print(e)
        return redirect(url_for("failure"))

    return redirect(url_for("success", pc_name=PC_NAME))


@app.route("/success")
def success():
    return render_template("success.html", pc_name=PC_NAME)


@app.route("/failure")
def failure():
    return render_template("failure.html", pc_name=PC_NAME)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
