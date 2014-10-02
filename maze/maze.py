# CS364 Assignment 2.1
# Cole Peppis and Ben Stern

from search import *
from math import fabs

# Representation of the maze based on cell configuration

maze0 = [
    ['0110', '0101', '0101', '0101', '0101', '0101', '0101', '0111', '0101', '0101', '0101', '0101', '0101', '0001'],
    ['1010', '0110', '0011', '0110', '0011', '0100', '1100', '0101', '0101', '0101', '0101', '0111', '0101', '0011'],
    ['1010', '1010', '1010', '1010', '1100', '0101', '0101', '0101', '0101', '0101', '0011', '1010', '0110', '1011'],
    ['1010', '1010', '1010', '1010', '1001', '0101', '0101', '0101', '0101', '0011', '1010', '1010', '1010', '1010'],
    ['1010', '1010', '1010', '1010', '1010', '0110', '0101', '0101', '0101', '1001', '1100', '1001', '1010', '1010'],
    ['1010', '1010', '1110', '1011', '1010', '1110', '0101', '0101', '0101', '0011', '0010', '0010', '1010', '1010'],
    ['1110', '1011', '1010', '1010', '1010', '1010', '0110', '0011', '0010', '1010', '1010', '1010', '1010', '1010'],
    ['1010', '1010', '1010', '1000', '1010', '1010', '1110', '1001', '1010', '1010', '1010', '1010', '1010', '1010'],
    ['1010', '1010', '1010', '0110', '1011', '1010', '1010', '0110', '1011', '1010', '1010', '1110', '1011', '1010'],
    ['1010', '1010', '1010', '1010', '1010', '1010', '1010', '1010', '1010', '1010', '1110', '1011', '1010', '1010'],
    ['1010', '1110', '1011', '1010', '1010', '1010', '1010', '1010', '1010', '1010', '1010', '1010', '1010', '1010'],
    ['1010', '1000', '1000', '1010', '1100', '1101', '1011', '1010', '1010', '1010', '1010', '1010', '1000', '1010'],
    ['1010', '0110', '0101', '1101', '0011', '0100', '1011', '1010', '1110', '1011', '1010', '1000', '0110', '1011'],
    ['1100', '1001', '0100', '0101', '1001', '0100', '1101', '1001', '1000', '1000', '1100', '0101', '1001', '1000']
    ]

def rules_str(node):
    square_str = maze0[node[1]][node[0]]
    return square_str
rules = []
rules.append({"pre": lambda n:rules_str(n)[0] == '1',"act": lambda n:(n[0], n[1]-1)})
rules.append({"pre": lambda n:rules_str(n)[1] == '1',"act": lambda n:(n[0]+1, n[1])})
rules.append({"pre": lambda n:rules_str(n)[2] == '1',"act": lambda n:(n[0], n[1]+1)})
rules.append({"pre": lambda n:rules_str(n)[3] == '1',"act": lambda n:(n[0]-1, n[1])})

goal = lambda n: n == (6,7)

legal = lambda n: True

root = Node((6,0), rules, legal)

x = lambda n:1

h = lambda n: abs(n[0]-6) + abs(n[1] - 7)


# ....
# ....
# .... The following main program runs all 5 searchs using the new versions in search.py

if __name__ == '__main__':
    print("CS364, Assignment 2, Ben Stern, Cole Peppis")
    print('1a   i: Depth-First:     ', depth(root, goal, silent=True))
    print('1a  ii: Hill-Climbing:   ', hill(root, goal, h, silent=True))
    print('1a iii: Steepest-Ascent: ', steep(root, goal, h, silent=True))
    print('1a  iv: Best-First:      ', best(root, goal, h, silent=True))
    print('1a   v: Algorithm A:     ', algAM(root, goal, h, silent=True))

