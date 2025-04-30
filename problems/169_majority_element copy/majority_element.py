from typing import List


class Solution:
    def majority_element(self, nums: List[int]) -> int:
        n = len(nums)
        freq = {}
        max_cnt = 0
        res = -1

        # Create hash table from the list nums
        for i in range(n):
            freq[nums[i]] = freq.get(nums[i], 0) + 1

        # find the majority element from hash table
        for value, cnt in freq.items():
            if max_cnt < cnt or (cnt == max_cnt and value > res):
                res = value
                max_cnt = cnt

        return res


if __name__ == "__main__":
    arr = [40, 50, 30, 40, 50, 30, 30]
    sol = Solution()

    print(sol.majority_element(arr))
