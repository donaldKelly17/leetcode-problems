from typing import List


class Solution:
    def max_profit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        diff = 0
        min_price = prices[0]

        for i in range(n):
            if prices[i] < min_price:
                min_price = prices[i]
            else:
                diff = prices[i] - min_price
                if diff > max_profit:
                    max_profit = diff

        return max_profit


# # This solution passed 150/212 test cases on Leetcode
# # Passed the first three testcases in the test file (test_max_profit)

# class Solution:
#     def max_profit(self, prices: List[int]) -> int:
#         i = 0  # Pointer 1
#         j = len(prices) - 1  # Pointer 2

#         min_price = 10000
#         max_price = 0

#         while i <= j:
#             if prices[i] < min_price:
#                 min_price = prices[i]
#             if prices[j] > max_price:
#                 max_price = prices[j]
#             i += 1
#             j -= 1

#         if max_price > min_price:
#             return max_price - min_price
#         else:
#             return 0
