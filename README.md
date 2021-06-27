# Weather at home

This is a simple system which uses rpi and DHT11 sensor with flask as a http
server and client to set up some cool IoT stuff.

On the rpi's connect the DHT11 sensors to the 5V GRND and PIN 14 and start run
the server.py. On another machiene run add the room and ip the server is placed
tr the stations.json file and run the client.py program

To run the client:

```
python3 src/client.py
```

The data comes on the format
Room,temperature,humidity
