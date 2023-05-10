from heapq import heappop, heappush

# goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
goal = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12],[13, 14, 15, 0]]

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
                if j != len(goal) - 1:
                    if(self.puzzle[i][j] < 10):
                        print('0', end='')
                        print(self.puzzle[i][j], end=' ')
                    else:
                        print(self.puzzle[i][j], end=' ')
                else:
                    if(self.puzzle[i][j] < 10):
                        print('0', end='')
                        print(self.puzzle[i][j], end=' ')
                    else:
                        print(self.puzzle[i][j], end=' ')
                    print()
        print()
    
    def heuristic(self):
        h = 0

        for i in range(len(self.puzzle)):
            for j in range(len(self.puzzle)):
                if self.puzzle[i][j] != goal[i][j]:
                    h += 1
        
        return h
    
    def distToGoal(self, i, j):
        k = self.puzzle[i][j]
        i_ = len(self.puzzle) - 1
        j_ = i_

        if(k != 0):
            i_ = int((k-1) / len(self.puzzle))
            j_ = int((k-1) % len(self.puzzle))
        
        return abs(i - i_) + abs(j - j_)
    
    def heuristic2(self):
        h = 0
           
        for i in range(len(self.puzzle)):
            for j in range(len(self.puzzle)):
                # m = self.puzzle[i][j]
                h += self.distToGoal(i, j)
                # n = self.distToGoal(i, j)
                # print(m, n)

        return h


def isGoal(s):
    # return s.puzzle == [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
    return s.puzzle == goal


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

    # p = [[3, 2, 5],  # C4
    #      [1, 7, 6],
    #      [4, 0, 8]]

    # p = [[4, 1, 5],  # C5 0m0,993s
    #      [8, 3, 7],
    #      [2, 6, 0]]

    # p = [[1, 0, 4],  # C6 0m7,574s
    #      [3, 7, 5],
    #      [6, 2, 8]]

    p = [[ 5,  1,  2,  4], 
         [ 9,  6,  3,  8], 
         [10, 14,  7, 11], 
         [13,  0, 15, 12]]

    # p = [[ 2, 14, 10,  8],
    #      [ 1, 13,  4, 11],
    #      [ 5,  6, 12,  0],
    #      [ 9,  7,  3, 15]]

    # p = [[ 0,  2, 13,  6],
    #      [ 9,  4,  7, 12],
    #      [14, 10,  8,  5],
    #      [11, 15,  3,  1]]                 

    # p = [[0, 8, 4],
    #      [1, 2, 7],
    #      [3, 6, 5]]
#    p = [[1, 6, 7],  # cancelado em 25m
#         [3, 5, 8],
#         [4, 2, 0]]
    # p = [[0, 8, 3],  #
    #      [2, 1, 5],
    #      [4, 7, 6]]
    # p = [[7, 1, 2],  # real	11m25,381s
    #      [6, 0, 8],
    #      [4, 5, 3]]
    # p = [[0, 3, 5],  # real	0m0,283s 10 moves
    #      [1, 2, 6],
    #      [4, 7, 8]]

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
    if s.row != len(goal) - 1:
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
    if s.col != len(goal) - 1:
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
#    heappush(queue, (s.heuristic(), s))
#    heappush(queue, (s.heuristic2(), s))
#    heappush(queue, (s.heuristic() + s.cost , s))
    heappush(queue, (s.heuristic2() + s.cost , s))


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
