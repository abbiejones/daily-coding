# You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, with the following API:
#
# record(order_id): adds the order_id to the log
# get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
# You should be as efficient with time and space as possible.

# class Node:
#     def __init__(self, order_id=0, previous=None, next=None):
#         self.order_id = order_id
#         self.previous = previous
#         self.next = next
#
# class Linked_List:
#     def __init__(self, root=None):
#         self.root=root
#         self.tail=root
#
# def record(order_id):
#
#     return
#
#
# def get_last(i):
#     return
#
#
# def main():
#
#
# main()
import random

class Log(object):
    def __init__(self, n):
        self.n = n
        self._log = []
        self._cur = 0

    def record(self, order_id):
        if len(self._log) == self.n:
            self._log[self._cur] = order_id
        else:
            self._log.append(order_id)
        self._cur = (self._cur + 1) % self.n

    def get_last(self, i):
        return self._log[self._cur - i]

def reverse_sentence(sentence):
    sentence_list = sentence.split(' ')
    sentence_list = sentence_list[::-1]
    sentence = ' '.join(list(sentence_list))
    return sentence

def main():
    orders = [random.randint(0,20) for x in range(10)]

    # loggy = Log(5)
    #
    # for i in range(len(orders)):
    #     loggy.record(orders[i])
    #     loggy.get_last(1)

    print(reverse_sentence("this is a fun coding assignment"))
main()
