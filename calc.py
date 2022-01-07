from sympy import *

x, y, z = symbols('x y z')

a1 = 6.33*x+5*(2.96*6.33)/2
a2 = 6.33*y+3*(2.96*6.33)/2
a3 = 6.33*z+1*(2.96*6.33)/2
a4 = 6.33*(17.73-x)+6.33*(17.73-y)+6.33*(17.73-z)
at = (17.73*3*6.33)+9*(2.96*6.33)/2

answer = solve([Eq(a1, a2), Eq(a1, a3), Eq(a1, a4), Eq(a1+a2+a3+a4,at)], [x, y, z])
print(answer)
print('a1=', a1.evalf(subs=answer))
print('a2=', a2.evalf(subs=answer))
print('a3=', a3.evalf(subs=answer))
print('a4=', a4.evalf(subs=answer))
print('at=', at)
print('x=', x.evalf(subs=answer))
print('y=', y.evalf(subs=answer))
print('z=', z.evalf(subs=answer))
