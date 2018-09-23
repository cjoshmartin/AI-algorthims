import queue

from utils.Node import mapGraphWithCost


def uniform_cost_search(start, goal):
    path_cost = 0
    frontier = queue.PriorityQueue()
    explored = set()

    frontier.put((0, start))

    while True:
        if frontier.empty():
            return 'failure'
        current_tuple = frontier.get()
        current = current_tuple[1]
        path_cost = path_cost + current_tuple[0]
        city = current.value
        # city = start == current if  else current.value

        if city == goal:
            return True

        explored.add(city)

        for child in current.children:
            child_city = child[1].value
            if child not in frontier.queue or child_city not in explored:
                frontier.put(child)



map_with_cost = mapGraphWithCost()
uniform_cost_search(map_with_cost, 'Bucharest')
