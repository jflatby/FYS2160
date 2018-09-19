import numpy as np
import matplotlib.pyplot as plt
plt.style.use("ggplot")

k = 1.3e-23

def entropy(N, S):
    return k * (N * np.log(2) - S**2/(2*N))


M = 10 ** 4
N = 60


def random_int():
    """Returns -1 or 1 randomly"""
    return 1 if np.random.random() < 0.5 else -1

net_spins = np.zeros(121)
for i in range(M):
    net_spins[np.sum([random_int() for i in range(N)]) + 60] += 1

print(net_spins)

x = np.arange(-N, N+1)
plt.plot(x, entropy(x, net_spins))
plt.savefig("oblig1_27.png")
plt.show()