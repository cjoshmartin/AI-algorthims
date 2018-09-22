from queue import Queue

from utils.Node import letterTree, letterGraph


def breath_first_search(goal, node):
    path_queue = Queue()
    has_seen = set()

    path_queue.put(node)
    while not path_queue.empty():
        next_node =path_queue.get()

        if next_node.value == goal:
            return True

        if next_node.value in has_seen:
            continue

        has_seen.add(next_node.value)
        print(next_node.value)
        if next_node.children is None:
            continue

        for child_node in next_node.children:
            path_queue.put(child_node)

    return False



print('Tree:: {}'.format(breath_first_search('G', letterTree())))

graph = letterGraph()
print('Graph:: {}'.format(breath_first_search('K', graph)))

