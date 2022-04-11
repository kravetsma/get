import RPi.GPIO as gpd
import time


def decimal2binary(value): 
    return [int(bit) for bit in bin(value)[2:].zfill(8)]


def analogVoltage(num):
    global dac
    for i,val in enumerate(decimal2binary(num)):
                    gpd.output(dac[i],val)


def adc()->float:
    global dac,comp
    left,right =0,255
    for _ in range(8):
        volt = left + (right-left)//2
        analogVoltage(volt)
        time.sleep(0.07)
        if not gpd.input(comp):
            right = volt
        else:
            left = volt
    print("voltage meaning ",left + (right-left)//2, decimal2binary(left + (right-left)//2))
    return    3.3*(left + (right-left)//2)/255


gpd.setmode(gpd.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17

gpd.setup(comp, gpd.IN)
gpd.setup(dac, gpd.OUT)
gpd.setup(troyka, gpd.OUT, initial=1)

try:
    while __name__ == '__main__':
        print(adc())
finally:
    gpd.output(dac,0)
    gpd.cleanup()