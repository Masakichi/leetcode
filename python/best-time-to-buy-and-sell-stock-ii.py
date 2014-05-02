class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        res = 0
        for x in range(len(prices)):
            try:
                if prices[x] <= prices[x+1]:
                    res += prices[x+1]-prices[x]
            except:
                return res
        return res
