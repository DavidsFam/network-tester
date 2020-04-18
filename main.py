from speedtest import SpeedTest
import wifi

def test(network):
    wifi.connect(network)
    print(f"testing speed on {wifi.get_current_network_name()}")
    test = SpeedTest()
    test.print_results() # todo aggregate and display these someplace

if __name__ == "__main__":
    for network in wifi.get_all_possible_networks():
        print(f"attempting to connect to {network}")
        try:
            test(network)
        except wifi.ConnectionException as e:
            print(e)