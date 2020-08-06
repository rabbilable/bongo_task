class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def lca(root, node1, node2):
    """
    [This solution it is a Binary Tree and not a Binary Search Tree
    Here the time complexity is O(n) as the function traverse the tree from bottom up
    Space Complexity is O(n)]

    Args:
        root ([obj]): [passes the node object]
        node1 ([int]): [passes the first node]
        node2 ([int]): [passes the second node]
    """
    if root is None:
        return None

    if root.key == node1 or root.key == node2:
        return root

    left_lca = lca(root.left, node1, node2)
    right_lca = lca(root.right, node1, node2)

    if left_lca and right_lca:
        return root

    return left_lca if left_lca is not None else right_lca


# TEST CASE
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print("LCA(4,6) = ", lca(root, 4, 6).key)
print("LCA(5,2) = ", lca(root, 5, 2).key)
print("LCA(2,3) = ", lca(root, 2, 3).key)
print("LCA(2,8) = ", lca(root, 2, 8).key)
