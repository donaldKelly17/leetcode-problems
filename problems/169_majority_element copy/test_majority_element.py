import pytest

from majority_element import Solution

"""
Example 1:

Input: nums = [3,2,3]
Output: 3

Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

"""

testdata = [
    ([3, 2, 3], 3),
    ([2, 2, 1, 1, 1, 2, 2], 2),
    ([1], 1),
]


@pytest.mark.parametrize("nums, output", testdata)
def test_majority_element(nums, output):
    sol = Solution()
    k = sol.majority_element(nums)

    assert k == output
