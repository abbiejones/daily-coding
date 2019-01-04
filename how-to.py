import heapq
import random

def merge(lists):
    merged_list = []

    heap = [(lst[0], i, 0) for i, lst in enumerate(lists) if lst]
    heapq.heapify(heap)

    while heap:
        val, list_ind, element_ind = heapq.heappop(heap)

        merged_list.append(val)

        if element_ind + 1 < len(lists[list_ind]):
            next_tuple = (lists[list_ind][element_ind + 1],
                          list_ind,
                          element_ind + 1)
            heapq.heappush(heap, next_tuple)
    return merged_list

def main():
    lists = []
    k = random.randint(0,25)
    n = random.randint(0,25)
    for x in range(k):
        single_list = []
        for x in range(n):
            single_list.append(random.randint(0,50))
        single_list.sort()
        lists.append(single_list)

    merged_list = merge(lists)

main()