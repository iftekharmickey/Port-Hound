# Port Scanner #

## What is a socket? ##

A socket is one endpoint of a two-way communication link between two programs running on the network. A socket is bound to a port number so that the TCP layer can identify the application that data is destined to be sent to.

For more information about sockets, visit [Oracle](https://docs.oracle.com/javase/tutorial/networking/sockets/definition.html).

## What is the difference between a socket and a port? ##

A socket consists of three things:

  1. An IP address
  2. A transport protocol
  3. A port number

A port is a number between 1 and 65535 inclusive that signifies a logical gate in a device. Every connection between a client and server requires a unique socket. For example:

  - 1030 is a port.
  - (10.1.1.2, TCP, port 1030) is a socket.

## What is a port scanner? ##

A port scanner is a program that checks network ports for one of three possible statuses – open, closed, or filtered. Port scanners are valuable tools in diagnosing network and connectivity issues. However, attackers use port scanners to detect possible access points for infiltration and identify what kinds of devices you are running on the network, such as firewalls, proxy servers, or VPN servers.

## How does a port scanner work? ##

A port scanner sends a network request to connect to a specific TCP or UDP port on a computer and records the response. To put it another way, the scanner sends a packet of network data to a port to check its current status. For example, if we wanted to check whether a web server was operating correctly, we would check the status of port 80 on that server to ensure it was open and listening. The status helps network engineers diagnose network issues or application connectivity issues or helps attackers find possible ports to infiltrate your network.
