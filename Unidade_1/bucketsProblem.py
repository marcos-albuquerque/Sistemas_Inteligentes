class State:
    def __init__(self, v1, v2, parent):
        self.v1 = v1
        self.v2 = v2
        self.parent = parent

def isGoal(s):
    return s.v1 + s.v2 == 5

def initialState():
    return State(0, 0, None)

def showState(s):
    print('V1: ', s.v1, 'V2: ', s.v2)

def expand(s):
    ret = []

    child1 = State(0, s.v2, s) # empty the first backet
    child2 = State(s.v1, 0, s) # empty the second backet

    child3 = State(3, s.v2, s) # fill the first backet
    child4 = State(s.v1, 4, s) # fill the second backet

    t = 3 - s.v1
    if t > s.v2:
        t = s.v2
    child5 = State(s.v1 + t, s.v2 - t, s) # transfers without overflowing from bucket 2 to backet 1
    
    t = 4 - s.v2
    if t > s.v1:
        t = s.v1
    child6 = State(s.v1 - t, s.v2 + t, s) # transfers without overflowing from bucket 1 to backet 2

    ret.append(child1)
    ret.append(child2)
    ret.append(child3)
    ret.append(child4)
    ret.append(child5)
    ret.append(child6)

    return ret

def showPath(s):
    if s is None:
        return
    showPath(s.parent)
    showState(s)

def isEqual(s1, s2):
    return s1.v1 == s2.v1 and s1.v2 == s2.v2

def isOnPath(child, ancestor):
    if ancestor is None:
        return False
    if isEqual(child, ancestor):
        return True
    return isOnPath(child, ancestor.parent)

queue = []

def isOpenState(s):
    for state in queue:
        if isEqual(s, state):
            return True
    return False

def enqueue(s):
    queue.append(s)

def dequeue():
    return queue.pop()

def queueIsEmpty():
    return len(queue) == 0

expandedStates = []

def isOnExpandedStates(s):
    for state in expandedStates:
        if isEqual(s, state):
            return True
    return False

s = initialState()

enqueue(s)

while not queueIsEmpty():
    current = dequeue()
    if isOnExpandedStates(current):
        continue
    if isGoal(current):
        print('Reached goal!')
        showPath(current)
        break
    showState(current)
    children = expand(current)
    expandedStates.append(current)
    for child in children:
        if (not isOnPath(child, current)) and (not isOpenState(child)):
            enqueue(child)
