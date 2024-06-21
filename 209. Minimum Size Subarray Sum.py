class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, total = 0,0
        output = len(nums) + 1
        r = 0
        while (r<len(nums)):
            total += nums[r]
            while (total >= target):
                output = min(output,(r-l+1))
                total -= nums[l]
                l += 1
            r+=1
        return 0 if output == len(nums) + 1 else output
