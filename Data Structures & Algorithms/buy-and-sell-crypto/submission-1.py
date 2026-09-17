class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximumProfit = 0
        minPriceSoFar = float("inf")
        
        for price in prices:
            minPriceSoFar = min(minPriceSoFar, price)
            maximumProfit = max(maximumProfit, price - minPriceSoFar)
        
        return maximumProfit
