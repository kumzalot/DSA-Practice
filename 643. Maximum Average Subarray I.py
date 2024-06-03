class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxAvg = -10000
        tot = 0
        for i in range(k):
            tot += nums[i]
        maxAvg = tot/k
        for i in range(k,len(nums)):
            tot += nums[i]
            tot -= nums[i-k]
            if (tot/k > maxAvg):
                maxAvg = tot/k
        return maxAvg

            
