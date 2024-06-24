import numpy as np
import matplotlib.pyplot as plt
# import matplotlib as mpl

C = 0.001   # Farads
L = 0.001   # Henry's
R = 2      # Resistance in Ohms


def Q(x):
    return np.sqrt(L/C)/R


def sin(x):
    return 5 * np.sin(x)


def Xc(f):
    return 1/(2*np.pi*f*C)


def Xl(f):
    return 2*np.pi*f*L


def Fres():
    return 1/(2*np.pi*np.sqrt(L*C))


def Zs(f):
    return np.sqrt(R**2 + (Xl(f)-Xc(f))**2)


def Zp(f):
    return 1/(np.sqrt(1/(R**2) + (1/Xl(f)-1/Xc(f))**2))


x = np.linspace(10, 1000, 1000)
y = sin(x)
q = Q(x)

fig, ax = plt.subplots()

# ax.plot(x, y, label='Sin(x)')
# plt.axhline(y=q, color='r', linestyle='-', label='Q Factor')
plt.axvline(x=Fres(), color='r', linestyle='-', label='Resonant Frequency')
ax.plot(x, Xc(x), label='Xc(f)')
ax.plot(x, Xl(x), label='Xl(f)')
ax.plot(x, Zp(x), label='Zp(f)')
ax.plot(x, Zs(x), label='Zs(f)')
ax.set_title('Plotting Functions in Matplotlib', size=14)
ax.set_xscale("log")
# ax.set_xlim(0, 4 * np.pi)
# ax.set_ylim(-5, 5)

# Despine the graph
plt.legend()
plt.show()
