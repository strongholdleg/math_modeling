import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
t = np.linspace (0, 10, 100)
def laminat (m, t):
    dmdt =  k * m
    return dmdt
m_0 = 10
k = 3
solve_Bi = odeint(laminat, m_0, t)
plt.plot(t, solve_Bi[:,0], label='Ра')
plt.xlabel('Пы')
plt.ylabel(' а')
plt.title('t')
plt.legend()

plt.show()

















































