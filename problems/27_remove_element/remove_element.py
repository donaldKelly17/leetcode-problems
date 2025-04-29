from typing import List


class Solution:
    def remove_element(self, nums: List[int], val: int) -> int:
        """ """
        nums[:] = [i for i in nums if i != val]

        k = len(nums)

        return k
