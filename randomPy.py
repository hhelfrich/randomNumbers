import random
import numpy as np 
import math
import matplotlib.pyplot as plt

def gaussian(x, mu, sigma):
    return ((1.0/np.sqrt(2.0*math.pi)*sigma)*np.exp(-(x - mu)**2/(2.0*sigma**2)))

print(random.random()) #prints a single random number b/t 0 and 1
print(random.uniform(1.0,6.0)) #single random b/t 1 and 6
print(random.randint(1,6)) #single integer btwn 1 and 6
print(random.gauss(0.0, 1.0)) #single guassian number

print(np.random.random(10))
print(np.random.uniform(1.0, 6.0, 10)) # 10 numbers btwn 1 and 6
print(np.random.randint(1,6,10))
print(np.random.normal(0, 1.0 , 10))

x_0 = np.linspace(-4.0,4.0,10000)
y_0 = gaussian(x_0,0.0,1.0)
x = np.random.normal(0.0, 1.0, 10000)

plt.hist(x,bins='fd',density =True)
plt.plot(x_0, y_0)
plt.show()