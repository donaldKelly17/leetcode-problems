from typing import List

"""
Version 2:  An improved version based on this tutorial:
https://youtu.be/c1B3LZQtZ_s?si=NRph-XvDQuKxXNt3

"""


class Solution:
    def majority_element(self, nums: List[int]) -> int:
        cnt = 0
        res = -1

        for num in nums:
            if cnt == 0:
                res = num

            if res == num:
                cnt += 1
            else:
                cnt -= 1

        return res


if __name__ == "__main__":
    arr = [40, 50, 30, 40, 50, 30, 30]
    sol = Solution()

    print(sol.majority_element(arr))
