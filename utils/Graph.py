from utils.Node import Node, infinity, create_leafs


def letterGraph():
    a = Node('A')
    b = Node('B')
    c = Node('C')
    d = Node('D')
    c = Node('C')
    e = Node('E')
    f = Node('F')
    g = Node('G')

    a.add_children([b, c])
    b.add_children([a, d, e])
    c.add_children([a, d])
    d.add_children([b, c, e, g, f])
    e.add_children([b, d, g])
    f.add_children([d, g])
    g.add_children([e, d, f])

    return a

def mapGraphWithCost():
    def create_node_with_cost(node, distance):
        return {'node': node, 'distance': distance, 'cost': infinity, 'via': None}

    arad = Node('Arad')
    sibiu = Node('Sibiu')
    timisoara = Node('Timisoara')
    zerind = Node('Zerind')
    fagaras = Node('Fagaras')
    oradea = Node('Oradea')
    rimniicu_vilcea = Node('Rimniicu Vilcea')
    lugoj = Node('Lugoj')
    bucharest = Node('Bucharest')
    pitesti = Node('Pitesti')
    craiova = Node('Craiova')
    mehadia = Node('Mehadia')
    urzieni = Node('Urzieni')
    drobeta = Node('Drobeta')
    hirsova = Node('Hirsova')
    vaslui = Node('Vaslui')
    iasi = Node('Iasi')

    arad.add_children([
        create_node_with_cost(sibiu, 140),
        create_node_with_cost(timisoara, 118),
        create_node_with_cost(zerind, 75)
    ])
    sibiu.add_children([
        create_node_with_cost(arad,140),
        create_node_with_cost(fagaras,99),
        create_node_with_cost(oradea,151),
        create_node_with_cost(rimniicu_vilcea, 80)
    ])
    timisoara.add_children([
        create_node_with_cost(arad, 118),
        create_node_with_cost(lugoj,111)
    ])
    zerind.add_children([
        create_node_with_cost(arad,75),
        create_node_with_cost(oradea,71)
    ])
    fagaras.add_children([
        create_node_with_cost(sibiu,99),
        create_node_with_cost(bucharest, 211)
    ])
    oradea.add_children([
        create_node_with_cost(zerind,71),
        create_node_with_cost(sibiu, 151)
    ])
    rimniicu_vilcea.add_children([
        create_node_with_cost(sibiu,80),
        create_node_with_cost(pitesti,97),
        create_node_with_cost(craiova, 146)
    ])
    lugoj.add_children([
        create_node_with_cost(timisoara,111),
        create_node_with_cost(mehadia,70)
    ])
    bucharest.add_children([
        create_node_with_cost(fagaras,211),
        create_node_with_cost(pitesti,101),
        create_node_with_cost(Node('Giurgiu'), 90), # Leaf Node
        create_node_with_cost(urzieni,85)
    ])
    pitesti.add_children([
        create_node_with_cost(rimniicu_vilcea,97),
        create_node_with_cost(craiova, 138),
        create_node_with_cost(bucharest,101)
    ])
    craiova.add_children([
        create_node_with_cost(pitesti,138),
        create_node_with_cost(rimniicu_vilcea,146),
        create_node_with_cost(drobeta,120)
    ])
    mehadia.add_children([
        create_node_with_cost(lugoj,70),
        create_node_with_cost(drobeta,75)
    ])
    urzieni.add_children([
        create_node_with_cost(hirsova, 98),
        create_node_with_cost(vaslui, 142),
        create_node_with_cost(bucharest, 85)
    ])
    drobeta.add_children([
        create_node_with_cost(mehadia,75),
        create_node_with_cost(craiova,120)
    ])
    hirsova.add_children([
        create_node_with_cost(Node('Eforie'), 86),
        create_node_with_cost(urzieni, 98)
    ])
    vaslui.add_children([
        create_node_with_cost(urzieni,142),
        create_node_with_cost(iasi,92)
    ])
    iasi.add_children([
        create_node_with_cost(vaslui,92),
        create_node_with_cost(Node('Neamt'), 87)
    ])

    return arad

