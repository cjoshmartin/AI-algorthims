from utils.Node import mapGraphWithCost
from utils.priority_queue import priority_queue


def print_success(startNode, goal, dict):
    dictKey = goal
    output = goal

    while dictKey != startNode.value:
        dictKey = dict[dictKey]
        output = '{} -> {}'.format(dictKey, output)

    return output


def __get_city_name(node):
    return node.value


def calculate_cost(acc, item):
    return acc + item


def uniform_cost_search(start, goal):
    path_cost = 0
    frontier = priority_queue()
    explored = set()
    path = {}

    frontier.enqueue({'node': start, 'distance': 0, 'cost': 0})

    while frontier.size() > 0:

        current_object = frontier.dequeue()
        current = current_object['node']
        path_cost = calculate_cost(path_cost, current_object['distance'])
        city = __get_city_name(current)

        if city == goal:
            return print_success(start, goal, path)

        explored.add(city)
        if not current.is_leaf():
            for child in current.children:
                child_city = __get_city_name(child['node'])
                if child not in frontier.queue and child_city not in explored:
                    cost = calculate_cost(path_cost, child['distance'])
                    if cost < child['cost']:
                        child['cost'] = cost
                        path[child_city] = city
                    frontier.enqueue(child)

    return 'failure'


for goal in ['Bucharest', 'Neamt', 'JOSH']:
    path = uniform_cost_search(mapGraphWithCost(), goal)
    print(path)
