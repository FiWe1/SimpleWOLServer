A simple python / flask web app to Wake On Lan your PC
in its local network.

Deploy on your always on device connected physically to the PC
(ethernet, LAN), and make the server accesible on internet,
f.e. via VPN (Tailscale).

address.py:
Edit pc_mac address and LAN broadcast IP address.


Run wol_server.py. Now, you can wake your PC on URL:
http://your_ip:1950/wake