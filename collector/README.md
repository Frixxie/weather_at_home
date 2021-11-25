# Weather at home

This is a simple system which uses rpi and [DHT11](https://whadda.com/product/dht11-digital-temperature-humidity-sensor-module-wpse311/)
sensor with flask as a http server and client to set up some cool IoT stuff.

On the rpi's connect the DHT11 sensors to the 5V, GRND and PIN 14 and start run
the server.py.

On the main machiene add the room and the ip of the pi
(which currently is on the format "http://<ip>:5000/data")
to the stations.json file.
Then you can run the client.py program

To run the client:

```sh
python3 src/client.py
```

The data comes on the format
room,temperature,humidity
