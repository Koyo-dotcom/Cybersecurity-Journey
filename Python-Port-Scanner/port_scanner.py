import argparse
from colorama import init, Fore
import socket
import sys
import pyfiglet 
from datetime import datetime
from threading import Thread, Lock

init()
GREEN = Fore.GREEN
RESET = Fore.RESET
GRAY = Fore.LIGHTBLACK_EX

ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)

if len(sys.argv) == 2:
    target = sys.argv[1]
else:
    print("Invalid amount of variables")
    sys.exit()

print("-" * 50)
print("Scanning Target: " + target)
print("Scanning started at:" + str(datetime.now()))
print("-" * 50)

print_lock = Lock()
def port_scan(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        s.connect_ex((host, port))
    except:
        with print_lock:
            print(f"{GRAY}{host}:{port} is closed   {RESET}")
    else:
        with print_lock:
            print(f"{GREEN}{host}:{port} is open   {RESET}")
    finally:
        s.close()

port_scan(target)