import pytest

from is_palindrome import Solution

"""
Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

"""

testdata = [
    ("A man, a plan, a canal: Panama", True),
    ("race a car", False),
    (" ", True),
    ("ab_a", True),
]


@pytest.mark.parametrize("string, output", testdata)
def test_is_palindrome(string, output):
    sol = Solution()
    k = sol.is_palindrome(string)

    assert k == output
