# when <--usb
# orange, yellow
# grey, purple

# built-in libraries
import time
import machine

# user-made libraries
from Motor import *

#--------------------------------------#
LED = machine.Pin(2, machine.Pin.OUT);
LED.on();

motPins = ((25, 26, 27), (5, 18, 17));

m1 = Motor(motPins[0]);
m2 = Motor(motPins[1]);

for i in range(3):
    LED.on();
    time.sleep(250/1000);
    LED.off();
    time.sleep(250/1000);