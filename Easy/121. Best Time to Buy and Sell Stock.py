from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        min_price = prices[0]
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)
        
        return max_profit


solution = Solution()

prices = [7,1,5,3,6,4]
print(solution.maxProfit(prices = prices))

prices = [7,6,4,3,1]
print(solution.maxProfit(prices = prices))

prices = [2,4,1]
print(solution.maxProfit(prices = prices))


# Attempt 1
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        list_len = len(prices)

        for i in range(list_len):
            if i != list_len-1:
            
                for j in range(i+1, list_len):
                    if prices[i] < prices[j] and (price_difference := prices[j] - prices[i]) > profit:
                        profit = price_difference
        return profit

"""