from typing import List


class Solution:
    def max_area(self, height: List[int]) -> int:
        left_pointer: int = 0
        right_pointer: int = len(height) - 1
        max_volume: int = 0
        current_volume: int = 0

        while left_pointer < right_pointer:
            min_height = min(height[left_pointer], height[right_pointer])
            diff = right_pointer - left_pointer
            current_volume = min_height * diff
            max_volume = max(max_volume, current_volume)

            if height[left_pointer] < height[right_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1

        return max_volume
