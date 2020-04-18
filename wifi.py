from subprocess import check_output, call
import re
from halo import Halo

WIFI_PASSWORD = open(".wifipassword","r+").read()
NETWORKSETUP_CURRENT_NETWORK_REGEX = "Current Wi-Fi Network:(.*)"
class ConnectionException(Exception):
    pass

def get_current_network_name():
    cur_network = check_output(["networksetup", "-getairportnetwork", "en0"]).decode("utf-8")
    if(re.match(NETWORKSETUP_CURRENT_NETWORK_REGEX, cur_network)):
        return re.search("Current Wi-Fi Network:(.*)", cur_network).group(1)
    else:
        raise ConnectionException("not currently connected to wifi")

def get_all_possible_networks():
    # todo this could maybe be cleaned up; gotta be a better way to get available networks
    all_previously_connected_networks = check_output(["networksetup", "-listpreferredwirelessnetworks", "en0"]).decode("utf-8")
    return all_previously_connected_networks.split("\n\t")[1:]

@Halo(text='Connecting', spinner='dots')
def connect(network):
    connection_result = check_output(["networksetup", "-setairportnetwork", "en0", network, WIFI_PASSWORD]).decode("utf-8")
    # todo figure out the real error state here; also determine if we have to sleep
    print(connection_result)
    if(re.match("Error.*", connection_result)):
        raise ConnectionException(f"failed to connect to {network}")
