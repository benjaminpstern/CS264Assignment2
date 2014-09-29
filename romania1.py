# CS364 Romania traveling problem using arc values
# Running this from the prompt will produce 5 searchs

from search1 import *

Arad = GraphNode('Arad')
Bucharest = GraphNode('Bucharest', goal=True)
Oradea = GraphNode('Oradea')
Timisoara = GraphNode('Timisoara')
Sibiu = GraphNode('Sibiu')
Craiova = GraphNode('Craiova')
Dobreta = GraphNode('Dobreta')
Eforie = GraphNode('Eforie')
Fagaras = GraphNode('Fagaras')
Giurgiu = GraphNode('Giurgiu')
Hirsova = GraphNode('Hirsova')
Iasi = GraphNode('Iasi')
Lugoj = GraphNode('Lugoj')
Mehadia = GraphNode('Mehadia')
Neamt = GraphNode('Neamt')
Pitesti = GraphNode('Pitesti')
Rimunicu_Vilcea = GraphNode('Rimunicu_Vilcea')
Urziceni = GraphNode('Urziceni')
Vaslui = GraphNode('Vaslui')
Zerind = GraphNode('Zerind')

# Include arc values when setting successors by pairing the successor with
# the arc value

Arad.setSuccessors([(Zerind,75), (Sibiu, 140), (Timisoara,118)])
Oradea.setSuccessors([(Zerind,71), (Sibiu,151)])
Timisoara.setSuccessors([(Arad,118), (Lugoj,111)])
Sibiu.setSuccessors([(Arad,140), (Oradea,151), (Fagaras,99), (Rimunicu_Vilcea,80)])
Craiova.setSuccessors([(Dobreta,120), (Rimunicu_Vilcea,146), (Pitesti, 138)])
Dobreta.setSuccessors([(Mehadia,75), (Craiova,120)])
Eforie.setSuccessors([(Hirsova,86)])
Fagaras.setSuccessors([(Sibiu,99), (Bucharest,211)])
Giurgiu.setSuccessors([(Bucharest,90)])
Hirsova.setSuccessors([(Urziceni,98), (Eforie,86)])
Iasi.setSuccessors([(Neamt,87), (Vaslui,92)])
Lugoj.setSuccessors([(Timisoara,111), (Mehadia,70)])
Mehadia.setSuccessors([(Lugoj,70), (Dobreta,75)])
Neamt.setSuccessors([(Iasi,87)])
Pitesti.setSuccessors([(Craiova,138), (Rimunicu_Vilcea,97), (Bucharest,101)])
Rimunicu_Vilcea.setSuccessors([(Sibiu,80), (Pitesti,97), (Craiova,138)])
Urziceni.setSuccessors([(Bucharest,85), (98,Hirsova), (Vaslui,142)])
Vaslui.setSuccessors([(Iasi,92), (Urziceni,142)])
Zerind.setSuccessors([(Arad,75), (Oradea,75)])

rules = rulemaker(4)

goal = gnGoal

root = graphToNode(Arad, rules)

def h(n):
    return {
        'Arad':366,
        'Bucharest':0,
        'Craiova':160,
        'Dobreta':242,
        'Eforie':161,
        'Fagaras':178,
        'Giurgiu':77,
        'Hirsova':151,
        'Iasi':226,
        'Lugoj':244,
        'Mehadia':241,
        'Neamt':234,
        'Oradea':380,
        'Pitesti':98,
        'Rimunicu_Vilcea':193,
        'Sibiu':253,
        'Timisoara':329,
        'Urziceni':80,
        'Vaslui':199,
        'Zerind':374
    }[n.id()]
        
if __name__ == '__main__':
    print('depth: ', depth(root, goal, silent=True))
    print('hill:  ', hill(root, goal, h, silent=True))
    print('steep: ', steep(root, goal, h, silent=True))
    print('best:  ', best(root, goal, h, silent=True))
    print('alg A: ', algAM(root, goal, h, silent=True))
