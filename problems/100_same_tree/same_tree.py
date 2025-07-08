# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_same_tree(self, p: TreeNode | None, q: TreeNode | None) -> bool:

        def is_balanced(p, q):
            if not p and not q:
                return True

            if (p and not q) or (not p and q):
                return False

            if p.val != q.val:
                return False

            return is_balanced(p.left, q.left) and is_balanced(p.right, q.right)

        return is_balanced(p, q)
