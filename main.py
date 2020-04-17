from speedtest import SpeedTest
import wifi

if __name__ == "__main__":
    print(f"Testing speed on {wifi.get_current_network_name()}")
    test = SpeedTest()
    test.print_results()