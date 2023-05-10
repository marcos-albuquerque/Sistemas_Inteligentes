'''
Problema da mochila com duas restrições: 
Drescrição: pretende-se colocar um conjunto de itens que tem preço, peso e volume em uma mochila 
que tem um determinado limite de volume e peso de forma a maximizar o preço total dos itens carregados na mochila 
''' 

from random import randint, uniform
import numpy as np
import matplotlib.pyplot as plt

           # weight,volume e price
itemList = [(30, 15,  60),
            (40, 10, 100),
            (80, 20,  95),
            (90, 30,  80),
            (50, 40,  70),
            (75, 25,  90),
            (30, 10,  55),
            (35, 45,  65),
            (45, 35,  85),
            (80, 10, 110),
            (85, 15, 75),
            (70, 30, 60),
            (40, 10, 85),
            (45, 20, 35),
            (30, 10, 65),
            (65, 25, 55),
            (35, 15, 60),
            (80, 35, 90),
            (70, 45, 85),
            (45, 10, 100)]

weightLimit = 250
volumeLimit = 120

class State:
    def __init__(self, backpack, weight, volume, price):
        self.backpack = backpack.copy()
        self.weight = weight
        self.volume = volume
        self.price = price


backpack = []

for i in range(len(itemList)):  # empty backpack
    backpack.append(False)

def initialState():
    return State(backpack, 0, 0, 0)


# generates a set of states (population)
def current_gen(size):
    ret = []

    for i in range(size):
        s = initialState()

        while True:
        # for j in range(200):
            x = randint(0, len(itemList) - 1)

            if s.backpack[x]:
                continue

            (w, v, p)  = itemList[x]

            if(s.weight + w <= weightLimit and s.volume + v <= volumeLimit):
                s.weight += w
                s.volume += v
                s.price += p
                s.backpack[x] = True
            else:
                break
        
        ret.append(s)
    
    return ret


def copy(s):
    s2 = initialState()
    s2.backpack = s.backpack
    s2.weight = s.weight
    s2.volume = s.volume
    s2.price = s.price

    return s2

def succ(s):
    f = randint(0, 1)

    for j in range(100):
        s2 = copy(s)
        x = randint(0, len(s2.backpack) - 1)

        (w, v, p)  = itemList[x]

        if(f == 0):
            if( not s2.backpack[x] ):
                if( s2.weight + w <= weightLimit and s2.volume + v <= volumeLimit):
                    s2.weight += w
                    s2.volume += v
                    s2.price += p
                    s2.backpack[x] = True

                    return s2
            else:
                continue
        else:
            if(s2.backpack[x]):
                s2.weight -= w
                s2.volume -= v
                s2.price -= p
                s2.backpack[x] = False

                return s2
            else:
                continue
    
    return s


def choose(set):
    b1 = set[randint(0, len(set) - 1)]
    b2 = set[randint(0, len(set) - 1)]

    if b1.price > b2.price:
        return b1
    return b2


# crossing with probabilistic division
def cross(s1, s2):
    for j in range(200):
        ret = initialState()
        f = randint(0, len(itemList) - 1)

        for i in range(len(backpack)):
            if i <= f:
                ret.backpack[i] = s1.backpack[i]
            else:
                ret.backpack[i] = s2.backpack[i]

        # update backpack values
        for i in range(len(backpack)):
            if ret.backpack[i]:
                (w, v, p)  = itemList[i]
                ret.weight += w
                ret.volume += v
                ret.price += p
        
        # checks if it complies with the limits
        if(ret.weight <= weightLimit and ret.volume <= volumeLimit):
            return ret

    x = randint(0, 1)
    if x == 1:
        return s1
    else:
        return s2


def mutate(s):
    if(uniform(0.0, 1.0) <= 0.1):
        return succ(s)
    return s


prices = []
population_size = 300
number_of_generations = 30

cg = current_gen(population_size)

firstGen = [] # it will storage the first generation prices
for i in range(population_size):
    firstGen.append(cg[i].price)
firstGen.sort(reverse=True)

best30first = [] # it will storage the 30 best prices from first generation
for i in range(10):
    best30first.append(firstGen[i])
best30first.sort(reverse=True)

ind = np.arange(10)

plt.figure(1)
plt.bar(ind, best30first)
plt.title('Top ten of the first generation')
plt.xlabel('Top ten')
plt.ylabel('Best price')

lastGen = [] # it will storage the last generation prices
best30last = [] # it will storage the 30 best prices from last generation

for i in range(number_of_generations):
    next_gen = []
    best = 0

    for j in range(population_size):
        x = choose(cg)
        y = choose(cg)
        child = cross(x, y)
        if(child.price > best):
            best = child.price
        child = mutate(child)
        next_gen.append(child)
    
    if (i == number_of_generations - 1):
        for i in range(population_size):
            lastGen.append(next_gen[i].price)
        
        lastGen.sort(reverse=True)

        for i in range(10):
            best30last.append(lastGen[i])
        best30last.sort(reverse=True)
        
    prices.append(best)
    print('')
    cg = next_gen

best = cg[0]
for s in cg:
    if(s.price > best.price):
        best = s

print('Backpack = ', best.backpack)
print('Weight = ', best.weight, 'Volume = ', best.volume, 'Price = ', best.price)

ind2 = np.arange(number_of_generations)

plt.figure(2)
plt.bar(ind2, prices)
plt.title('Solution quality vs. Number of generations')
plt.xlabel('Number of generations')
plt.ylabel('Best price')

plt.figure(3)
plt.bar(ind, best30last)
plt.title('Top ten of the last generation')
plt.xlabel('Top ten')
plt.ylabel('Best price')

plt.show()

