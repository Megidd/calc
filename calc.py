from sympy import *

w1, w2, w3, h2, h3 = symbols('w1 w2 w3 h2 h3')

tan = 8.89/19
h1 = 17.73
wt = 19

a1 = h1*w1+(w1*w1*tan)/2
a2 = h2*w2+(w2*w2*tan)/2
a3 = h3*w3+(w3*w3*tan)/2
a4 = w2*(h1+w1*tan-h2)+w3*(h1+(w1+w2)*tan-h3)
at = (h1*wt)+(wt*wt*tan)/2

eq1 = a1 - a2
eq2 = a1 - a3
eq3 = a1 - a4
eq4 = a1+a2+a3+a4-at
eq5 = w1+w2+w3-wt

eq1 = nsimplify(eq1, rational=1)
eq2 = nsimplify(eq2, rational=1)
eq3 = nsimplify(eq3, rational=1)
eq4 = nsimplify(eq4, rational=1)
eq5 = nsimplify(eq5, rational=1)

answer = nsolve((eq1, eq2, eq3, eq4, eq5), (w1, w2, w3, h2, h3), (6, 7, 8, 9, 10))
print(answer)
print('a1=', a1.evalf(subs=answer))
print('a2=', a2.evalf(subs=answer))
print('a3=', a3.evalf(subs=answer))
print('a4=', a4.evalf(subs=answer))
print('at=', at)
