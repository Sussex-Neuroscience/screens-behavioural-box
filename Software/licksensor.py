from machine import TouchPad,Pin
import time

threshhold = 150 #adjust according to the animal conductivity
pin = TouchPad(15)

while True:
     touch = pin.read()
     #check pin output signal for threshold ajustment
     #print(touch) 
     #time.sleep_ms(500)
     if touch <threshhold:
         print("touch detected")
         time.sleep_ms(500)