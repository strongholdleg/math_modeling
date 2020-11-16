import math
print(math.sqrt(3))

import sympy
print(sympy.sqrt(3))
print(2 * sympy.sqrt(3))

from sympy import symbols
x, y = symbols('x y')
expr = x + 2*y
print(expr)
print(expr+1)
print(x * expr)

from sympy import sin, cos, pi, exp
print(sin(x**2)- exp(-2*x) + cos(pi/x))

from sympy import symbols
from sympy import sin, cos, pi, exp
x , y , z = symbols('x y z')
expr = sin(x**2)-exp(-2*x)+cos(pi/x)
expr_new = expr.subs(x,y)
print(expr_new)

expr_new = expr.subs(x, x**2)
print(expr_new)

from sympy import symbols
from sympy import sin, cos
from sympy import simplify, expand, factor, trigsimp

x, y, z = symbols('x y z')

simp_expr = simplify(sin(x)**2 + cos(x)**2)
print(simp_expr)

simp_expr = expand((x+1)*(x-2)-(x-1)*x)
print(simp_expr)

simp_expr = factor(x**3 - x**2 + x-1)
print(simp_expr)

simp_expr = factor(simp_expr)
print(simp_expr)

from sympy import symbols
from sympy import sin, cos, pi, exp
from sympy import Eq, solve, solveset, linsolve, nonlinsolve

x, y, z = symbols('x y z')

expr = x**2 - 2
solve_expr = solve(expr, x)
print(solve_expr)

expr = Eq(x,y)
print(expr)

expr = Eq(3, 1)
print(expr)

solve_expr = solveset(x**2 - 2, x)
print(solve_expr)

expr = sin(x**2)-exp(-2*x)+cos(pi/x)
solve_expr = solveset(expr,x)
print(solve_expr)

system = [x**2+1, y**2+1]
solve_system = nonlinsolve(system,[x,y])
print(solve_system)

system = [x**2 - 2*y**2-2, x*y-2]
solve_system = nonlinsolve(system,[x,y])
print(solve_system)

from sympy import symbols
from sympy.vector import CoordSys3D
from sympy import sin, cos, trigsimp

N= CoordSys3D('N')
a, b, c =symbols('a b c')

v = N.i - 2*N.j
print(v/3)











































































