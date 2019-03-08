import math
import operator
from collections import defaultdict
# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.
#
# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.
#
# Follow-up: Can you do this in O(N) time and constant space?

'''
largest it can be: math.ceil(len(list))

sum the entire list and subtract values until you get to a value where none of the array values are touching
'''


#rough draft
def max_no_touching(lst):
    lst_sum = sum(lst)
    index_value = defaultdict(int)
    max_counter = lst_sum - sum(index_value.values())
    max_length = math.ceil(len(lst)/2)


    for x in range(len(lst) - max_length):
        min_value = min(lst)
        min_index = lst.index(min(lst))
        index_value[min_index] = min_value


def max_n_not_touching(lst):
    n = lst.length / 3

    max_lists = []
    for x in range(0, n):
        max_lists.append(max_three_not_touching(lst, (x*3) + 0, (x*3) + 1, (x*3) + 2))


#max of any three
def max_three_not_touching(lst, a, b, c):
    possibilities = {a:lst[a], b: lst[b], c: lst[c], -1: lst[a] + lst[c]}
    return sorted(possibilities.items(), key=operator.itemgetter(1))

#O(2^n) provided solution
def largest_non_adjacent_2n(arr):
    if not arr:
        return 0

    return max(
            largest_non_adjacent_2n(arr[1:]),
            arr[0] + largest_non_adjacent_2n(arr[2:]))

def largest_non_adjacent_n(arr):
    if len(arr) <= 2:
        return max(0, max(arr))

    cache = [0 for i in arr]
    cache[0] = max(0, arr[0])
    cache[1] = max(cache[0], arr[1])

    for i in range(2, len(arr)):
        num = arr[i]
        cache[i] = max(num + cache[i - 2], cache[i - 1])
    return cache[-1]


def largest_non_adjacent_constant(arr):
    if len(arr) <= 2:
        return max(0, max(arr))

    max_excluding_last= max(0, arr[0])
    max_including_last = max(max_excluding_last, arr[1])

    for num in arr[2:]:
        prev_max_including_last = max_including_last

        max_including_last = max(max_including_last, max_excluding_last + num)
        max_excluding_last = prev_max_including_last

    return max(max_including_last, max_excluding_last)

def main():
    lst = [2,4,6,2,5]

    max_no_touching(lst)