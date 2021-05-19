import pyb

def main():
    
    print("Blinky button demo")
    RedLed = pyb.Pin(pyb.Pin.cpu.B14, mode=pyb.Pin.OUT_PP)
    
    Button = pyb.Pin(pyb.Pin.cpu.C13, mode=pyb.Pin.IN, pull=pyb.Pin.PULL_NONE)
    
    while True:
        
        RedLed.value(Button.value())
        

main()