import os
import socket
import time
import whois

def who_is(target):
    return(whois.whois(target))

def ip_target(target):
    ip = socket.gethostbyname(target)
    return(f"O ip de {target} é {ip}")
    time.sleep(1)

def check_connections():
    return(os.system("ipconfig"))

def ping_target(target):
    req = os.system(f"ping {target}")
    return req


