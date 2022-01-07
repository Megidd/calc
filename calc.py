from sympy import *

w1, w2, w3, h2, h3 = symbols('w1 w2 w3 h2 h3')

tan = 8.89/19
h1 = 17.73
wt = 19

a1 = h1*w1
a2 = h2*w2
a3 = h3*w3
a4 = w2*(h1-h2)+w3*(h1-h3)
at = (h1*wt)

eq1 = a1 - at/4
eq2 = a2 - at/4
eq3 = a3 - at/4
eq4 = a4 - at/4
eq5 = w1+w2+w3-wt

eq1 = nsimplify(eq1, rational=1)
eq2 = nsimplify(eq2, rational=1)
eq3 = nsimplify(eq3, rational=1)
eq4 = nsimplify(eq4, rational=1)
eq5 = nsimplify(eq5, rational=1)

answer = solve((eq1, eq2, eq3, eq4, eq5), (w1, w2, w3, h2, h3))
print(answer)
w3_ = 7
assume_w3 = {w1: 19/4, w2: 57/4 - w3_, w3: w3_, h2: -33687/(400*w3_ - 5700), h3: 33687/(400*w3_)}
print('a1=', a1.evalf(subs=assume_w3))
print('a2=', a2.evalf(subs=assume_w3))
print('a3=', a3.evalf(subs=assume_w3))
print('a4=', a4.evalf(subs=assume_w3))
print('at=', at)
print('w1=', w1.evalf(subs=assume_w3))
print('w2=', w2.evalf(subs=assume_w3))
print('w3=', w3.evalf(subs=assume_w3))
print('h2=', h2.evalf(subs=assume_w3))
print('h3=', h3.evalf(subs=assume_w3))