import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
number = [0] * len(dac)
GPIO.setup(dac, GPIO.OUT)

x = bin(int(input()))
k = len(x) - 2
nums = [0] * 8
for i in range(k):
    nums[len(dac) - 1 - i] = int(x[k + 1 - i])

GPIO.output(dac, nums)

time.sleep(12)

GPIO.output(dac, 0)
GPIO.cleanup()
