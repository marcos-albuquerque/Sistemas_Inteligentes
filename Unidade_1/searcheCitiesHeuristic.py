# Busca gulosa pela melhor escolha

# Heurística: distância em linha reta até Bucharest
from heapq import heappop, heappush

class City:
    def __init__(self, name, heuristic):
        self.name = name
        self.neighboors = []
        self.heuristic = heuristic
    
    def addNeighboors(self, neighboors):
        for city in neighboors:
            self.neighboors.append(city)

arad = City('Arad', 366)
zerind = City('Zerind', 374)
sibiu = City('Sibiu', 253)
timisoara = City('Timisoara', 329)
oradea = City('Oradea', 380)
lugoj = City('Lugoj', 244)
fagaras = City('Fagaras', 178)
vilcea = City('R. Vilcea', 193)
mehadia = City('Mehadia', 241)
bucharest = City('Bucharest', 0)
pitesti = City('Pitesti', 98)
craiova = City('Craiova', 160)
drobeta = City('Drobeta', 242)
urziceni = City('Urziceni', 80)
giurgiu = City('Giurgiu', 77)
vaslui = City('Vaslui', 199)
hisova = City('Hisova', 151)
iasi = City('Iasi', 226)
eforie = City('Eforie', 161)
neamt = City('Neamt', 234)

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
    heappush(queue, (s.city.heuristic, s))

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