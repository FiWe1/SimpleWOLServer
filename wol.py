import socket

from config import PC_MAC, LAN_BROADCAST


def wol(luna_mac_address: bytes) -> None:
    """Send a Wake-on-LAN magic packet to the specified MAC address."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    magic = b"\xff" * 6 + luna_mac_address * 16
    s.sendto(magic, (LAN_BROADCAST, 7))

if __name__ == "__main__":
    # Pass to wol the MAC address of the Ethernet port of the appliance to wake up
    wol(PC_MAC)
    print("The Force Awakens!")