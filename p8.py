

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Tree:

    def __init__(self, root=None):
        self.root = root

def is_unival(root):
    value = root.value
    def unival_helper(root, value):
        if root == None:
            return True
        if root.val == value:
            return unival_helper(root.left) and unival_helper(root.right)
        return False
    unival_helper(root, root.val)


def count_wrapper(root):
    count, _ = count_unival(root)
    return count

def count_unival(root):
    if root == None:
        return 0, True

    left_count, left_uni = count_unival(root.left)
    right_count, right_uni = count_unival(root.right)

    total_count = left_count + right_count

    if left_uni & right_uni:
        if root.left is not None and root.value != root.left.value:
            return total_count, False
        if root.right is not None and root.value != root.right.value:
            return total_count, False
        return total_count + 1, True
    return total_count, False
