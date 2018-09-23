from utils.Node import mapGraphWithCost
from utils.priority_queue import priority_queue


def print_success(startNode, goal, dict):
    dictKey = goal
    output = goal

    while dictKey != startNode.value:
        dictKey = dict[dictKey]
        output = '{} -> {}'.format(dictKey, output)

    return output


def uniform_cost_search(start, goal):
    path_cost = 0
    frontier = priority_queue()
    explored = set()
    path = {}

    frontier.enqueue({'node': start, 'distance': 0, 'cost': 0})

    while frontier.size() > 0:

        current_tuple = frontier.dequeue()
        current = current_tuple['node']
        path_cost = path_cost + current_tuple['distance']
        city = current.value

        if city == goal:
            return print_success(start, goal, path)

        explored.add(city)
        if not current.is_leaf():
            for child in current.children:
                child_city = child['node'].value
                if child not in frontier.queue and child_city not in explored:
                    cost = child['distance'] + path_cost
                    if cost < child['cost']:
                        child['cost'] = cost
                        path[child_city] = city
                    frontier.enqueue(child)

    return 'failure'


for goal in ['Bucharest', 'Neamt', 'JOSH']:
    path = uniform_cost_search(mapGraphWithCost(), goal)
    print(path)
