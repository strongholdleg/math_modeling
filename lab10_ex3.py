import numpy as np	
from scipy.integrate import odeint	
import matplotlib.pyplot as plt
x = np.arange(-5, 5, 0.3)
def diff_function(func, t):
    y,g=func
    dy_dt=g
    dg_dt=np.sin(t)+np.cos(t)
    return dy_dt,dg_dt
y0=4
dy0_dt=-1
k0=y0,dy0_dt
sol = odeint(diff_function, k0, t)
plt.plot(t, sol[:, 1], 'g', label='y')
plt.legend()
plt.show()


















































