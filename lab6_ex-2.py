import matplotlib.pyplot as plt
import numpy as np
def parabola_plotter(a =1, b = 1,  c = 0, title = 'График'): 
    x = np.arange(-10,10,0.01)
    y = a*(x**2) + b*x + c
    plt.plot(x, y )
    #plt.xlabel('ось x')
    #plt.ylabel('ось y')
    #plt.title(title)
    plt.show()
parabola_plotter()


def giperbola_plotter(d = 1, title='гипербола'):
    x_min=-20
    x_max=20
    x = np.arange(x_min, x_max, 0.01)
    y = d/x
    y = np.ma.masked_less(y, x_min)
    y = np.ma.masked_greater(y, x_max)
    plt.plot(x,y)
    plt.show()
giperbola_plotter()





