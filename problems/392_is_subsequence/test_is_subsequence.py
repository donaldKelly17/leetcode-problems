import pytest

from is_subsequence import Solution

"""
Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false

"""

testdata = [
    ("abc", "ahbgdc", True),
    ("axc", "ahbgdc", False),
    ("", "ahbgdc", True),
    ("abcdefg", "abc", False),
]


@pytest.mark.parametrize("subsequence, text, output", testdata)
def test_is_subsequence(subsequence, text, output):
    sol = Solution()
    k = sol.is_subsequence(subsequence, text)

    assert k == output
