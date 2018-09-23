import queue

from utils.Node import mapGraphWithCost


class priority_queue:
    def __init__(self, priority='cost'):
        self.queue = []
        self.__size = 0
        self.priority = priority

    def __sorting_agl(self, item):
        return item[self.priority]

    def __sort(self):
        self.queue.sort(key=self.__sorting_agl)

    def __change_size(self, beta):
        new_size = self.__size + beta
        if new_size < 0:
            raise Exception('Can not have a size less then 0')
        self.__size = new_size

    def __get(self):
        item = self.queue[0]
        del self.queue[0]
        return item

    def size(self):
        return self.__size

    def enqueue(self, item):
        self.queue.append(item)
        self.__change_size(1)
        self.__sort()

    def dequeue(self):
        item = self.__get()
        self.__change_size(-1)
        self.__sort()
        return item


def uniform_cost_search(start, goal):
    path_cost = 0
    frontier = priority_queue()
    explored = set()

    frontier.enqueue({'node': start, 'distance': 0, 'cost': 0})

    while frontier.size() > 0:

        current_tuple = frontier.dequeue()
        current = current_tuple['node']
        path_cost = path_cost + current_tuple['distance']
        city = current.value
        print(city)
        if city == goal:
            return explored

        explored.add(city)

        for child in current.children:
            child_city = child['node'].value
            if child not in frontier.queue and child_city not in explored:
                cost = child['distance'] + path_cost
                # if  cost < child['cost']:
                child['cost'] = cost
                child['via'] = city
                frontier.enqueue(child)

    return 'failure'


map_with_cost = mapGraphWithCost()
tacos = uniform_cost_search(map_with_cost, 'Bucharest')
tacos
