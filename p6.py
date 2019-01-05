

class Node:

    def __init__(self, value, previous=0, after=0):
        self.value = value
        self.both = previous ^ after

    def add(self, after):
        self.both = self.both ^ after

    def next_node(self, previous):
        return self.both ^ previous


class List:
    def __init__(self, value):
        self.root = Node(value)
        self.tail = self.root

    def add(self, value):
        after = Node(value, previous = self.tail, after = 0)
        self.tail.add(after)

    def get(self, index):

        if self.root != None:
            current_index = self.root

            got_it = current_index.next_node(0)

            for i in range(index-2):
                got_it = current_index.next_node(current_index)

            return got_it

