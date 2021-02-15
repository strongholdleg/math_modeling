import numpy as np	
from scipy.integrate import odeint	
import matplotlib.pyplot as plt
x = np.arange(-5, 5, 0.3)
def diff_function(g, t):
    x,y = g
    dx_dt = 3*x-2*y+(e**(3*t))/(e**t)+1
    dy_dt = x- (e**(3*t))/(e**t)+1
    return dx_dt, dy_dt
y0=-7
x0=5
e = 2.718
g0 =x0, y0
sol = odeint(diff_function, g0, t)
plt.plot(t, sol[:, 1], 'g', label='y')
plt.legend()
plt.show()











































