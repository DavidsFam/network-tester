from datetime import datetime
from subprocess import check_output, CalledProcessError
from halo import Halo
import json

class SpeedTest:
    def __init__(self):
        self.start_time = datetime.now().timestamp()
        results = self.run_speedtest()
        self.ping = results["ping"]["latency"]
        self.download_bytes = results["download"]["bytes"]
        self.download_bandwidth = results["download"]["bandwidth"]
        self.upload_bytes = results["upload"]["bytes"]
        self.upload_bandwidth = results["download"]["bandwidth"]
        self.end_time = datetime.now().timestamp()

    @Halo(text='testing...', spinner='dots')
    def run_speedtest(self):
        try:
            return json.loads(check_output(["speedtest", "-f", "json"], timeout=60))
        except CalledProcessError as e:
            print(f"speedtest failed with {e}")
            return {
                "ping": {"latency": 0}, #todo technically this should by infinity
                "upload": {"bytes": 0, "bandwidth": 0},
                "download": {"bytes": 0, "bandwidth": 0}
            }

    def print_results(self):
        print(f"""
start time:         {self.start_time}
end time:           {self.end_time}
ping:               {self.ping}
download bytes:     {self.download_bytes}
download bandwidth: {self.download_bandwidth}
upload bytes:       {self.upload_bytes}
upload bandwidth:   {self.upload_bandwidth}
""")
