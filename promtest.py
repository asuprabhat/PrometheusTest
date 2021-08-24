import prometheus_client as prom
import requests
import time
from contextlib import suppress


for name in list(prom.REGISTRY._names_to_collectors.values()):
    with suppress(KeyError):
        prom.REGISTRY.unregister(name)

UP_GAUGE=prom.Gauge('sample_external_url_up', 'URL Up', ['url'])
RESPONSE_TIME_GAUGE = prom.Gauge('sample_external_url_response_ms', 'Url response time in ms', ["url"])
URL_LIST = ["https://httpstat.us/503", "https://httpstat.us/200"]

def get_response(url: str) -> dict:
    response = requests.get(url)
    response_time = response.elapsed.total_seconds()
    if response.status_code == 200:
        url_status = 1
    else:
        url_status = 0
    UP_GAUGE.labels(url).set(url_status)
    RESPONSE_TIME_GAUGE.labels(url).set(response_time)

def get_url_status():
    while True:
        for url_name in URL_LIST:
            get_response(url_name)
        time.sleep(5)


if __name__ == '__main__':
    prom.start_http_server(80)
    get_url_status()