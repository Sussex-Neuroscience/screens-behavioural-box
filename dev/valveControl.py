import time
import belay
import keyboard

device = belay.Device("COM3")

valve1Status = False
valve2Status = False
valve3Status = False
valve4Status = False

@device.task
def check_valve_status():
    if valve1Status == True:
        valve1.value(1)
    if valve1Status == False:
        valve1.value(0)

    if valve2Status == True:
        valve2.value(1)
    if valve2Status == False:
        valve2.value(0)

    if valve3Status == True:
        valve3.value(1)
    if valve3Status == False:
        valve3.value(0)

    if valve4Status == True:
        valve4.value(1)
    if valve4Status == False:
        valve4.value(0)

@device.task
def set_value(num, state):
    if num == 1:
        valve1.value(state)
    
    if num == 2:
        valve2.value(state)

    if num == 3:
        valve3.value(state)

    if num == 4:
        valve4.value(state)

@device.setup
def setup():
    global valve1Status
    global valve2Status
    global valve3Status
    global valve4Status

    touchPin1 = 12
    touchPin2 = 13
    touchPin3 = 14
    touchPin4 = 27

    valvePin1 = 5
    valvePin2 = 18
    valvePin3 = 16
    valvePin4 = 17

    touchThreshhold = 270

    from machine import TouchPad, Pin

    pin1 = TouchPad(touchPin1)
    pin2 = TouchPad(touchPin2)
    pin3 = TouchPad(touchPin3)
    pin4 = TouchPad(touchPin4)

    valve1 = Pin(valvePin1, Pin.OUT)
    valve2 = Pin(valvePin2, Pin.OUT)
    valve3 = Pin(valvePin3, Pin.OUT)
    valve4 = Pin(valvePin4, Pin.OUT)

    while True:
        touch1 = pin1.read()
        touch2 = pin2.read()
        touch3 = pin3.read()
        touch4 = pin4.read()

        if touch1 < touchThreshhold:
            valve1Status = True

        else:
            valve1Status = False


        if touch2 < touchThreshhold:
            valve2Status = True
            
        else:
            valve2Status = False


        if touch3 < touchThreshhold:
            valve3Status = True
            
        else:
            valve3Status = False


        if touch4 < touchThreshhold:
            valve4Status = True
            
        else:
            valve4Status = False

        check_valve_status()

setup()