from speedtest import SpeedTest
import wifi
import metrics

def test(network):
    try:
        if(not wifi.get_current_network_name() == network):
            print(f"attempting to connect to {network}")
            wifi.connect(network)
        print(f"testing speed on {wifi.get_current_network_name()}")
        test = SpeedTest()
        test.print_results() # todo aggregate and display these someplace
        metrics.record(network, test)
    except wifi.ConnectionException as e:
        print(e)

def test_all():
    [test(network) for network in wifi.get_all_possible_networks()]

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='test the network speed')
    parser.add_argument('--network', type=str, default="", help='name of network to test (optional)')
    args = parser.parse_args()
    if(args.network):
        test(args.network)
    else:
        test_all()
