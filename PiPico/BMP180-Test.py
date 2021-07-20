from machine import I2C, Pin
from time import sleep_ms
from bmp180 import BMP180

# Pico has 2 I2C buses (not counting the PIO)
bus = I2C(0, scl=Pin(17), sda=Pin(16), freq=100000)

# Print out any addresses found
#devices = bus.scan()

#if devices:
#    for d in devices:
#        print(hex(d))

sleep_ms(200)

bmp180 = BMP180(bus, 250.41)
bmp180.oversample = 2
bmp180.sealevel = 1049.92

while 1:
    temp = bmp180.temperature
    p = bmp180.pressure
    altitude = bmp180.altitude
    bmp180.makegauge()
    print(temp, p, altitude)
    sleep_ms(500)
