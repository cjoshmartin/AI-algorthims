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





