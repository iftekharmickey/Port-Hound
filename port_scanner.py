# Import necessary modules
import pyfiglet  # For creating an ASCII art banner
import sys  # For handling command-line arguments
import socket  # For network socket operations
from datetime import datetime  # For timestamping

# Create an ASCII art banner for the port scanner
ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)

# Check the number of command-line arguments
if len(sys.argv) == 2:
    # If there are two arguments, use the second argument as the target host
    target = socket.gethostbyname(sys.argv[1])
else:
    # If the number of arguments is not 2, print an error message and exit
    print("Invalid number of arguments")
    sys.exit()

# Print a separator line
print("-" * 50)
# Print information about the target host and scanning start time
print("Scanning target: " + target)
print("Scanning started at: " + str(datetime.now()))
# Print another separator line
print("-" * 50)

try:
    # Loop through ports from 1 to 65534
    for port in range(1, 65535):
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set a default timeout for the socket (1 second)
        socket.setdefaulttimeout(1)
        # Attempt to connect to the target host and port
        result = s.connect_ex((target, port))
        # Check if the connection was successful (result == 0) and print open port information
        if result == 0:
            print("Port {} is open".format(port))
        # Close the socket connection
        s.close()

except KeyboardInterrupt:
    # Handle a keyboard interrupt (e.g., Ctrl+C) and exit the program
    print("\nExiting Program")
    sys.exit()

except socket.gaierror:
    # Handle the case where the hostname could not be resolved
    print("\nHostname Could Not Be Resolved")
    sys.exit()

except socket.error:
    # Handle the case where the server is not responding
    print("\nServer Not Responding")
    sys.exit()
