import numpy as np
import matplotlib.pyplot as plt

def get_pi(N):
    x = np.random.random(N)
    y = np.random.random(N)
    r = np.sqrt(x*x + y*y)
    N_in = len(r[np.where(r <= 1)])
    return (N_in/N)*4.0

N = 10000
N_trials = 10000
pis = np.zeros(N_trials)
for i in range(0,N_trials):
    pis[i] = get_pi(N)

print(pis.mean(), "+/-", pis.std())
plt.hist(pis, bins='fd', density=True)
plt.show()

#use guassian mu (mean) and sigma (std dev) to get evenly spaced