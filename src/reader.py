import RPi.GPIO as GPIO
from dht11 import DHT11

# init GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# will be using pin 14 to send and recieve data
dht11 = DHT11(pin = 14)

def read_from_sensor():
    successfull_read = False
    while successfull_read is False:
        res = dht11.read()
        if res.is_valid():
            successfull_read = True
            return (res.temperature, res.humidity)


if __name__ == '__main__':
    print(read_from_sensor())
