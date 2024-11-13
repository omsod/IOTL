import Adafruit_DHT
import os, sys
from time import sleep
import requests
import RPi.GPIO as GPIO

baseURL= 'https://api.thingspeak.com/update?api_key=OBZOESL11D0P65DR'
SensorPin = 4
while True:

    try:
        print("Program is Running")

        humi, temp = Adafruit_DHT.read(Adafruit_DHT.DHT11, SensorPin)
        if (humi > 0) and (temp > 0):

            print(humi)

            print(temp)

            print("Data received")

            x='{}{}{}{}{}'.format(baseURL, '&field1=', temp, '&field2=', humi)

            y = requests.post(x)

            print(y.status_code)

            print(x)

        sleep(5)

    except :
        print("Data not received")
        sleep(5)