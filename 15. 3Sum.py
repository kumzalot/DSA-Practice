class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        op = []
        for i,a in enumerate(nums):
            if i>0 and a==nums[i-1]: #skipping for same values
                continue
            l,r = i+1, len(nums) - 1
            while l<r:
                tot = a + nums[l] + nums[r]
                if tot < 0:
                    l+=1
                elif tot > 0:
                    r-=1
                else:
                    op.append([a,nums[l],nums[r]])
                    l += 1
                    while nums[l]==nums[l-1] and l<r:
                        l += 1 #to avoid duplicate triplets
        return op
