import re


class Solution:
    def is_palindrome(self, s: str) -> bool:
        s = re.sub(r"[^a-zA-Z0-9]", "", s)
        s = s.lower()
        x = 0
        y = len(s)

        if y <= 1:
            return True

        while x <= y:
            if s[x] != s[y - 1]:
                return False
            x += 1
            y -= 1

        return True
