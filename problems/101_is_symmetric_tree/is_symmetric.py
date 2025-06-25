# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_symmetric(self, root: TreeNode | None) -> bool:
        def is_mirror(node_1: TreeNode, node_2: TreeNode) -> bool:
            if node_1 is None and node_2 is None:
                return True

            if node_1 is None or node_2 is None or node_1.val != node_2.val:
                return False

            return is_mirror(node_1.left, node_2.right) and is_mirror(
                node_1.right, node_2.left
            )

        return is_mirror(root, root)
