# CS364 search1.py 
# contains classes used by all graphsearch algorithms
# including GraphNode
# and all search algorithms:
#   depth:  depth-first search   
#   hill:   hill-climbing
#   steep:  steepest ascent hill-climbing
#   best:   best-first search
#   algA:   algorithm A with path redirection
#   algAM:  algorithm A without path redirection

# this version models non-uniform costs

# depth first search

def depth(root, goal, silent=False):
    ans = Stack()
    open = Stack()
    open.push(root)
    closed = set()
    ctr = 0
    while not open.isEmpty():
        ctr += 1
        node = open.pop()
        while not ans.isEmpty() and not node in ans.top().successors():
            if not silent:
                print("backtrack")
            ans.pop()
        ans.push(node)
        if not silent:
            print(node)
        if goal(node.state()):
            break
        closed.add(node)
        open.push(list(filter(lambda e: not e in closed, node.successors())))
    return {"result": ans, "steps": ctr, "cost": ans.top().cost(), "nodes": open.length()+len(closed)}

# hill climbing

def hill(root, goal, H, silent=False):
    path = [root]
    ctr = 0
    best = None
    while True:
        ctr += 1
        node = path[0]
        if not silent:
            print(ctr, node, "H="+str(H(node.state())))
        for s in node.successors():
            if best == None or H(s.state()) < H(best.state()):
                best = s
        if H(best.state()) < H(node.state()):
            path = [best]+path
        else:
            break
    cost = path[0].cost()
    path.reverse()
    return {"result": path, "steps": ctr, "cost": cost, "nodes": len(path)-1}

# steepest ascent hill climbing

def steep(root, goal, h, silent=False):
    ans = Stack()
    open = Stack()
    open.push(root)
    closed = set()
    ctr = 0
    while not open.isEmpty():
        ctr += 1
        node = open.pop()
        while not ans.isEmpty() and not node in ans.top().successors():
            if not silent:
                print("backtrack")
            ans.pop()
        ans.push(node)
        if not silent:
            print(node)
        if goal(node.state()):
            break
        closed.add(node)
        open.push(sorted(list(filter(lambda e: not e in closed, node.successors())),
                         key=lambda n: h(n.state())))
    return {"result": ans, "steps": ctr, "cost": ans.top().cost(), "nodes": open.length()+len(closed)}

# best-first search with path redirection

def best(root, goal, h, silent=False):
    f = lambda p: h(p[0].state())
    open = [[root]]
    closed = set()
    ctr = 0
    while open != []:
        ctr += 1
        path = open.pop(0)
        tmp = f(path)
        node = path[0]
        if not silent:
            print(ctr, node, "f="+str(tmp))
        if goal(node.state()):
            cost = path[0].cost()
            path.reverse()
            return {"result": path, "steps": ctr,
                    "cost": cost, "nodes": len(open)+len(closed)}
        closed.add(node)
        for s in node.successors():
            if s in closed:
                continue;
            spath = [s]+path
            scost = f(spath)
            found = False
            for i in range(len(open)):
                p = open[i]
                for j in range(len(p)):
                    p0 = p[j:]
                    if s != p0[0]:
                        continue
                    if j == 0:
                        found = True
                    if scost < f(p0):
                        p1 = p[0:j]+spath
                        open[i] = p1
            if not found:
                open = [spath] + open
        open.sort(key=f)
    return 'fail'

# Algorithm A with path redirection

def algA(root, goal, h, silent=False):
    f = lambda p: h(p[0].state()) +p[0].cost()
    open = [[root]]
    closed = set()
    ctr = 0
    while open != []:
        ctr += 1
        path = open.pop(0)
        tmp = f(path)
        node = path[0]
        if not silent:
            print(ctr, node, "f="+str(tmp))
        if goal(node.state()):
            cost = f(path)
            path.reverse()
            return {"result": path, "steps": ctr,
                    "cost": cost, "nodes": len(open)+len(closed)}
        closed.add(node)
        for s in node.successors():
            if s in closed:
                continue;
            spath = [s]+path
            scost = f(spath)
            found = False
            for i in range(len(open)):
                p = open[i]
                for j in range(len(p)):
                    p0 = p[j:]
                    if s != p0[0]:
                        continue
                    if j == 0:
                        found = True
                    if scost < f(p0):
                        p1 = p[0:j]+spath
                        open[i] = p1
            if not found:
                open = [spath] + open
        open.sort(key=f)
    return 'fail'

# Algorithm A without path redirection (assumes monotonic h)

def algAM(root, goal, h, silent=False):
    f = lambda p: h(p[0].state()) +p[0].cost()
    open = [[root]]
    closed = set()
    ctr = 0
    while open != []:
        ctr += 1
        path = open.pop(0)
        tmp = f(path)
        node = path[0]
        if not silent:
            print(ctr, node, "f="+str(tmp))
        if goal(node.state()):
            cost = f(path)
            path.reverse()
            return {"result": path, "steps": ctr,
                    "cost": cost, "nodes": len(open)+len(closed)}
        closed.add(node)
 
        for s in node.successors():
            if s in closed:
                continue
            if s in list(map(lambda n: n[0], open)):
                continue
            spath = [s]+path
            open = [spath] + open

        open.sort(key=f)
    return 'fail'

# Node(state, rules, legal)
#   represents a graph node in a particular problem
#   initialized with a state, set of rules and legality test
#   state must be a hashable type (i.e., a number or a tuple)
#   rules must be a list of using the precondition/action format:
#      {"pre": pre-fn, "act": act-fn, "cost": cost-fn}
#     where pre-fn accepts a state and returns True or False
#     where act-fn accepts a state and returns a state
#     where cost-fn accepts a state and returns the cost of moving to that state

class Node:
    def __init__(self, state, rules, legal, cost=0):
        self.__state = state
        self.__rules = rules
        self.__legal = legal
        self.__cost = cost
        self.__successors = None
    def successors(self):
        if self.__successors == None:
            self.__successors = []
            for rule in self.__rules:
                if not rule["pre"](self.__state):
                    continue
                child = rule["act"](self.__state)
                if self.__legal(child):
                    newcost = rule["cost"](self.__state) + self.__cost
                    self.__successors.append(Node(child, self.__rules, self.__legal, cost=newcost))
        return self.__successors
    def state(self):
        return self.__state
    def cost(self):
        return self.__cost
    def __hash__(self):
        return hash(self.__state)
    def __eq__(self, other):
        return type(other) == Node and self.__state == other.__state
    def __repr__(self):
        return str(self.__state)

# Stack()
#   general purpose stack object    

class Stack(object):
    def __init__(self):
        self.__data = list()
    def isEmpty(self):
        return len(self.__data) == 0
    def push(self, x):
        if type(x) == list:
            x.reverse()
            self.__data = self.__data + x
        else:
            self.__data.append(x)
    def top(self):
        try: 
            return self.__data[len(self.__data)-1]
        except Exception as e:
            print("Empty stack")
    def pop(self):
        try: 
            ans = self.__data.pop()
            return ans
        except Exception as e:
            print("Empty stack")
    def length(self):
        return len(self.__data)
    def __repr__(self):
        return str(self.__data)

# GraphNode is a class of labeled objects (using *id*) containing a set of successors
# A GraphNode may also be designated as a goal node

class GraphNode:
    def __init__(self, id, goal=False):
        self.__id = id
        self.__goal = goal
        self.__successors = []
    def setSuccessors(self, successors):
        self.__successors = successors
    def successors(self):
        return self.__successors
    def id(self):
        return self.__id
    def isGoal(self):
        return self.__goal
    def __repr__(self):
        goalmark = "G" if self.__goal else ""
        dots = "..." if len(self.__successors) > 0 else ""
        return "{"+str(self.__id)+goalmark+dots+"}"

# Successor is a pair (N, c), where N is a GraphNode and c is a number representing the cost.

# rulemaker builds a set of production rules for use with search.py,
# each of which maps a GraphNode to one of its successors

def rulemaker(branch):
    def rule(k):
        def pre(n):
            return k < len(n.successors())
        def act(n):
            return n.successors()[k][0]
        def cost(n):
            return n.successors()[k][1]
        return {"pre": pre, "act": act, "cost":cost}
    return [rule(k) for k in range(branch)]

# gnGoal is a goal detecting function for use with search.py

def gnGoal(n):
    return n.isGoal()

# graphToNode creates a search.Node from a GraphNode using rules produced by rulemaker

def graphToNode(t, rules):
    return Node(t, rules, lambda n: True)
