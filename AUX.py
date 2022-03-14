import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

aux = [22, 23, 27, 18, 15, 14, 3, 2]
GPIO.setup(aux, GPIO.IN)

leds = [21, 20, 16, 12, 7, 8, 25, 24]
GPIO.setup(leds, GPIO.OUT)

while True:
    for j in range(len(aux)):
        GPIO.output(leds[j], GPIO.input(aux[j]))
