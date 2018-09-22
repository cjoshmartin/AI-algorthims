infinity = float('inf')


class Node:
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children

    def total(self):
        curr_total = 1

        if self.is_leaf():
            return curr_total

        for child in self.children:
            curr_total = curr_total + child.total()

        return curr_total

    def add_child(self, value):
        self.children.append(Node(value))

    def is_leaf(self):
        return not self.children


def create_leafs(input_list):
    output_list = []

    for num in input_list:
        output_list.append(Node(num))

    return output_list

def letterTree():
    a1 = Node('B', create_leafs(['C','D','E']))
    a2 = Node('F', create_leafs(['G', 'H', 'I']))
    a3 = Node('J', create_leafs(['K', 'L', 'M']))
    parent = Node('A', [a1, a2, a3])
    return parent

def tree_for_adv_search():
    a1 = Node(infinity, create_leafs([3, 12, 8]))
    a2 = Node(infinity, create_leafs([2, 4, 6]))
    a3 = Node(infinity, create_leafs([14, 5, 2]))
    parent = Node(infinity, [a1, a2, a3])
    print('number of nodes: {}'.format(parent.total()))
    return parent
