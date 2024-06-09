import socket 

"""
    By Karla Quirós
    Reference: https://www.youtube.com/watch?v=gUod_PQgJKk
"""

def scan_ports(ip):
    """
    Scan all ports of a given IP address, there are 65535 ports in total.
    version 1: scan each port sequentially.
    return: None
    """
    for puerto in range(1, 65536):  # Each port
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            # Check which ports are open and closed
            result = sock.connect_ex((ip, puerto))
            if result == 0:
                print(f"Port {puerto} is open")
            else:
                print(f"Port {puerto} is closed")

if __name__ == "__main__":
    ip = input('Enter the IP address: ')  # Asking for the IP address to scan
    scan_ports(ip)

# The previous code is slow because it scans each port sequentially. We can use threads to scan multiple ports at the same time.

import socket
import concurrent.futures # to run multiple threads at the same time

def scan_port(ip, port):
    """
    Scan a single port of a given IP address.
    This function is called by the scan_ports function.
    return: a string with the result of the scan
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.5)  # Set a timeout for socket operations, so it doesn't wait forever
            result = sock.connect_ex((ip, port))
            if result == 0:
                return f"Port {port} is open"
            else:
                return f"Port {port} is closed"
    except socket.error:
        return f"Error scanning port {port}" 


def scan_ports(ip):
    """
    Scan all ports of a given IP address, using threads to improve performance.
    Uses ThreadPoolExecutor to run multiple threads at the same time.
    return: None
    """
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor: 
        futures = [executor.submit(scan_port, ip, port) for port in range(1, 65535)] 
        for future in concurrent.futures.as_completed(futures):
            print(future.result())

if __name__ == "__main__":
    # Asking for the IP address to scan
    ip = input('Enter the IP address: ') 
    scan_ports(ip)


# We can ask for only a range of ports to scan, instead of scanning all 65535 ports.

import socket
import concurrent.futures

def scan_specific_ports(ip, start_port, end_port):
    """
    Scan a range of ports of a given IP address.
    Uses threads to improve performance.
    return: None
    """
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        futures = [executor.submit(scan_port, ip, port) for port in range(start_port, end_port + 1)]
        for future in concurrent.futures.as_completed(futures):
            print(future.result())
            
if __name__ == "__main__":
    ip = input('Enter the IP address: ')
    start_port = int(input('Enter the starting port: '))
    end_port = int(input('Enter the ending port: '))
    scan_specific_ports(ip, start_port, end_port)
    