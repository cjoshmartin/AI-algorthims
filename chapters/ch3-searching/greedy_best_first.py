from utils.Graph import mapGraphWithCost
from utils.general import get_city_name, start_line_distances
from utils.priority_queue import priority_queue


def success(stack):
    output = ''
    while len(stack) > 0:
        city = stack.pop()
        output = '{} -> {}'.format(city, output)
    return output


def greedy_best_first(start, goal):
    def queue_structure(node, distance):
        return {'node': node, 'distance': distance}

    frontier = priority_queue('distance')
    path = []
    lookup_table = start_line_distances()
    frontier.enqueue(queue_structure(start, lookup_table[get_city_name(start)]))

    while frontier.size() > 0:
        current_object = frontier.dequeue()
        current = current_object['node']
        city = get_city_name(current)

        path.append(city)

        if city == goal:
            return success(path)

        if not current.is_leaf():
            for child in current.children:
                child['distance'] = lookup_table[city]
                frontier.enqueue(child)

    return 'Failure'


graph = mapGraphWithCost()
path = greedy_best_first(graph, 'Bucharest')
print(path)
