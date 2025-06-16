import pytest

from same_tree import Solution

"""
Example 1:

Input: p = [1,2,3], q = [1,2,3]
Output: true


Example 2:

Input: p = [1,2], q = [1,null,2]
Output: false


Example 3:

Input: p = [1,2,1], q = [1,1,2]
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
    ([1, 2, 3], [1, 2, 3], True),
    ([1, 2], [1, None, 2], False),
    ([1, 2, 1], [1, 1, 2], False),
    ([None], [None], True),
    ([None], [1], False),
    ([1], [2], False),
]


@pytest.mark.parametrize("p, q, output", testdata)
def test_max_depth(p, q, output):
    p_root = build_complete_tree(p, 0, len(p))
    q_root = build_complete_tree(q, 0, len(q))

    sol = Solution()
    k = sol.is_same_tree(p_root, q_root)

    assert k == output
