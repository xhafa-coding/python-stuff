import numpy as np
import matplotlib.pyplot as plt
import random


mu = 0
stdev = 1
pi = 3.141592
step_size = 0.01

normalvalues = []

steps = np.arange(-5, 5.1, step_size)
sqrtpi = np.sqrt(2*pi)


for x in steps:
    gauss = (1/(stdev*sqrtpi))*np.exp(-(x-mu)**2/(2*(stdev**2)))
    normalvalues.append(gauss)


plt.plot(steps, normalvalues, color='darkblue')
plt.fill_between(steps, normalvalues, color='darkblue')
plt.title("A Normal Distribution")
plt.xlabel("Observation")
plt.ylabel("Probability Density")
plt.show()