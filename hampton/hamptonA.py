# CS364 Artificial Intelligence
# Cole Peppis and Ben Stern

from search import *

A = GraphNode('A')
B = GraphNode('B')
C = GraphNode('C')
D = GraphNode('D')
E = GraphNode('E')
F = GraphNode('F')
G = GraphNode('G')
H = GraphNode('H')
I = GraphNode('I')
J = GraphNode('J')
K = GraphNode('K')
L = GraphNode('L')
M = GraphNode('M', goal=True)

A.setSuccessors([B,C])
B.setSuccessors([A])
C.setSuccessors([D,E])
D.setSuccessors([C])
E.setSuccessors([C,F,G])
F.setSuccessors([E])
G.setSuccessors([E,H,I])
H.setSuccessors([G,I,J])
I.setSuccessors([G,H,J])
J.setSuccessors([I,H,K])
K.setSuccessors([J,L,M])
L.setSuccessors([K])
M.setSuccessors([K])

hd = {}
hd[A] = 1
hd[B] = 1.5
hd[C] = 1.25
hd[D] = 1.5
hd[E] = 1
hd[F] = .5
hd[G] = 1.25
hd[H] = .5
hd[I] = 1.25
hd[J] = 1.5
hd[K] = 1.25
hd[L] = .75
hd[M] = 0

root = graphToNode(A,rulemaker(3))
goal = lambda n: n.isGoal()
h = lambda n: hd[n]
# .... The following main program runs all 5 searches using the new versions in search.py
if __name__ == '__main__':
    print("CS364, Assignment 2, Problem 2a, Cole Peppis, Ben Stern")
    print('Depth First Search: ', depth(root, goal, silent=True))
    print('Hill Climbing: ', hill(root, goal, h, silent=True))
    print('Steepest Ascent Hill Climbing: ', steep(root, goal, h, silent=True))
    print('Best First Search: ', best(root, goal, h, silent=True))
    print('Algorithm A: ', algAM(root, goal, h, silent=True))
