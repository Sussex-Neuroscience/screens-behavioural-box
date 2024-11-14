from machine import TouchPad, Pin, UART
import time


uart = UART(1, 9600)
uart.init(9600, bits=8, parity=None, stop=1)

relay1 = 16
relay_pin1 = Pin(relay1, Pin.OUT)
relay2 = 17
relay_pin2 = Pin(relay2, Pin.OUT)
relay3 = 05
relay_pin3 = Pin(relay3, Pin.OUT)
relay4 = 18
relay_pin4 = Pin(relay4, Pin.OUT)


threshold_value = 250


touch_pin1 = TouchPad(Pin(12, mode=Pin.IN))
touch_pin2 = TouchPad(Pin(13, mode=Pin.IN))
touch_pin3 = TouchPad(Pin(14, mode=Pin.IN))
touch_pin4 = TouchPad(Pin(27, mode=Pin.IN))


while True:
    value = uart.read()
    
    if value == 1:
        Screen1()
    elif value == 2:
        Screen2()
    elif value == 3:
        Screen3()
    
    time.sleep(0.5)


def Screen1(): #OpenSolendoid 1 for (x) second(s)
    pinvalue1 = touch_pin1.read()
    relay_pin1.value(1)
    time.sleep(5)
    relay_pin1.value(0)


def Screen2(): #OpenSolendoid 2 for (x) second(s)
    pinvalue2 = touch_pin2.read()
    relay_pin2.value(1)
    time.sleep(5)
    relay_pin2.value(0)


def Screen3(): #OpenSolendoid 3 for (x) second(s)
    pinvalue3 = touch_pin3.read()
    relay_pin3.value(1)
    time.sleep(5)
    relay_pin3.value(0)

    
    

    
 