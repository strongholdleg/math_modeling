import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
t = np.linspace (1, 10, 100)
def kus (m, t):
    dmdt =  - k * m*t 
    return dmdt
m_0 = 1000
k = 0.08
solve_Bi = odeint( kus, m_0, t)
plt.plot(t, solve_Bi[:,0], label='Ра')
plt.xlabel('Пы')
plt.ylabel(' а')
plt.title('t')
plt.legend()

plt.show()



























