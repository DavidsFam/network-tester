from speedtest import SpeedTest
import wifi

if __name__ == "__main__":
    for network in wifi.get_all_possible_networks():
        print(f"Attempting to connect to {network}")
        try:
            wifi.connect(network)
            print(f"Testing speed on {wifi.get_current_network_name()}")
            test = SpeedTest()
            test.print_results()
        except wifi.ConnectionException as e:
            print(e)