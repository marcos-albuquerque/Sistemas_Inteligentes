fl = 'fl'
# fl2 = fl1
# fl3 = fl1
# fl4 = fl1
x = '_x_'
fr = 'fr'
# fr2 = fr1
# fr3 = fr1
# fr4 = fr1

class State:
    def __init__(self, p, parent):
        self.p = p
        self.parent = parent

    def show(self):
        for i in range(len(self.p)):
            print(self.p[i], end=' ')
        print()

    def isGoal(self):
        return self.p == [fr, fr, fr, fr, x, fl, fl, fl, fl]

def initialState():
    q = [fl, fl, fl, fl, x, fr, fr, fr, fr]
    return State(q, None)

def expand(s):
    ret = []

    # Um sapo da esquerda realiza um pulo simples para direita
    for i in range(len(s.p)):
        if s.p[i] == x and i != 0 and s.p[i - 1] != fr:
                pt = s.p.copy()
                temp = pt[i-1]
                pt[i-1] = x
                pt[i] = temp
                child = State(pt, s)
                ret.append(child)
                break

    # Um sapo da esquerda realiza um pulo duplo para direita
    for i in range(len(s.p)):
        if s.p[i] == x:
            if (i - 2 >= 0) and s.p[i-2] != fr:
                pt = s.p.copy()
                temp = pt[i - 2]
                pt[i - 2] = x
                pt[i] = temp
                child = State(pt, s)
                ret.append(child)
                break

    # Um sapo da dereita realiza um pulo simples para esquerda
    for i in range(len(s.p)):
        if s.p[i] == x and i != (len(s.p) - 1) and s.p[i + 1] != fl:
            pt = s.p.copy()
            temp = pt[i + 1]
            pt[i + 1] = x
            pt[i] = temp
            child = State(pt, s)
            ret.append(child)
            break
    
    # Um sapo da dereita realiza um pulo duplo para esquerda
    for i in range(len(s.p)):
        if s.p[i] == x:
            if (i+2 <= (len(s.p) - 1)) and s.p[i + 2] != fl:
                pt = s.p.copy()
                temp = pt[i + 2]
                pt[i + 2] = x
                pt[i] = temp
                child = State(pt, s)
                ret.append(child)
                break
    return ret

def showPath(s):
    if s is None:
        return
    showPath(s.parent)
    s.show()

queue = []
expandedStates = []

def queueIsEmpty():
    return len(queue) == 0

def enqueue(s):
    queue.append(s)

def dequeue():
    temp = queue[0]
    del queue[0]
    return temp

i = 0
s = initialState()
enqueue(s)

s.show()

while not queueIsEmpty():
    current = dequeue()
    if current.isGoal():
        print('\nSearched goal!')
        showPath(current)
        print('Number of expanded states: ', i)
        break
    current.show()
    children = expand(current)
    # expandedStates.append(current)
    for child in children:
        enqueue(child)
        i += 1
