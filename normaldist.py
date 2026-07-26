import numpy as np
import random
import matplotlib.pyplot as plt

size = 300000
values = []
frequency_plot = {}
x_coor = []
y_coor = []


for n in range(size):
    sample = np.random.normal(0,1)
    rounded = round(sample, 3)
    values.append(rounded)


for value in values:
    if value not in frequency_plot:
        frequency_plot[value] = 1
    else:
        frequency_plot[value] = frequency_plot[value] + 1
        
for item in frequency_plot.keys():
    y_coor.append(item)

for values in frequency_plot.values():
    x_coor.append(values)

paired_data = list(zip(y_coor, x_coor))
sorted_paired_data = sorted(paired_data, key=lambda item: item[1])

x_values, y_counts = zip(*sorted_paired_data)
x_array = np.array(x_values)
y_array = np.array(y_counts)

plt.bar(x_array, y_array, color='darkblue')
plt.title("A Normal Distribution")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

