class Node:
    def __init__(self, name, par = None) -> None:
        self.name = name
        self.par = par
    
    def display(seft) -> None:
        print(seft.name)
    
from collections import defaultdict
data = defaultdict(list)
data['A'] = ['B', 'C', 'D']
data['B'] = ['E', 'F']
data['C'] = ['G', 'H']
data['D'] = ['I', 'J']
data['F'] = ['K', 'L', 'M']
data['H'] = ['N', 'O']


def isNodeInOpenClosed(target, open, closed):
    for i in open:
        if target.name == i.name:
            return True
    for i in closed:
        if target.name == i.name:
            return True
    return False

def path(target):
    target.display()
    if target.par != None:
        path(target.par)
    return

def DFS(start, end):
    open = []
    closed = []
    open.append(start)
    while len(open) != 0:
        openNode = open.pop(0)
        if openNode.name == end.name:
            print('successly')
            path(openNode)
            return
        closed.append(openNode)
        for i in data[openNode.name]:
            temp = Node(i, openNode)
            if not isNodeInOpenClosed(temp, open, closed):
                open.insert(0,temp)

    print('Search fail')
    return

# run the app
DFS(Node('A'), Node('O'))