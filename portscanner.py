import socket
from datetime import datetime

# Create an ASCII art banner for the port scanner
banner = """
###   ###  ###  ###   #   #  ###  #   # #   # ####
#  # #   # #  #  #    #   # #   # #   # ##  # #   #
#  # #   # #  #  #    ##### #   # #   # # # # #   #
###  #   # ###   #    #   # #   # #   # # # # #   #
#    #   # #  #  #    #   # #   # #   # #  ## #   #
#     ###  #  #  #    #   #  ###   ###  #   # ####
"""
print(banner)

# Get the target host from user input
target = input("Enter the IP address or domain to scan: ")

# Print a separator line
print("-" * 50)
print(f"Scanning target: {target}")
print(f"Scanning started at: {datetime.now()}")
print("-" * 50)

def scan_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((target, port))
    s.close()
    return result == 0

open_ports = []

try:
    for port in range(1, 65535):
        if scan_port(port):
            open_ports.append(port)
            print(f"Port {port}: Open")
        else:
            print(f"Port {port}: Closed")

except KeyboardInterrupt:
    print("\nExiting Program")

except socket.gaierror:
    print("\nHostname Could Not Be Resolved")

except socket.error:
    print("\nServer Not Responding")

# Print the final list of open ports
if open_ports:
    print(f"Open ports: {', '.join(map(str, open_ports))}")
else:
    print("No open ports found.")
