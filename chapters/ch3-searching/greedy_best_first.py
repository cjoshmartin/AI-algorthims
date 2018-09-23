from utils.Graph import mapGraphWithCost
from utils.general import get_city_name
from utils.priority_queue import priority_queue


def success(stack):
    output = ''
    while len(stack) > 0:
        city = stack.pop()
        output = '{} -> {}'.format(city, output)
    return output


def genrate_dict():
    map_dict = {}

    def append_city(city, distance):
        map_dict[city] = distance
    # ideally you would want to fix these based on your goal
    append_city('Arad', 366)
    append_city('Sibiu', 253)
    append_city('Timisoara', 329)
    append_city('Zerind', 374)
    append_city('Fagaras', 176)
    append_city('Oradea', 380)
    append_city('Rimniicu Vilcea', 193)
    append_city('Lugoj', 244)
    append_city('Bucharest', 0)
    append_city('Pitesti', 100)
    append_city('Craiova', 160)
    append_city('Mehadia', 241)
    append_city('Urzieni', 80)
    append_city('Drobeta', 242)
    append_city('Hirsova', 151)
    append_city('Vaslui', 199)
    append_city('Iasi', 226)
    append_city('Eforie', 161)
    append_city('Giurgiu', 77)
    append_city('Neamt', 234)

    return map_dict


def greedy_best_first(start, goal):
    def queue_structure(node, distance):
        return {'node': node, 'distance': distance}

    frontier = priority_queue('distance')
    path = []
    lookup_table = genrate_dict()
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
