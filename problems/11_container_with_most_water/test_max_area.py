import pytest

from max_area import Solution

"""
Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
In this case, the max area of water the container can contain is 49.

Example 2:

Input: height = [1,1]
Output: 1

"""

testdata = [([1, 8, 6, 2, 5, 4, 8, 3, 7], 49), ([1, 1], 1), ([8, 7, 2, 1], 7)]


@pytest.mark.parametrize("height, output", testdata)
def test_max_area(height, output):
    sol = Solution()
    k = sol.max_area(height)

    assert k == output
