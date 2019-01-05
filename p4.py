import random

# Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
#
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
#
# You can modify the input array in-place.

#O(n) time and #O(n) space
def first_positive(lst):
    setty = set(lst)
    i = 1
    while i in setty:
        i += 1
    return i

#O(n) time and O(1) space
def first_missing_positive(nums):
    if not nums:
        return 1
    for i, num in enumerate(nums):
        while i + 1 != nums[i] and 0 < nums[i] <= len(nums):
            v = nums[i]
            nums[i], nums[v - 1] = nums[v - 1], nums[i]
            nums[v - 1] = v
            if nums[i] == nums[v - 1]:
                break
    for i, num in enumerate(nums, 1):
        if num != i:
            return i
    return len(nums) + 1

def main():
    lst = []
    n = random.randint(0,15)
    for x in range(n):
        lst.append(random.randint(-10, 10))
    first_missing_positive(lst)

main()