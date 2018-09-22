from queue import Queue

from utils.Node import letterTree, letterGraph


def breath_first_search(goal, node):
    path_queue = Queue()
    path_queue.put(node)
    return bfs_r(goal, node, path_queue)


def bfs_r(goal, node, path_queue, has_seen=set()):
    print(node.value)
    if goal == node.value:
        return path_queue

    next_node = path_queue.get()
    for child_node in next_node.children:
        if child_node not in has_seen:
            has_seen.add(child_node)
            path_queue.put(child_node)

    if not path_queue.empty():
        bfs_r(goal, next_node, path_queue, has_seen)


print('Tree:: ')
breath_first_search('G', letterTree())

print('Graph:: ')
breath_first_search('G', letterGraph())
