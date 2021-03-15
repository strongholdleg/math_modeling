import numpy as np	
from scipy.integrate import odeint	
import matplotlib.pyplot as plt	
from matplotlib.animation import FuncAnimation
t = np.linspace(0, 5, frames)
def move_func(g, t):
    x, y = g
    dxdt = k*(z-(x+y)) 
    dydt = k2*(z-(x+y))
    return dxdt , dydt
z = 90
k = 5
k2 = 15
g = 0,0
sol = odeint(move_func, g, t)
plt.plot(t,sol, '-', color= 'b')
plt.show()













































