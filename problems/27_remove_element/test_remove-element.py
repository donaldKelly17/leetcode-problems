import pytest

from remove_element import Solution

"""
Example 1:

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]

Example 2:

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
"""

testdata = [
    ([3, 2, 2, 3], 3, [2, 2], 2),
    ([0, 1, 2, 2, 3, 0, 4, 2], 2, [0, 1, 3, 0, 4], 5),
]


@pytest.mark.parametrize("nums, val, expected, output", testdata)
def test_merge(nums, val, expected, output):
    sol = Solution()
    k = sol.remove_element(nums, val)

    assert nums == expected
    assert k == output
