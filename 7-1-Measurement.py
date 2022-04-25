import RPi.GPIO as gpio
import matplotlib.pyplot as plt
import time


def dec2bin(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def num2dac(value):
    signal = dec2bin(value)
    gpio.output(dac, signal)
    return signal

def getnum(arr):
    num = 0
    for i, elem in enumerate(arr):
        num += elem * (2 ** (7 - i))
    return num

def adc():
    arr = [0] * 8
    num = 0
    for i in range(8):
        arr[i] = 1
        num = getnum(arr)
        if i == 8:
            return None
        num2dac(num)
        time.sleep(0.01)
        comp_value = gpio.input(comp)

        if comp_value == 0:
            arr[i] = 0
    return num


data = []
leds = [21, 20, 16, 12, 7, 8, 25, 24]
dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troy = 17

gpio.setmode(gpio.BCM)
gpio.setup(leds, gpio.OUT)
gpio.setup(dac, gpio.OUT)
gpio.setup(troy, gpio.OUT, initial=1)
gpio.setup(comp, gpio.IN)

starting_time = time.time()

try:
    while __name__ == '__main__':
        gpio.output(troy, 1)
        current = adc()
        time.sleep(0.1)
        gpio.output(leds, dec2bin(current))
        num = current / 256 * 3.3
        print(num)
        data.append(num)
        if num > 2.5:
            break
    
    gpio.output(troy, 0)
    while __name__ == '__main__':
        current = adc()
        time.sleep(0.001)
        gpio.output(leds, dec2bin(current))
        num = current / 256 * 3.3
        data.append(num)
        if num < 0.5:
            break
    
    stop_time = time.time()
    print("Total time: ", stop_time - starting_time)
    print("Frequency: ", 1)
    print("Steps: ", 8)
    plt.plot(data)
    plt.show()

    data = list(map(str, data))
    with open("./data.txt", 'w') as file:
        file.write("\n".join(data))

finally:
    gpio.output(leds, 0)
    gpio.output(troy, 0)
    gpio.cleanup()