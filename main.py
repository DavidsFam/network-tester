from speedtest import SpeedTest
import wifi
import metrics
import time

def test(network):
    try:
        if(not wifi.maybe_get_current_network_name() == network):
            print(f"attempting to connect to {network}")
            wifi.connect(network)
        print(f"testing speed on {wifi.get_current_network_name()}")
        test = SpeedTest()
        test.print_results()
        if(not test.passed):
            if(wifi.check_internet_connectivity()):
                print("********** got a failed test but the internet *is* connected")
        metrics.record(network, test)
    except wifi.ConnectionException as e:
        metrics.recordFailure(network)
        print(e)

def test_all():
    networks = ['Davids', 'Davids 5', 'Fairpoint8663_Ext'] # todo wifi.get_all_possible_networks() is not ready for prime time just yet
    [test(network) for network in networks]

def run(network):
    if(args.network):
        test(args.network)
    else:
        test_all()

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='test the network speed')
    parser.add_argument('--loop', action='store_true', help='rerun tests continuously')
    parser.add_argument('--network', type=str, default="", help='name of network to test (optional)')
    args = parser.parse_args()
    if(args.loop):
        print("looping; quit out with control + c")
        while True:
            try:
                run(args.network)
            except RuntimeError as e:
                print(e)
            except KeyboardInterrupt as e:
                print("have a nice day")
                exit()
    else:
        run(args.network)
