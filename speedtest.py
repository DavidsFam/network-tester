from datetime import datetime
from subprocess import check_output, CalledProcessError
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
        try:
            return json.loads(check_output(["speedtest", "--json"]))
        except CalledProcessError as e:
            print(f"speedtest failed with {e}")
            return {
                "ping": 0, #todo technically this should by infinity
                "upload": 0,
                "download": 0
            }

    def print_results(self):
        print(f"""
start time: {self.start_time}
end time:   {self.end_time}
ping:       {self.ping}
download:   {self.download}
upload:     {self.upload}
""")
