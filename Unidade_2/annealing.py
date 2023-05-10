from math import exp
from random import uniform

def goal(x):
	return x*x*(x-1)*(x-2)*(x-3)*(x-4)


class State:
    def __init__(self, x):
        self.x = x
        self.f = goal(x)


def succ(s):
    x1 = s.x + uniform(-1.0, 1.0)
    return State(x1)


def initialState():
    return State(uniform(-10, 10))


current = initialState()
T = 1000.0

while True:
    T = 0.999*T

    if (T < 0.01):
        break

    neighboor = succ(current)

    delta = current.f - neighboor.f

    if(delta > 0):
        current = neighboor
    elif(uniform(0.0, 1) < exp(delta/T)):
        current = neighboor

print('x = ', current.x, 'f = ', current.f)
