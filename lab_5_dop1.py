from sympy import symbols
from sympy import sqrt
from sympy.vector import CoordSys3D

from sympy import sin, cos, exp
from sympy import simplify, expand, factor, trigsimp

N = CoordSys3D('N')

V1 = 4*N.i+3*N.j+8*N.k
V2 = -2*N.i+8*N.j+7*N.k
V3 = -5*N.i-6*N.j+12*N.k

a1 = V1.magnitude
b1 = V2.magnitude
c1 = V3.magnitude
Q = V1.dot(V2)
W = V1.dot(V3)
E = V2.dot(V3)
cos_V1V2 = W/a1
cos_V1V3 = W/b1
cos_V2V3 = E/c1
print(cos_V1V2)
print(cos_V1V3)
print(cos_V2V3)