from utils.Node import Node, create_leafs, infinity


def letterTree():
    a1 = Node('B', create_leafs(['C', 'D', 'E'], 3), 2)
    a2 = Node('F', create_leafs(['G', 'H', 'I'], 3), 2)
    a3 = Node('J', create_leafs(['K', 'L', 'M'], 3), 2)
    parent = Node('A', [a1, a2, a3], 1)
    return parent

def tree_for_adv_search():
    a1 = Node(infinity, create_leafs([3, 12, 8]))
    a2 = Node(infinity, create_leafs([2, 4, 6]))
    a3 = Node(infinity, create_leafs([14, 5, 2]))
    parent = Node(infinity, [a1, a2, a3])
    print('number of nodes: {}'.format(parent.total()))
    return parent

