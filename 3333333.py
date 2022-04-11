import RPi.GPIO as gpio
import time

def dec2bin(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def num2dac(value):
    signal = dec2bin(value)
    time.sleep(0.02 )
    gpio.output(dac, signal)
    return signal

dac     = [26, 19, 13,  6,  5, 11, 9, 10]
leds    = [21, 20, 16, 12, 7, 8, 25, 24]


comp    = 4
troyka  = 17
bits    = len(dac)
levels  = 2**bits
maxVoltage = 3.3


gpio.setmode(gpio.BCM)
gpio.setup(dac, gpio.OUT)
gpio.setup(troyka, gpio.OUT, initial = gpio.HIGH)

gpio.setup(comp,  gpio.IN)
gpio.setup(leds, gpio.OUT)

outp = [0, 0, 0, 0, 0, 0, 0, 0]
tmpp = [0, 0, 0, 0, 0, 0, 0, 0]

try:
    while True:
        for value in range(256):
            time.sleep(0.001)
            signal = num2dac(value)
            voltage = value / levels * maxVoltage
            compValue = gpio.input(comp)
            if compValue == 0:
                for j in range(8):
                    if value > 2**j:
                        tmpp[j] = 1
                    else: tmpp[j] = 0
                outp = tmpp
                print(voltage)
                break
        gpio.output(leds, outp)
finally:
    gpio.output(dac, gpio.LOW)
    gpio.cleanup()