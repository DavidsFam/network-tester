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

    @Halo(text='connecting...', spinner='dots')
    def run_speedtest(self):
        try:
            return json.loads(check_output(["speedtest", "-f", "json"]))
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
download:   {self.download} #todo torkel
upload:     {self.upload} #todo torkel
""")
