# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_same_tree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        if p == q:
            return True

        if p is None or q is None or p.val != q.val:
            return False

        return self.is_same_tree(p.left, q.left) and self.is_same_tree(p.right, q.right)
