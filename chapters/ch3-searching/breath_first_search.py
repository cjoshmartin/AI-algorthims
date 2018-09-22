from queue import Queue

from utils.Node import letterTree, letterGraph


def breath_first_search(goal, node):
    path_queue = Queue()
    path_queue.put(node)
    return bfs_r(goal, node, path_queue, set())


def bfs_r(goal, node, path_queue, has_seen):
    print(node.value)
    if node.value not in has_seen:
        has_seen.add(node.value)

    if goal == node.value:
        return path_queue

    next_node = path_queue.get()
    if not next_node.is_leaf():
        for child_node in next_node.children:
            if child_node.value not in has_seen:
                has_seen.add(child_node.value)
                path_queue.put(child_node)

    if not path_queue.empty():
        bfs_r(goal, next_node, path_queue, has_seen)

    return None

print('Tree:: ')
breath_first_search('G', letterTree())

print('Graph:: ')
graph = letterGraph()
tacos= breath_first_search('F', graph)
tacos