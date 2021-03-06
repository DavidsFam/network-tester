from prometheus_client import CollectorRegistry, Gauge, push_to_gateway

registry = CollectorRegistry()
download_bandwidth_gauge = Gauge('download_bandwidth', 'download bandwidth', ['network'], registry=registry)
download_bytes_gauge = Gauge('download_speed', 'download speed (bytes per second)', ['network'], registry=registry)
upload_bandwidth_gauge = Gauge('upload_bandwidth', 'upload bandwidth', ['network'], registry=registry)
upload_bytes_gauge = Gauge('upload_speed', 'upload speed (bytes per second)', ['network'], registry=registry)
ping_gauge = Gauge('ping_latency', 'download speed (milliseconds)', ['network'], registry=registry)

def record(network, test):
    download_bandwidth_gauge.labels(network=network).set(test.download_bandwidth)
    download_bytes_gauge.labels(network=network).set(test.download_bytes)
    upload_bandwidth_gauge.labels(network=network).set(test.upload_bandwidth)
    upload_bytes_gauge.labels(network=network).set(test.upload_bytes)
    ping_gauge.labels(network=network).set(test.ping)
    push_to_gateway('http://localhost:9091', job='network-config-test', registry=registry)

def recordFailure(network):
    download_bandwidth_gauge.labels(network=network).set(0)
    download_bytes_gauge.labels(network=network).set(0)
    upload_bandwidth_gauge.labels(network=network).set(0)
    upload_bytes_gauge.labels(network=network).set(0)
    ping_gauge.labels(network=network).set(0)
    push_to_gateway('http://localhost:9091', job='network-config-test', registry=registry)
