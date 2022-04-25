import RPi.GPIO as GPIO
import time

import matplotlib.pyplot as plt

def decimal2ninary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]
led = [21, 20, 16, 12, 7 , 8, 25, 24]
dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17
Max = 3.3
level = 2**(len(dac))

GPIO.setmode(GPIO.BCM)

for i in range(len(dac)):
    GPIO.setup(dac[i], GPIO.OUT, initial = GPIO.LOW)

for i in range(len(dac)):
    GPIO.setup(led[i], GPIO.OUT, initial = GPIO.LOW)

GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def num2dac(value):
    signal = decimal2ninary(value)
    GPIO.output(dac, signal)
    return signal

try:
    while True:
        kol = 0
        start = time.time()
        s = 0
        GPIO.output(17,1)
        clock = []
        volt = []
        while s < 256*0.97:    # заряжка кондея 
            value = [0] * 8
            cur_time = time.time()
            for i in range(8):
                
                value[i] = 1
                s=''
                for j in value:
                    s+=str(j)
                s = int(s, base = 2)
                signal  = num2dac(s)
                voltage = s/(level) * Max
                comparator = GPIO.input(comp)
                if comparator <= 0:
                    value[i] = 0

            light = decimal2ninary(s) # вывод на leds
            for i in range(len(led)-1, -1, -1):
                GPIO.output(led[i],0)
            if 0<s and s<= 32:
                GPIO.output(led[7],1)
            elif 32<s and s<=64:
                for i in range(len(led)-1,5,-1):
                    GPIO.output(led[i],1)
            elif 64<s and s<=96:
                for i in range(len(led)-1,4,-1):
                    GPIO.output(led[i],1)
            elif 96<s and s<=128:
                for i in range(len(led)-1,3,-1):
                    GPIO.output(led[i],1)
            elif 128<s and s<=160:
                for i in range(len(led)-1,2,-1):
                    GPIO.output(led[i],1)
            elif 160<s and s<=192:
                for i in range(len(led)-1,1,-1):
                    GPIO.output(led[i],1)
            elif 192<s and s<=224:
                for i in range(len(led)-1,0,-1):
                    GPIO.output(led[i],1)
            elif 224<s and s<=256:
                for i in range(len(led)-1,-1,-1):
                    GPIO.output(led[i],1)
            
            
            volt.append(voltage)
            cur_time_late = time.time()
            kol+=1
            clock.append(cur_time_late - cur_time)
            print('ADC value = {:^3} - {}, input voltage = {:.2f}'.format(s,signal,voltage))


            
        GPIO.output(17,0)
        while s > 256*0.03: # Разрядка кондея
            value = [0] * 8
            cur_time = time.time()
            for i in range(8):
                value[i] = 1
                s=''
                for j in value:
                    s+=str(j)
                s = int(s, base = 2)
                signal  = num2dac(s)
                voltage = s/(level) * Max
                comparator = GPIO.input(comp)
                if comparator <= 0:
                    value[i] = 0


            light = decimal2ninary(s) # вывод на leds
            for i in range(len(led)-1, -1, -1):
                GPIO.output(led[i],0)
            if 0<s and s<= 32:
                GPIO.output(led[7],1)
            elif 32<s and s<=64:
                for i in range(len(led)-1,5,-1):
                    GPIO.output(led[i],1)
            elif 64<s and s<=96:
                for i in range(len(led)-1,4,-1):
                    GPIO.output(led[i],1)
            elif 96<s and s<=128:
                for i in range(len(led)-1,3,-1):
                    GPIO.output(led[i],1)
            elif 128<s and s<=160:
                for i in range(len(led)-1,2,-1):
                    GPIO.output(led[i],1)
            elif 160<s and s<=192:
                for i in range(len(led)-1,1,-1):
                    GPIO.output(led[i],1)
            elif 192<s and s<=224:
                for i in range(len(led)-1,0,-1):
                    GPIO.output(led[i],1)
            elif 224<s and s<=256:
                for i in range(len(led)-1,-1,-1):
                    GPIO.output(led[i],1)

            volt.append(voltage)
            kol+=1
            cur_time_late = time.time()
            clock.append(cur_time_late - cur_time)
            print('ADC value = {:^3} - {}, input voltage = {:.2f}'.format(s,signal,voltage))
        finish = time.time()
        break


    with open('data.txt', 'w') as outfile:
        plt.plot(clock, volt)
        plt.xlabel('t, с')
        plt.ylabel('U, В')
        plt.title('Зависимость напряжения на обкладках конденсатора U от времени t')
        plt.show()
        
        str_voltage = [str(u) for u in volt]
        out = '\n'.join(str_voltage)
        outfile.write(out)
    
    with open('settings.txt', 'w') as outfile:
        total_time = finish - start # итоговое время 
        T = total_time/kol # период одного измерения
        freq = kol / total_time # частотка дискритизации 
        quant = 3.3/256 # шаг квантования
        print('Общая продолжительность эксперемента {:.2f}, Период одного измерения - {:.5f}, средняя частота дискритизации - {:.5f}, Шаг квантования - {:.4f}'.format(total_time, T, freq, quant))
        data = '\n'.join(str(total_time))
        data = '\n'.join(str(T))
        data = '\n'.join(str(freq))
        data = '\n'.join(str(quant))
        outfile.write(data)
        

finally:
    for i in dac:
        GPIO.output(i,0)
    for i in led:
        GPIO.output(i,0)
    GPIO.output(17, 0)
    GPIO.cleanup() 