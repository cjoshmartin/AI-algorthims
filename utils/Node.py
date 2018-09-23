infinity = float('inf')


class Node:
    def __init__(self, value, children = None, depth=None):
        self.value = value
        self.children = children
        self.depth = depth

    def total(self, has_seen=set()):

        curr_total = 1

        if self.is_leaf():
            return curr_total

        for child in self.children:

            if child not in has_seen:
                has_seen.add(child)
                curr_total = curr_total + child.total(has_seen)

        return curr_total

    def add_child(self, child, depth= None):
        if self.children is None:
            self.children = [child]
            self.depth =depth
        else:
            self.children.append(child)

    def add_child_by_value(self, value):
        self.children.add_child(Node(value))

    def add_children(self, list_of_children):
        for child in list_of_children:
            self.add_child(child)

    def is_leaf(self):
        return self.children is None


def create_leafs(input_list, depth = None):
    output_list = []

    for num in input_list:
        output_list.append(Node(num, None, depth))

    return output_list


def letterTree():
    a1 = Node('B', create_leafs(['C', 'D', 'E'], 3), 2)
    a2 = Node('F', create_leafs(['G', 'H', 'I'], 3), 2)
    a3 = Node('J', create_leafs(['K', 'L', 'M'], 3), 2)
    parent = Node('A', [a1, a2, a3], 1)
    return parent


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

def tree_for_adv_search():
    a1 = Node(infinity, create_leafs([3, 12, 8]))
    a2 = Node(infinity, create_leafs([2, 4, 6]))
    a3 = Node(infinity, create_leafs([14, 5, 2]))
    parent = Node(infinity, [a1, a2, a3])
    print('number of nodes: {}'.format(parent.total()))
    return parent

