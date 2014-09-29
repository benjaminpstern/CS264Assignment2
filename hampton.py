# CS364 Artificial Intelligence
# Use this file to hold your solution to hamptonA

from search import *


# .... The following main program runs all 5 searchs using the new versions in search.py

if __name__ == '__main__':
    print("CS364, Assignment 2, Ima Student, Ura Student")
    print('1a: ', depth(root, goal, silent=True))
    print('1b: ', hill(root, goal, h, silent=True))
    print('1c: ', steep(root, goal, h, silent=True))
    print('1d: ', best(root, goal, h, silent=True))
    print('1e: ', algAM(root, goal, h, silent=True))
