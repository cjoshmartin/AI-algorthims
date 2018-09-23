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

