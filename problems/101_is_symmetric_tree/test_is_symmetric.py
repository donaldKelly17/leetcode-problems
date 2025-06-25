import pytest

from is_symmetric import Solution

"""
Example 1:

Input: root = [1,2,2,3,4,4,3]
Output: true


Example 2:

Input: root = [1,2,2,null,3,null,3]
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
    ([1, 2, 2, 3, 4, 4, 3], True),
    ([1, 2, 2, None, 3, None, 3], False),
]


@pytest.mark.parametrize("root, output", testdata)
def test_max_depth(root, output):
    root = build_complete_tree(root, 0, len(root))

    sol = Solution()
    k = sol.is_symmetric(root)

    assert k == output
