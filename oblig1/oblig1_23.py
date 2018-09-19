import numpy as np
import matplotlib.pyplot as plt
plt.style.use("ggplot")

M = 10**4
N = 60

def random_int():
    """Returns -1 or 1 randomly"""
    return 1 if np.random.random() < 0.5 else -1

net_spins = np.zeros(M)
for i in range(M):
    net_spins[i] = np.sum([random_int() for i in range(N)])

x = np.arange(-N, N+1)
plt.hist(net_spins, x)
plt.savefig("oblig1_23.png")


plt.show()


