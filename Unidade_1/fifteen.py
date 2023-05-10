from heapq import heappop, heappush

class State:
    def __init__(self, puzzle, cost, row, col, parent):
        self.puzzle = puzzle
        self.cost = cost
        self.row = row
        self.col = col
        self.parent = parent

    def __lt__(self, other):
        return self.cost <= other.cost

    def show(self):
        for i in range(len(self.puzzle)):
            for j in range(len(self.puzzle)):
                if j != 2:
                    print(self.puzzle[i][j], end=' ')
                else:
                    print(self.puzzle[i][j], end=' ')
                    print()
        print()


def isGoal(s):
    return s.puzzle == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]


def initialState():
#    p = [[7, 2, 1],  # real	1m7,213s   16 moves C1
#         [5, 0, 3],
#         [4, 8, 6]]
         
#    p = [[0, 8, 3],  # C2
#         [2, 1, 5],
#         [4, 7, 6]]

#    p = [[0, 3, 5],  # real	0m0,283s 10 moves C3
#         [1, 2, 6],
#         [4, 7, 8]]

#    p = [[3, 2, 5],  # C4
#         [1, 7, 6],
#         [4, 0, 8]]

    # p = [[0, 8, 4],
    #      [1, 2, 7],
    #      [3, 6, 5]]
    # p = [[1, 6, 7],  # cancelado em 25m
    #      [3, 5, 8],
    #      [4, 2, 0]]

    # p = [[7, 1, 2],  # real	11m25,381s
    #      [6, 0, 8],
    #      [4, 5, 3]]

    
    for i in range(len(p)):
        for j in range(len(p)):
            if p[i][j] == 0:
                return State(p, 0, i, j, None)


def copy(puzzle):
    pcopy = []
    for row in puzzle:
            pcopy.append(row.copy())
    return pcopy


def expand(s):
    ret = []
    
    # swap between above piece and the empty space
    if s.row != 0:
        pcopy = copy(s.puzzle)

        aux = pcopy[s.row][s.col]
        pcopy[s.row][s.col] = pcopy[s.row - 1][s.col]
        pcopy[s.row - 1][s.col] = aux

        child = State(pcopy, s.cost + 1, s.row, s.col, s)
        child.row -= 1
        ret.append(child)
    
    # swap between below piece and the empty space
    if s.row != 2:
        pcopy = copy(s.puzzle)        

        aux = pcopy[s.row][s.col]
        pcopy[s.row][s.col] = pcopy[s.row + 1][s.col]
        pcopy[s.row + 1][s.col] = aux

        child = State(pcopy, s.cost + 1, s.row, s.col, s)
        child.row += 1
        ret.append(child)

    # swap between the left piece and the empty space
    if s.col != 0:
        pcopy = copy(s.puzzle)

        aux = pcopy[s.row][s.col]
        pcopy[s.row][s.col] = pcopy[s.row][s.col - 1]
        pcopy[s.row][s.col - 1] = aux

        child = State(pcopy, s.cost + 1, s.row, s.col, s)
        child.col -= 1
        ret.append(child)
    
    # swap between the right piece and the empty space
    if s.col != 2:
        pcopy = copy(s.puzzle)

        aux = pcopy[s.row][s.col]
        pcopy[s.row][s.col] = pcopy[s.row][s.col + 1]
        pcopy[s.row][s.col + 1] = aux

        child = State(pcopy, s.cost + 1, s.row, s.col, s)
        child.col += 1
        ret.append(child)

    return ret


queue = []
expandedStates = []


def enqueue(s):
    heappush(queue, (s.cost, s))


def dequeue():
    # take off the state with the smallest cost
    (c, s) = heappop(queue)
    return s

def showPath(s):
    if s is None:
        return

    showPath(s.parent)
    s.show()


def queueIsEmpty():
    return len(queue) == 0


def isEqual(s1, s2):
    return s1.puzzle == s2.puzzle


def isOnExpandedStates(s):
    for state in expandedStates:
        if isEqual(s, state):
            return True
    return False


s = initialState()
enqueue(s)
es_counter = 0

while not queueIsEmpty():
    current = dequeue()

    if isOnExpandedStates(current):
        continue

    if isGoal(current):
        print('\nSearched goal!')
        showPath(current)
        print('Number of expanded states: ', es_counter)
        break

    current.show()
    children = expand(current)
    expandedStates.append(current)

    for child in children:
        enqueue(child)
        es_counter += 1

print(len(queue))
