import time

import requests
from bs4 import BeautifulSoup
from prometheus_client import start_http_server, Gauge

RADIATION_VALUE = Gauge('radiation_value', 'Radiation value', labelnames=('location',))

URL = "https://www.npp.zp.ua/uk/safety/arms"


def update_stats():
    resp = requests.get(URL)
    data = resp.text
    soup = BeautifulSoup(data)
    content = soup.find(id="block-porto-content")
    trs = content.find_all('tr')[1:]

    for tr in trs:
        tds = tr.find_all('td')
        location_td, value_td = tds[0], tds[1]
        location, value = location_td.text.strip(), value_td.text.strip()
        RADIATION_VALUE.labels(location=location).set(value)


if __name__ == '__main__':
    start_http_server(8000)
    while True:
        update_stats()
        time.sleep(50)
