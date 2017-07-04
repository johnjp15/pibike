import time
from math import log
from gpiozero import PWMLED
from gpiozero import MCP3008

pot = MCP3008(0)
hall = MCP3008(1)
led = PWMLED(21)

#led.source = pot.values

#led.source = hall.values



while True:
    #print(pot.value)
    brightness = hall.value + ((hall.value - 0.5151) * 5.0)
    if(brightness > 1.0):
        brightness = 1.0
    elif(brightness < 0.0):
        brightness = 0.0
    led.value = brightness
    print(brightness)
    time.sleep(0.01)
###

