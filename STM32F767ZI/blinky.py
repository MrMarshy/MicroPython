# Blinky STM32F767ZI
import pyb

GreenUserLed = pyb.LED(1)
BlueUserLed = pyb.LED(2)
RedUserLed = pyb.LED(3)

while True:
    GreenUserLed.on()
    BlueUserLed.on()
    RedUserLed.on()
    
    pyb.delay(1000)
    
    GreenUserLed.off()
    BlueUserLed.off()
    RedUserLed.off()
    
    pyb.delay(1000)