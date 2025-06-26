# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def has_path_sum(self, root: TreeNode | None, target_sum: int) -> bool:
        def find_sum_path(root: TreeNode, running_total: int):
            if root is None:
                return False

            running_total += root.val

            if root.left is None and root.right is None and running_total == target_sum:
                return True

            return find_sum_path(root.left, running_total) or find_sum_path(
                root.right, running_total
            )

        return find_sum_path(root, running_total=0)


if __name__ == "__main__":

    def build_complete_tree(arr: list[int], i: int, n: int) -> TreeNode | None:
        root = None
        if i < n and arr[i] is not None:
            root = TreeNode(arr[i])
            root.left = build_complete_tree(arr, 2 * i + 1, n)
            root.right = build_complete_tree(arr, 2 * i + 2, n)
        return root

    tree_array = [1, 2]
    target_sum = 1
    output = False

    root = build_complete_tree(tree_array, 0, len(tree_array))

    sol = Solution()

    k = sol.has_path_sum(root, target_sum)

    assert k == output
