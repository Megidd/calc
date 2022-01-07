from sympy import *

w1, w2, w3, h2, h3 = symbols('w1 w2 w3 h2 h3')

a1 = 17.73*w1+(w1*w1*8.89/19)/2
a2 = h2*w2+(w2*w2*8.89/19)/2
a3 = h3*w3+(w3*w3*8.89/19)/2
a4 = w2*(17.73+w1*8.89/19-h2)+w3*(17.73+w1*8.89/19+w2*8.89/19-h3)
at = (17.73*19)+(8.89*19)/2

answer = solve([Eq(a1,a2), Eq(a1,a3), Eq(a1,a4), Eq(a1+a2+a3+a4,at), Eq(w1+w2+w3,19)], [w1, w2, w3, h2, h3])
print(answer)
print('a1=', a1.evalf(subs=answer))
print('a2=', a2.evalf(subs=answer))
print('a3=', a3.evalf(subs=answer))
print('a4=', a4.evalf(subs=answer))
print('at=', at)
