# Port-Scanner

## Overview

This Python script serves as a versatile network utility. It allows users to scan a target IP address for open ports within the range of 1 to 65535. Upon execution, the script establishes socket connections to various ports, checking their status. When an open port is encountered, the script reports it as "Port [number] is open."

This tool is invaluable for network administrators and security professionals, aiding in identifying open ports, potential vulnerabilities, and network configuration issues. It leverages Python's socket module and offers a simple yet effective means of assessing the network perimeter.

### Usage

You can use this script to check which ports are open on a remote server or device. Please make sure you have the necessary permissions to perform port scanning.

  ```bash
  python port_scanner.py <target_host>
  ```
Replace <target_host> with the hostname or IP address of the target you want to scan.

### Requirements and Dependencies
- Python 3.x
- pyfiglet

You can install the required dependency using 'pip':

  ```bash
  pip install pyfiglet
  ```

### Author

This tool was developed by Iftekhar Tahir. If you have any questions or feedback, please don't hesitate to reach out to me at iftekhar.tahir@proton.me.

Feel free to fork and modify this script to suit your needs.

Happy scanning!
