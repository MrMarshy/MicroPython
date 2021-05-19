import pyb
import pindefs
from micropython import const
"""
    Getting analog value from pin PA6 using timer interrupt.
    Read the internal temperature 
"""

from array import array
Timer1 = pyb.Timer(1, freq=10, mode=pyb.Timer.UP)
adc = pyb.ADC(pyb.Pin.cpu.A6) # PA6 is D12 on the morpho connector
interrupt_cnt = 0
print_flag = 0
BUFF_SIZE = const(20)
buffer = array('I', (0 for i in range(BUFF_SIZE)))

LD1 = pyb.LED(1)

def rawToVolts(value):
    voltage = 3.3 * value / 4095
    return voltage

def getADC(timer):
    global interrupt_cnt
    global print_flag
    global buffer
    global BUFF_SIZE
    buffer[interrupt_cnt] = adc.read()
    interrupt_cnt = interrupt_cnt + 1
    
    if interrupt_cnt == BUFF_SIZE:
        Timer1.deinit()
        print_flag = 1
        
def main():
    
    global print_flag
    
    total = 0
    
    LD2 = pyb.LED(2)
    
    LD3 = pyb.Pin('PB14', pyb.Pin.OUT_PP)
    LD3.value(1)
    
    Timer1.callback(getADC)
    
    adc_internal_temperature = pyb.ADCAll(12, 0x70000)
    value = adc_internal_temperature.read_core_temp()
    print("Internal temperature: %6.4f" % (value))
    pyb.delay(100)
    
    while True:
        if print_flag == 1:
            for i in range(len(buffer)):
                adc_volt = rawToVolts(buffer[i])
                total = total + adc_volt
                print(adc_volt)
            
            print_flag = 0
            avg = total / BUFF_SIZE
            print("Printing is done! - avg: %6.4f" % (avg))
            
            if avg > 1.5:
                LD2.on()
            else:
                LD2.off()
                
main()