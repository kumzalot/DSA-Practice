class Solution:
    def jump(self, nums: List[int]) -> int:
        steps = 0
        l = 0
        r = 0
        while(r<len(nums)-1):
            longest = 0
            for i in range(l,r+1):
                longest = max(longest, i+nums[i])
            l = r+1
            r = longest
            steps += 1
        return steps
