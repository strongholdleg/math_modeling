import numpy as np
my_array=np.zeros(shape=(5,6))
for(i,j),x in np.ndenumerate(my_array):
    m=input (f'элемент: строка {i}, столб {j}')
    my_array[i,j]=float(m)
    print(i,j,x,sep=";")
    print(my_array)





