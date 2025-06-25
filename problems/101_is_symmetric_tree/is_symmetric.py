# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_symmetric(self, root: TreeNode | None) -> bool:
        def is_mirror(node1: TreeNode, node2: TreeNode) -> bool:
            # Both nodes are None, meaning both subtrees are empty, thus symmetric
            if node1 is None and node2 is None:
                return True

            # If only one of the nodes is None or if the values don't match, the subtrees aren't mirrors
            if node1 is None or node2 is None or node1.val != node2.val:
                return False

            # Check the outer and inner pairs of subtrees
            return is_mirror(node1.left, node2.right) and is_mirror(
                node1.right, node2.left
            )

        # Start the recursion with root as both parameters, as the check is for the tree with itself
        return is_mirror(root, root)
