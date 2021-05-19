import pyb

from array import array
from math import pi, sin

"""
    DAC output from pin PA4, D24 morpho using DMA.
    DAC frequency is set to 8Hz using Timer2. Hence, freq of sinusoid signal is
    8/128 Hz.
"""

CONV_FACTOR = 4095/3.3

def voltToRaw(voltage):
    value = int(voltage * CONV_FACTOR)
    return value

def main():
    # the 'f' is to indicate the data is floating point
    sine_voltages = array('f', 1.65 + 1.65 * sin(2*pi*i/128) for i in range(128))
    
    # the 'H' is to indicate the data is to be unsigned half-words
    DAC_vals = array('H', (0 for i in range(128)))
    
    for i in range(len(DAC_vals)):
        DAC_vals[i] = voltToRaw(sine_voltages[i])
    
    dac1 = pyb.DAC(1, bits=12, buffering = True)
    
    dac1.write_timed(DAC_vals, pyb.Timer(2, freq=8), mode=dac1.CIRCULAR)
    
main()