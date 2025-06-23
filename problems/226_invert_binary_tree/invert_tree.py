# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invert_tree(self, root: TreeNode | None) -> TreeNode | None:

        if not root:
            return None

        root.left, root.right = root.right, root.left
        self.invert_tree(root.left)
        self.invert_tree(root.right)

        return root


if __name__ == "__main__":

    class SameTree:
        def is_same_tree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
            if p == q:
                return True

            if p is None or q is None or p.val != q.val:
                return False

            return self.is_same_tree(p.left, q.left) and self.is_same_tree(
                p.right, q.right
            )

    def build_complete_tree(arr: list[int], i: int, n: int) -> TreeNode | None:
        root = None
        if i < n and arr[i] is not None:
            root = TreeNode(arr[i])
            root.left = build_complete_tree(arr, 2 * i + 1, n)
            root.right = build_complete_tree(arr, 2 * i + 2, n)
        return root

    tree_array = [4, 2, 7, 1, 3, 6, 9]
    output = [4, 7, 2, 9, 6, 3, 1]

    root = build_complete_tree(tree_array, 0, len(tree_array))
    inverted_root = build_complete_tree(output, 0, len(output))

    sol = Solution()
    same_tree = SameTree()

    k = sol.invert_tree(root)

    is_the_same = same_tree.is_same_tree(k, inverted_root)

    assert is_the_same
