import pyb
from micropython import const

"""
    Getting DAC output from pin PA4, D24 morpho using polling.
"""

CONV_FACTOR = 4095/3.3

def voltToRaw(voltage):
    value = int(voltage * CONV_FACTOR)
    return value

def main():
    DAC_voltage = 0
    # DAC1 is PA4, D24 morpho connector
    dac1 = pyb.DAC(1, bits = 12, buffering = True)
    
    while True:
        result = voltToRaw(DAC_Voltage)
        dac1.write(result)
        DAC_voltage = DAC_voltage + 0.01
        print("DAC Voltage: %6.4f" % (DAC_voltage))
        if DAC_voltage > 3.3:
            DAC_voltage = 0
            
        pyb.delay(10)
        
main()