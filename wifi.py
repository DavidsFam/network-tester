from subprocess import check_output
import re

def get_current_network_name():
    cur_network = check_output(["networksetup", "-getairportnetwork", "en0"]).decode("utf-8")
    return re.search("Current Wi-Fi Network:(.*)", cur_network).group(1)
