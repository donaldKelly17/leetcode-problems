from typing import List


class Solution:
    def two_sum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        if right == 1:
            return [1, 2]

        while left < right:
            current_total = numbers[left] + numbers[right]

            if current_total == target:
                return [left + 1, right + 1]
            elif current_total < target:
                left += 1
            else:
                right -= 1
