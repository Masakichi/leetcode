class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        try:
            min_p = prices[0]
        except:
            return 0
        profit = 0
        for x in prices:
            min_p = min(min_p,x)
            profit = max(profit,x-min_p)
        return profit
