"""
An improved solution based on:
    - https://youtu.be/Nxzstmv_U0U?si=Xjh4KN74WhSImG_J
    - https://youtu.be/jJXJ16kPFWg?si=dAuH3qNHTyqOyiiS

First solution:
    Runtime = 9ms  (O(N))
    Memory = 19.3 MB  (O(1))

Improved solution:
    Runtime = 7ms  (O(N))
    Memory = 18.03 MB  (O(1))
"""


class Solution:
    def is_palindrome(self, s: str) -> bool:
        n = len(s)
        x = 0
        y = n - 1

        if n <= 1:
            return True

        while x < y:
            if not s[x].isalnum():
                x += 1
                continue

            if not s[y].isalnum():
                y -= 1
                continue

            if s[x].lower() != s[y].lower():
                return False

            x += 1
            y -= 1

        return True
