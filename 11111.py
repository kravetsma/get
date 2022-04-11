import RPi.GPIO as gp
import time

gp.setmode(gp.BCM)
dac = [26, 19,13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17
MVolt = 3.3
bit = 8
level = 2 ** bit
volt = 0

gp.setup(dac, gp.OUT)
gp.setup(troyka, gp.OUT, initial = 1)
gp.setup(comp, gp.IN)

def d2b(v):
    return [int(bit) for bit in bin(v)[2:].zfill(8)]
def adc():
    for i in range(level):
        s = d2b(i)
        gp.output(dac,s)
        time.sleep(0.0005)
        cV = gp.input(comp)
        if cV == 0:
            print("ADC value", i, s)
            return i
flag = True
try:
    while flag:
        voltage =  adc() / level * MVolt
        print("voltage meaning ", voltage)
except KeyBoardInterrupt:
    print("Emergency stop")
finally:
    gp.output(dac, 0)
    gp.output(troyka, 0)
    gp.cleanup()