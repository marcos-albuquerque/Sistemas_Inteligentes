# Busca de custo uniforme

from heapq import heappop, heappush

class City:
    def __init__(self, name):
        self.name = name
        self.neighboors = []
    
    def addNeighboors(self, neighboors):
        for city in neighboors:
            self.neighboors.append(city)

arad = City('Arad')
zerind = City('Zerind')
sibiu = City('Sibiu')
timisoara = City('Timisoara')
oradea = City('Oradea')
lugoj = City('Lugoj')
fagaras = City('Fagaras')
vilcea = City('R. Vilcea')
mehadia = City('Mehadia')
bucharest = City('Bucharest')
pitesti = City('Pitesti')
craiova = City('Craiova')
drobeta = City('Drobeta')
urziceni = City('Urziceni')
giurgiu = City('Giurgiu')
vaslui = City('Vaslui')
hisova = City('Hisova')
iasi = City('Iasi')
eforie = City('Eforie')
neamt = City('Neamt')

arad.addNeighboors([(75, zerind), (140, sibiu), (118, timisoara)])
zerind.addNeighboors([(71, oradea), (75, arad)])
sibiu.addNeighboors([(151, oradea), (140, arad), (99, fagaras), (80, vilcea)])
timisoara.addNeighboors([(118, arad), (111, lugoj)])
oradea.addNeighboors([(71, zerind), (151, sibiu)])
lugoj.addNeighboors([(111, timisoara), (70, mehadia)])
mehadia.addNeighboors([(70, lugoj), (75, drobeta)])
drobeta.addNeighboors([(75, mehadia), (120, craiova)])
craiova.addNeighboors([(120, drobeta), (146, vilcea), (138, pitesti)])
vilcea.addNeighboors([(80, sibiu), (97, pitesti), (146, craiova)])
pitesti.addNeighboors([(97, vilcea), (138, craiova), (101, bucharest)])
fagaras.addNeighboors([(99, sibiu), (211, bucharest)])
bucharest.addNeighboors([(85, urziceni), (90, giurgiu), (211, fagaras)])
giurgiu.addNeighboors([(90, bucharest)])
urziceni.addNeighboors([(85, bucharest), (98, hisova), (142, vaslui)])
hisova.addNeighboors([(86, eforie), (98, urziceni)])
eforie.addNeighboors([(86, hisova)])
vaslui.addNeighboors([(42, urziceni), (92, iasi)])
iasi.addNeighboors([(92, vaslui), (87, neamt)])
neamt.addNeighboors([(87, iasi)])

class State:
    def __init__(self, city, g, parent):
        self.city = city
        self.g = g
        self.parent = parent
    
    def __lt__(self, other):
        return self.g < other.g
    
def isGoal(s):
    return s.city.name == 'Bucharest'

def expand(s):
    ret = []

    for (cost, neighboor) in s.city.neighboors:
        child = State(neighboor, s.g + cost, s)
        ret.append(child)

    return ret

def initialState():
    return State(arad, 0, None)

def showState(s):
    print(s.city.name, ',', s.g)

queue = []

def enqueue(s):
    heappush(queue, (s.g, s))

def dequeue():
    (g, s) = heappop(queue) # retira estado com menor custo
    return s

def queueIsEmpty():
    return len(queue) == 0

def showPath(s):
    if s is None:
        return
    showPath(s.parent)
    showState(s)

i = 0
s = initialState()
enqueue(s)

while not queueIsEmpty():
    current = dequeue()
    if isGoal(current):
        print('\nSearched goal!')
        showPath(current)
        print('Number of expanded states: ', i)
        break
    # showState(current)
    children = expand(current)
    i += 1
    for child in children:
        enqueue(child)