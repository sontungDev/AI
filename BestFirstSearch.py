from collections import defaultdict
from queue import PriorityQueue

class Node:
    def __init__(self, name, h = 0, par = None) -> None:
        self.name = name
        self.par = par
        self.h = h
    
    def display(seft) -> None:
        print(seft.name)

    def __lt__(self, o:object) -> bool:
        if o == None:
            return False
        return self.h < o.h
    
    def __eq__(self, o: object) -> bool:
        if o == None:
            return False
        return self.name == o.name


data = defaultdict(list)
data['A'] = ['B', 'C', 'D', 6]
data['B'] = ['E', 'F', 3]
data['C'] = ['G', 'H', 4]
data['D'] = ['I', 'J', 5]
data['E'] = [3]
data['F'] = ['K', 'L', 'M', 1]
data['G'] = [6]
data['H'] = ['N', 'O', 2]
data['I'] = [5]
data['J'] = [4]
data['K'] = [2]
data['L'] = [0]
data['M'] = [4]
data['N'] = [0]
data['O'] = [4]


def isNodeInOpenClosed(target : Node, open : PriorityQueue, closed : PriorityQueue) -> bool:
    if target == None:
        return False
    if target in open.queue:
        return True
    if target in closed.queue:
        return True
    return False

def path(target : Node, distance) -> None:
    target.display()
    distance += target.h
    if target.par != None:
        path(target.par, distance)
    return

def BFS(start : Node, end : Node) -> None:
    open = PriorityQueue()
    closed = PriorityQueue()
    
    start.h = data[start.name][-1]

    open.put(start)

    while not open.empty():
        openNode = open.get()
        if openNode.name == end.name:
            print('successly')
            path(openNode, 0)
            return
        closed.put(openNode)
        
        for i in range(0, len(data[openNode.name]) - 1):
            child = data[openNode.name]
            temp = Node(child[i], child[-1], openNode)            
            if not isNodeInOpenClosed(temp, open, closed):
                open.put(temp)

    print('Search fail')
    return

BFS(Node('A'), Node('O'))