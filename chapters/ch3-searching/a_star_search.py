from utils.Graph import mapGraphWithCost
from utils.general import get_city_name, start_line_distances, calculate_cost
from utils.priority_queue import priority_queue

def success(startNode, goal, dict):
    dictKey = goal
    output = goal

    while dictKey != startNode.value:
        dictKey = dict[dictKey]
        output = '{} -> {}'.format(dictKey, output)

    return output


def a_star_search(start, goal):
    frontier = priority_queue()
    possiable_moves = {}
    lookup_table = start_line_distances()
    explored = set()
    path_cost = 0
    frontier.enqueue({'node': start, 'distance': 0, 'cost': lookup_table[get_city_name(start)]})

    while frontier.size() > 0:

        current_object = frontier.dequeue()
        current = current_object['node']
        city = get_city_name(current)
        path_cost = calculate_cost([path_cost, current_object['distance'], lookup_table[city]])


        if city == goal :
            return success(start,goal, possiable_moves)

        explored.add(city)
        if not current.is_leaf():
            for child in current.children:
                child_city = get_city_name(child['node'])
                if child not in frontier.queue and child_city not in explored:
                    cost = calculate_cost([path_cost, child['distance'], lookup_table[city]])
                    if cost < child['cost']:
                        child['cost'] = cost
                        possiable_moves[child_city] = city
                    frontier.enqueue(child)

    return 'Failure'

goal = 'Bucharest'
path = a_star_search(mapGraphWithCost(), goal)
print(path)