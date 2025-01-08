class Solution(object):
    def countCompleteSubarrays(self, nums):
        n = len(nums)
        c = len(set(nums))
        
        count = 0

        for i in range(n):
            s = set()

            for j in range(i,n):
                s.add(nums[j])
                if (len(s) == c):
                    count += 1
        return count