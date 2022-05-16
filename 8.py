import numpy as np
import matplotlib.pyplot as plt


fig, axis = plt.subplots()
axis.grid()
axis.set_title("Процесс заряда и разряда конденсатора в RC-цепочке")

with open('/home/b04-106/get/data1.txt', 'r') as f:
    data = f.readlines()

data = list(map(lambda x: float(x) / 256 * 3.3, data))
time = [0.011 * i for i in range(len(data))]

max_y = 3.5000001
min_y = 0

min_x = 0
max_x = 10.0001

axis.plot(time, data, color='brown', label='V(t)', zorder=1)
axis.legend()
plt.xlabel("Время, c")
plt.ylabel("Напряжение, В")
axis.set_xlim(min_x, max_x)
axis.set_ylim(min_y, max_y)

new_data = data[::len(data)//30]
new_time = time[::len(data)//30]
new_data.append(max(data))
charge_time = round(time[data.index(max(data))], 2)
new_time.append(charge_time)
new_data.append(data[-1])
new_time.append(time[-1])
axis.scatter(new_time, new_data, color='red', s=7, zorder=2)

charge_time = round(time[data.index(max(data))], 2)
decharge_time = round(time[-1] - charge_time, 2)
plt.text(6, 2.5, "Время зарядa: {} c".format(charge_time))
plt.text(6, 2, "Время разрядa: {} c".format(decharge_time))

major_ticks = np.arange(min_x, max_x, 1)
minor_ticks = np.arange(min_x, max_x, 0.25)
major_ticks1 = np.arange(min_y, max_y, 0.5)
minor_ticks1 = np.arange(min_y, max_y, 0.05)

axis.set_xticks(major_ticks)
axis.set_xticks(minor_ticks, minor=True)
axis.set_yticks(major_ticks1)
axis.set_yticks(minor_ticks1, minor=True)

axis.grid(which='both',  linestyle=":")
axis.grid(which='minor', alpha=1)
axis.grid(which='major', alpha=1)

fig.show()
fig.savefig('./graph.svg', dpi=1000)
plt.show()