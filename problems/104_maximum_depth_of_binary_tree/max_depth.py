class Solution:
    def max_depth(self, root):
        if not root:
            return 0

        left = self.max_depth(root.left)
        right = self.max_depth(root.right)

        return 1 + max(left, right)
