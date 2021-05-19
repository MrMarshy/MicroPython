import pyb
"""
    Getting analog value from pin PA3 using polling.
"""

LD1 = pyb.LED(1)

def rawToVolts(value):
    voltage = 3.3 * value / 4095
    return voltage


def main():

   adc = pyb.ADC(pyb.Pin.cpu.A3) # PA3 is A0 on the morpho connector 
   
   while True:
       adc_val = adc.read()
       adc_volts = rawToVolts(adc_val)
       print("ADC voltage is %6.4f" % (adc_volts))
       
       if adc_volts > 1.5:
           LD1.on()
       else:
           LD1.off()
           
       pyb.delay(500) # 2Hz
main()