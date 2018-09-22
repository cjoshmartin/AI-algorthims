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


def tree_for_adv_search():
    a1 = Node(infinity, create_leafs([3, 12, 8]))
    a2 = Node(infinity, create_leafs([2, 4, 6]))
    a3 = Node(infinity, create_leafs([14, 5, 2]))
    parent = Node(infinity, [a1, a2, a3])
    print('number of nodes: {}'.format(parent.total()))
    return parent

