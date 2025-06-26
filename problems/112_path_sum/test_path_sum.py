import pytest

from path_sum import Solution

"""
Example 1:

Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true

Example 2:

Input: root = [1,2,3], targetSum = 5
Output: false

Example 3:

Input: root = [], targetSum = 0
Output: false

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
    ([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], 22, True),
    ([1, 2, 3], 5, False),
    ([], 0, False),
    ([1, 2], 1, False),
]


@pytest.mark.parametrize("tree_array, target_sum, output", testdata)
def test_max_depth(tree_array, target_sum, output):
    root = build_complete_tree(tree_array, 0, len(tree_array))

    sol = Solution()
    k = sol.has_path_sum(root, target_sum)

    assert k == output
