# CS364 Artificial Intelligence
# Cole Peppis and Ben Stern

from search1 import *

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

A.setSuccessors([(B,.75),(C,7)])
B.setSuccessors([(A,75)])
C.setSuccessors([(C,7),(D,2.5),(E,.5)])
D.setSuccessors([(C,2.5)])
E.setSuccessors([(C,.5),(F,3.5),(G,4.5)])
F.setSuccessors([(E,3.5)])
G.setSuccessors([(E,4.5),(H,2.5),(I,1)])
H.setSuccessors([(G,2.5),(I,1),(J,3.5)])
I.setSuccessors([(G,1),(H,1),(J,.75)])
J.setSuccessors([(I,.75),(H,3.5),(K,4.25)])
K.setSuccessors([(J,4.25),(L,1),(M,2.5)])
L.setSuccessors([(K,1)])
M.setSuccessors([(K,2.5)])

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
goal = gnGoal
h = lambda n: hd[n]
# .... The following main program runs all 5 searches using the new versions in search.py
if __name__ == '__main__':
    print("CS364, Assignment 2, Problem 2b, Cole Peppis, Ben Stern")
    print('Depth First Search: ', depth(root, goal, silent=True))
    print('Hill Climbing: ', hill(root, goal, h, silent=True))
    print('Steepest Ascent Hill Climbing: ', steep(root, goal, h, silent=True))
    print('Best First Search: ', best(root, goal, h, silent=True))
    print('Algorithm A: ', algAM(root, goal, h, silent=True))

