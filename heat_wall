import numpy as np
import matplotlib.pyplot as plt
wall_th = 0.1
n = 10
T0 = 0
T1s = 40
T2s = 20
dx = wall_th/n

alpha = 0.0001
t_final = 40
dt = 0.5

x = np.linspace(dx/2, wall_th-dx/2, n)

T = np.ones(n)*T0
dTdt = np.empty(n)

t = np.arange(0, t_final, dt)

for j in range(1, len(t)):
    plt.clf()
    for i in range(1, n-1):
        dTdt[i] = alpha*(-(T[i]-T[i-1])/dx**2 + (T[i+1]-T[i])/dx**2)
    dTdt[0] = alpha*(-(T[0]-T1s)/dx**2 + (T[1]-T[0])/dx**2)
    dTdt[n-1] = alpha*(-(T[n-1]-T[n-2])/dx**2 + (T2s-T[n-1])/dx**2)
    T = T + dTdt * dt
    plt.figure(1)
    plt.plot(x,T)
    plt.axis([0,wall_th,-5,45])
    plt.xlabel("distance")
    plt.ylabel("Temperature")
    plt.show()
    plt.pause(0.05)
