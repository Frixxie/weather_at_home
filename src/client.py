import json
import requests

if __name__ == '__main__':
    f = open('../stations.json')
    stations = json.load(f)
    for station in stations:
        for room, ip in station.items():
            res = requests.get(ip).json()
            temperature = res["temperature"]
            humidity = res["humidity"]
            print(f"Room: {room}, Temperature: {temperature}, Humidity: {humidity}")
