from typing import List

"""
Version 2: Improved solution using two pointers.

Pointer 1: i
Pointer 2: k

Complexity
Time: O(n)
Space: O(1)
"""


class Solution:
    def remove_duplicates(self, nums: List[int]) -> int:
        k = 1  # pointer 2
        n = len(nums)

        for i in range(1, n):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1

        return k
