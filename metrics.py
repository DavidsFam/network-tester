from prometheus_client import CollectorRegistry, Gauge, push_to_gateway

registry = CollectorRegistry()
#todo torkel
download_gauge = Gauge('download_speed', 'download speed (bits per second)', ['network'], registry=registry)
upload_gauge = Gauge('upload_speed', 'upload speed (bits per second)', ['network'], registry=registry)
ping_gauge = Gauge('ping_latency', 'download speed (milliseconds)', ['network'], registry=registry)

def record(network, test):
    download_gauge.labels(network=network).set(test.download)
    upload_gauge.labels(network=network).set(test.upload)
    ping_gauge.labels(network=network).set(test.ping)
    push_to_gateway('http://localhost:9091', job='network-config-test', registry=registry)