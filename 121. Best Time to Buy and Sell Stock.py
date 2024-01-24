class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        l,r = 0,1
        while r < len(prices):
            if prices[l] < prices[r]:
                prof = prices[r] - prices[l]
                maxProf = max(maxProf, prof)
            else:
                l = r #moving l to a lower price when l>r
            r += 1 #moving r+1 after every iteration
        return maxProf
