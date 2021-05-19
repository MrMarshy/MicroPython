import pyb
"""
    Toggling the onboard red LED using the Timer2 interrupt.
    Controlling brightness of the onboard LED using PWM.
"""

LD3 = pyb.LED(3)
duty_cycle = 0
Timer3 = pyb.Timer(3, freq=1000, mode=pyb.Timer.UP)
Timer3_PWM = Timer3.channel(3, mode=pyb.Timer.PWM, pin=pyb.Pin.cpu.B0, pulse_width_percent=0)

def toggle_LD3(timer):
    LD3.toggle()

def increase_duty_cycle(pin):
    global duty_cycle
    global Timer2_PWM
    
    duty_cycle = duty_cycle + 10
    if duty_cycle > 100:
        duty_cycle = 0
    print(duty_cycle)
    
    Timer3_PWM.pulse_width_percent(duty_cycle)
    

def main():

    Timer2 = pyb.Timer(2, freq=0.5, mode=pyb.Timer.UP)
    Timer2.callback(toggle_LD3)

    pyb.ExtInt(pyb.Pin.cpu.C13, mode=pyb.ExtInt.IRQ_RISING, pull=pyb.Pin.PULL_NONE, callback=increase_duty_cycle)
    
        
main()