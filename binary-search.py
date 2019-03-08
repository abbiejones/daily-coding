import sys
import random
import math

MAX = 20

def init_array(n):
    lst = []
    for x in range(n):
        lst.append(random.randint(0,MAX))
    return lst


def merge_sort(lst):
    split = math.floor(len(lst)/2)
    if split < 1:
        return lst
    else:
        left = merge_sort(lst[0:split])
        right = merge_sort(lst[split:])

        new = []
        x = 0
        y = 0
        left_length = len(left)
        right_length = len(right)
        while (x < left_length) & (y < right_length):
            if left[x] < right[y]:
                new.append(left[x])
                x += 1
            else:
                new.append(right[y])
                y += 1

        if x < left_length:
            for i in range(x, left_length):
                new.append(left[i])
        else:
            for j in range(y, right_length):
                new.append(right[j])

        return new


def verify_sorted(lst):
    for x in range(len(lst) - 1):
        if lst[x] > lst[x+1]:
            return False
    return True

def verify_search(lst, n, found):
    if (n in lst) & found:
        return True
    if (n not in lst) & found is False:
        return True
    else:
        return False

def binary_search(lst, n):
    split = math.floor(len(lst) / 2)
    divide = n - lst[split]
    if (split >= 1):
        if divide == 0:
            return True
        elif divide > 0 :
            if binary_search(lst[split:], n): return True
        elif divide < 0:
            if binary_search(lst[0:split], n): return True

    return False

def main():

    listy = []
    for x in range(10):
       listy.append(random.randint(0, MAX))
    sorted = merge_sort(listy)

    if (verify_sorted(sorted) == False):
        print("not sorted")
        exit(1)
    query = random.randint(0, MAX)
    print(sorted)

    found = binary_search(sorted, query)
    if (verify_search(sorted, query, found) == False):
        print("ERROR")
    else:
        print("YAY")


main()