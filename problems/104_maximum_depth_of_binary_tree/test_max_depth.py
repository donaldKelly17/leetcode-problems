import pytest

from max_depth import Solution

"""
Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 3


Example 2:

Input: root = [1,null,2]
Output: 2

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


testdata = [
    ([3, 9, 20, None, None, 15, 7], 3),
    ([1, None, 2], 2),
]


@pytest.mark.parametrize("tree_array, output", testdata)
def test_max_depth(tree_array, output):
    root = build_complete_tree(tree_array, 0, len(tree_array))

    sol = Solution()
    k = sol.max_depth(root)

    assert k == output
