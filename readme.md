# Simple WOL Server

A simple python / flask web app to Wake On Lan your PC
in its local network.

Deploy on your always on device connected physically to the PC
(ethernet, LAN), and make the server accesible on internet,
f.e. via VPN (Tailscale).

config.py:
Edit pc_mac address and LAN broadcast IP address, optionally app port.
- to ignore local changes in config.py (changing ports), run:
    git update-index --assume-unchanged config.py


Install required packages:
1. create and activate virtual environment:
python -m venv .venv
source .venv/bin/activate

2. install:
pip install -r requirements.txt


To run the app, run:
python wol_server.py

Now, you can wake your PC on URL:
http://your_ip:1950/wake