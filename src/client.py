import json
import requests
from time import time

if __name__ == '__main__':
    f = open('stations.json')
    stations = json.load(f)
    time = int(time())
    for station in stations:
        for room, ip in station.items():
            res = requests.get(ip).json()
            temperature = res["temperature"]
            humidity = res["humidity"]
            print(f"{time},{room},{temperature},{humidity}")
