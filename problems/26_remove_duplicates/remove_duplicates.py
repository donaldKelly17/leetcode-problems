from typing import List


class Solution:
    def remove_duplicates(self, nums: List[int]) -> int:
        nums[:] = list(dict.fromkeys(nums))

        return len(nums)
