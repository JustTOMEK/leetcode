class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        mini = prices[0]
        for i in range(1, len(prices)):
            if prices[i] - mini > profit:
                profit = prices[i] - mini
            if prices[i] < mini:
                mini = prices[i]
        return profit

