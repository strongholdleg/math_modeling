import numpy as np	
from scipy.integrate import odeint	
import matplotlib.pyplot as plt
x = np.arange(-5, 5, 0.3)
def diff_function(g, x):
    y,z = g
    dy_dx = y**2*z
    dz_dx = z/x-y*z**2
    return dy_dx, dz_dx
y0=1
z0= - 3
g0 = y0, z0
sol = odeint(diff_function, g0, x)
plt.plot(t, sol[:, 1], 'g', label='y')
plt.legend()
plt_show()















