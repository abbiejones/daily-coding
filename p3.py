import random

# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#O(n)
def serialize(root):
    if root is None:
        return "#"

    return "{} {} {}".format(root.val, serialize(root.left),serialize(root.right))

#O(n)
def deserialize(root):
    nodes = iter(root.split())
    return helper(nodes)


#O(n)
def helper(nodes):
    node = next(nodes)
    if node == "#":
        return None
    root = Node(node)
    root.left = helper(nodes)
    root.right = helper(nodes)

    return root


def main():
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(node)).left.left.val == 'left.left'



main()