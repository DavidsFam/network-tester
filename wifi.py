from subprocess import check_output, call
import re
from halo import Halo
import time

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

def get_all_possible_networks():
    # todo this could maybe be cleaned up; gotta be a better way to get available networks
    all_previously_connected_networks = check_output(["networksetup", "-listpreferredwirelessnetworks", "en0"]).decode("utf-8")
    return all_previously_connected_networks.split("\n\t")[1:]

@Halo(text='connecting...', spinner='dots')
def connect(network):
    connection_error = check_output(["networksetup", "-setairportnetwork", "en0", network, WIFI_PASSWORD]).decode("utf-8")
    time.sleep(10)
    if(connection_error):
        raise ConnectionException(f"failed to connect to {network} with error: {connection_error}")
