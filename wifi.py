from subprocess import check_output
import re

def get_current_network_name():
    cur_network_data = check_output(["airport", "-I"]).decode("utf-8") 
    return re.search("\sSSID: (.*)\n", cur_network_data).group(1)
