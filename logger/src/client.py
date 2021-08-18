import json
import requests
from time import time


def get_data(stations_file):
    """
    This method gets the data from the weather stations
    """
    with open(stations_file) as f:
        stations = json.load(f)
        dt = int(time())
        for station in stations:
            # There are only one item in station
            # This was the easiest way to unpack them
            for room, ip in station.items():
                res = requests.get(ip).json()
                temperature = res["temperature"]
                humidity = res["humidity"]
                print(f"{dt},{room},{temperature},{humidity}")


if __name__ == '__main__':
    get_data('/home/fredrik/projects/weather_at_home/stations.json')
