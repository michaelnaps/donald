import time
import machine

class Motor:
    def __init__(self, pList):
        self.in1 = machine.Pin(pList[0], machine.Pin.OUT);
        self.in2 = machine.Pin(pList[1], machine.Pin.OUT);
        self.en  = machine.Pin(pList[2], machine.Pin.OUT);

        self.in1.value(1);
        self.in2.value(0);
        self.en.value(0);
    
    def dirSwitch(self):
        val1 = self.in1.value();
        val2 = self.in2.value();

        self.in1.value(val2);
        self.in2.value(val1);

        return val1, val2;

#--------------------------------------#
LED = machine.Pin(2, machine.Pin.OUT);
LED.on();

motPins = ((25, 26, 27), (5, 18, 17));

m1 = Motor(motPins[0]);
m2 = Motor(motPins[1]);

for i in range(3):
    LED.on();
    time.sleep(500/1000);
    LED.off();
    time.sleep(500/1000);