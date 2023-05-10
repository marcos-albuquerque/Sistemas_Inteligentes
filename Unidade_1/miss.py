class State:
    def __init__(self, ml, cl, mr, cr, boat, parent):
        self.ml = ml
        self.cl = cl
        self.mr = mr
        self.cr = cr
        self.boat = boat
        self.parent = parent
    
    def show(self):
        if (self.boat == 0):
            b = "*|| "
        if (self.boat == 1):
            b = " ||*"
        print(f'{self.ml} {self.cl} {b} {self.mr} {self.cr}')
    
    def isGoal(self):
        if ( self.mr == 3 and self.cr == 3 ):
            return True
        return False
    
    def isValid(self):
        if ( (self.ml < self.cl and self.ml != 0) or (self.mr < self.cr and self.mr != 0) ):
            return False
        if ( self.ml > 3 or self.mr > 3 or self.cl > 3 or self.cr > 3 ):
            return False
        if ( self.ml < 0 or self.mr < 0 or self.cl < 0 or self.cr < 0 ):
            return False
        if ( (self.ml + self.mr) > 3 or (self.cl + self.cr)  > 3 ):
            return False
        if ( (self.ml + self.mr) < 0 or (self.cl + self.cr)  < 0 ):
            return False
        return True


def expand(s):
    ret = []

    # move 1 cannibal
    if( s.boat == 0 ):
        child0 = State(s.ml, s.cl - 1, s.mr, s.cr + 1, 1, s)
    if( s.boat == 1 ):
        child0 = State(s.ml, s.cl + 1, s.mr, s.cr - 1, 0, s)

    # move 1 missionary
    if( s.boat == 0 ):
        child1 = State(s.ml - 1, s.cl, s.mr + 1, s.cr, 1, s)
    if( s.boat == 1 ):
        child1 = State(s.ml + 1, s.cl, s.mr - 1, s.cr, 0, s)

    # move 2 cannibals
    if( s.boat == 0 ):
        child2 = State(s.ml, s.cl - 2, s.mr, s.cr + 2, 1, s)
    if( s.boat == 1 ):
        child2 = State(s.ml, s.cl + 2, s.mr, s.cr - 2, 0, s)

    # move 2 missionaries
    if( s.boat == 0 ):
        child3 = State(s.ml - 2, s.cl, s.mr + 2, s.cr, 1, s)
    if( s.boat == 1 ):
        child3 = State(s.ml + 2, s.cl, s.mr - 2, s.cr, 0, s)

    # move 1 cannibal and 1 missionary
    if( s.boat == 0 ):
        child4 = State(s.ml - 1, s.cl - 1, s.mr + 1, s.cr + 1, 1, s)
    if( s.boat == 1 ):
        child4 = State(s.ml + 1, s.cl + 1, s.mr - 1, s.cr - 1, 0, s)

    # ad children to the queue
    ret.append(child0)
    ret.append(child1)
    ret.append(child2)
    ret.append(child3)
    ret.append(child4)

    return ret


def showPath(s):
    if s is None:
        return
    showPath(s.parent)
    s.show()


def initialState():
    return State(3, 3, 0, 0, 0, None)


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


def isEqual(s1, s2):
    return s1.ml == s2.ml and s1.cl == s2.cl and s1.mr == s2.mr and s1.cr == s2.cr and s1.boat == s2.boat


def isOnPath(child, ancestor):
    if ancestor is None:
        return False
    if isEqual(child, ancestor):
        return True
    return isOnPath(child, ancestor.parent)


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
    if current.isGoal():
        print('Searched goal!')
        showPath(current)
        break
    current.show()
    children = expand(current)
    expandedStates.append(current)
    for child in children:
        if not child.isValid():
            continue
        enqueue(child)
