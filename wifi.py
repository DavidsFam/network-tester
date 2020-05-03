from subprocess import check_output, call
import re
from halo import Halo
import time
import os

WIFI_PASSWORD = open(".wifipassword","r+").read()
NETWORKSETUP_CURRENT_NETWORK_REGEX = "Current Wi-Fi Network:(.*)"
class ConnectionException(Exception):
    pass

def maybe_get_current_network_name():
    cur_network = check_output(["networksetup", "-getairportnetwork", "en0"]).decode("utf-8")
    if(re.match(NETWORKSETUP_CURRENT_NETWORK_REGEX, cur_network)):
        return re.search("Current Wi-Fi Network: (.*)", cur_network).group(1)

def get_current_network_name():
    cur_network = maybe_get_current_network_name()
    if(cur_network is None):
        raise ConnectionException("not currently connected to wifi")
    return cur_network

@Halo(text='scanning for networks...', spinner='dots')
def get_available_networks():
    available_networks = check_output(["airport", "--scan", "--xml"]).decode("utf-8")
    if(len(available_networks) > 0): # todo sometimes airport just immediately returns an empty result
        available_network_names = re.findall(r'<key>SSID_STR<\/key>\n\s+<string>(.*)<\/string>', available_networks)
        print(f"Found networks: {', '.join(available_network_names)}")
        return available_network_names

@Halo(text='connecting...', spinner='dots')
def connect(network):
    connection_error = check_output(["networksetup", "-setairportnetwork", "en0", network, WIFI_PASSWORD]).decode("utf-8")
    time.sleep(30) # i guess the network takes a little while after it's been connected to
    if(connection_error):
        raise ConnectionException(f"failed to connect to {network} with error: {connection_error}")

def check_internet_connectivity():
    response = os.system("ping -c 1 google.com")
    if response == 0:
        return True
    else:
        return False
