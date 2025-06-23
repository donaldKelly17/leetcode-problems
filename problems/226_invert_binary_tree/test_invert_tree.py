import pytest

from invert_tree import Solution

"""
Example 1:

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:

Input: root = [2,1,3]
Output: [2,3,1]

Example 3:

Input: root = []
Output: []

"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_complete_tree(arr: list[int], i: int, n: int) -> TreeNode | None:
    root = None
    if i < n and arr[i] is not None:
        root = TreeNode(arr[i])
        root.left = build_complete_tree(arr, 2 * i + 1, n)
        root.right = build_complete_tree(arr, 2 * i + 2, n)
    return root


class SameTree:
    def is_same_tree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        if p == q:
            return True

        if p is None or q is None or p.val != q.val:
            return False

        return self.is_same_tree(p.left, q.left) and self.is_same_tree(p.right, q.right)


testdata = [
    ([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]),
    ([2, 1, 3], [2, 3, 1]),
    ([], []),
]


@pytest.mark.parametrize("tree_array, output", testdata)
def test_invert_tree(tree_array, output):
    root = build_complete_tree(tree_array, 0, len(tree_array))
    inverted_root = build_complete_tree(output, 0, len(output))

    sol = Solution()
    same_tree = SameTree()

    k = sol.invert_tree(root)

    assert same_tree.is_same_tree(k, inverted_root)
