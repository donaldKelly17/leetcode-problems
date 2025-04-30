from typing import List

"""
Version 2: Improved solution using two pointers.

Complexity
Time: O(n)
Space: O(1)
"""


class Solution:
    def remove_element(self, nums: List[int], val: int) -> int:
        i = 0
        k = len(nums)

        while i < k:
            if nums[i] == val:
                nums[i] = nums[k - 1]
                k -= 1
            else:
                i += 1

        return k
