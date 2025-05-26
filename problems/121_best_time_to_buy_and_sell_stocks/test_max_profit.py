import pytest

from max_profit import Solution

"""
Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

"""

testdata = [
    ([7, 1, 5, 3, 6, 4], 5),
    ([7, 6, 4, 3, 1], 0),
    ([1, 4, 2], 3),
    ([3, 2, 6, 5, 0, 3], 4),
]


@pytest.mark.parametrize("nums, output", testdata)
def test_max_profit(nums, output):
    sol = Solution()
    k = sol.max_profit(nums)

    assert k == output
