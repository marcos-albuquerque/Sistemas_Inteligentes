fl1 = 'fl1'
fl2 = 'fl2'
fl3 = 'fl3'
x   = '_x_'
fr1 = 'fr1'
fr2 = 'fr2'
fr3 = 'fr3'

class State:
    def __init__(self, p, depth, parent):
        self.p = p
        self.depth = depth
        self.parent = parent
    
    def show(self):
        print(self.p[0], self.p[1], self.p[2], self.p[3], self.p[4], self.p[5], self.p[6])
    
    def isGoal(self):
        return self.p == [fr1, fr2, fr3, x, fl3, fl2, fl1]

def initialState():
    q = [fl3, fl2, fl1, x, fr1, fr2, fr3]
    return State(q, 0, None)

def expand(s):
    ret = []

    # Um sapo da esquerda realiza um pulo simples para direita
    for i in range(7):
        if s.p[i] == x and i != 0 and s.p[i-1]!=fr1 and s.p[i-1]!=fr2 and s.p[i-1]!=fr3:
                pt = s.p.copy()
                temp = pt[i - 1]
                pt[i - 1] = x
                pt[i] = temp
                child = State(pt, s.depth + 1, s)
                ret.append(child)
                break
    
    # Um sapo da esquerda realiza um pulo duplo para direita
    for i in range(7):
        if s.p[i] == x:
            if (i-2 >= 0) and s.p[i-2] != fr1 and s.p[i-2] != fr2 and s.p[i-2] != fr3:
                pt = s.p.copy()
                temp = pt[i-2]
                pt[i-2] = x
                pt[i] = temp
                child = State(pt, s.depth + 1, s)
                ret.append(child)
                break

    # Um sapo da dereita realiza um pulo simples para esquerda
    for i in range(7):
        if s.p[i] == x and i != 6 and s.p[i+1]!=fl1 and s.p[i+1]!=fl2 and s.p[i+1]!=fl3:
            pt = s.p.copy()
            temp = pt[i + 1]
            pt[i + 1] = x
            pt[i] = temp
            child = State(pt, s.depth + 1, s)
            ret.append(child)
            break
    
    # Um sapo da dereita realiza um pulo duplo para esquerda
    for i in range(7):
        if s.p[i] == x:
            if (i+2 <= 6) and s.p[i+2] != fl1 and s.p[i+2] != fl2 and s.p[i+2] != fl3:
                pt = s.p.copy()
                temp = pt[i+2]
                pt[i+2] = x
                pt[i] = temp
                child = State(pt, s.depth + 1, s)
                ret.append(child)
                break
    return ret

def showPath(s):
    if s is None:
        return
    showPath(s.parent)
    s.show()


stack = []


def stackIsEmpty():
    return len(stack) == 0


def push(s):
    stack.append(s)


def pop():
    return stack.pop()


depthLimit = 15
i = 0
s = initialState()
push(s)

while not stackIsEmpty():
    current = pop()
    if current.isGoal():
        print('\nSearched goal!')
        showPath(current)
        print('Number of expanded states: ', i)
        break
    current.show()
    if current.depth >= depthLimit:
        continue
    children = expand(current)
    for child in children:
        push(child)
        i += 1
