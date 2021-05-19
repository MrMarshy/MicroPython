import pyb

from array import array
from math import pi, sin

ChangeFreq = 8192*1000
"""
    https://docs.micropython.org/en/latest/library/pyb.DAC.html
    
    DAC output from pin PA4, D24 morpho.
    
    DAC frequency is set to ChangeFreq/8192 for 12 bits Hence, freq of triangle signal is
    1kHz
"""
def main():
    
    dac1 = pyb.DAC(1, bits=12, buffering = True)
    
    dac1.triangle(ChangeFreq)
    
main()


