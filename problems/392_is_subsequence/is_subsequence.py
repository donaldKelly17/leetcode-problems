"""
Version 1 solution using two pointers

Complexity
Time: O(n)
Space: O(1)
"""


class Solution:
    def is_subsequence(self, s: str, t: str) -> bool:
        n_s = len(s)
        n_t = len(t)

        if s == "":
            return True
        if n_s > n_t:
            return False

        s_pointer = 0

        for t_pointer in range(n_t):
            if s[s_pointer] == t[t_pointer]:
                if s_pointer == n_s - 1:
                    return True
                s_pointer += 1

        return False
