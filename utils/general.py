def get_city_name(node):
    return node.value


def calculate_cost(items):
    acc = 0
    for item in items:
        acc = acc + item
    return acc


def start_line_distances():
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