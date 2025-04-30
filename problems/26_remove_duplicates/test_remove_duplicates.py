import pytest

from remove_duplicates import Solution

"""
Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]

Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
"""

testdata = [
    ([1, 1, 2], 2),
    ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5),
]


@pytest.mark.parametrize("nums, output", testdata)
def test_merge(nums, output):
    sol = Solution()
    k = sol.remove_duplicates(nums)

    assert k == output
    assert len(nums) == len(set(nums))
