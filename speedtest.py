from datetime import datetime
from subprocess import check_output
import json

class SpeedTest:
    def __init__(self):
        self.start_time = datetime.now().timestamp()
        results = self.run_speedtest()
        self.ping = results["ping"]
        self.download = results["download"]
        self.upload = results["upload"]
        self.end_time = datetime.now().timestamp()
    
    def run_speedtest(self):
        return json.loads(check_output(["speedtest", "--json"]))

    def print_results(self):
        print(f"""
start time: {self.start_time}
end time:   {self.end_time}
ping:       {self.ping}
download:   {self.download}
upload:     {self.upload}
""")
