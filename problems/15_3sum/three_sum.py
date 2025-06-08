from typing import List


class Solution:
    def three_sum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        elif len(nums) == 3 and sum(nums) == 0:
            return [nums]

        nums.sort()

        triplets: List = []
        n: int = len(nums)
        i: int = 0

        while i < n - 2:
            if nums[1] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue

            left, right = i + 1, n - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum < 0:
                    left += 1
                elif current_sum > 0:
                    right -= 1
                else:
                    triplets.append([nums[i], nums[left], nums[right]])

                    left, right = left + 1, right - 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

            i += 1

        return triplets


if __name__ == "__main__":
    sol = Solution()

    nums = [-1, 0, 1, 2, -1, -4]

    k = sol.three_sum(nums)

    print(k)
