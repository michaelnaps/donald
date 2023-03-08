# when <--usb
# orange, yellow
# grey, purple

# built-in libraries
import time
import machine

# user-made libraries
from Motor import *

# global variable section
LED = machine.Pin(2, machine.Pin.OUT);
LED.on();

motPins = ((25, 26, 27), (5, 18, 17));

m1 = Motor(motPins[0]);
m2 = Motor(motPins[1]);

# blink twice if successful
for i in range(2):
    LED.on();
    time.sleep(250/1000);
    LED.off();
    time.sleep(250/1000);