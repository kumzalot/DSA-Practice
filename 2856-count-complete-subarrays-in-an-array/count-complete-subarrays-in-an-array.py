class Solution(object):
    def countCompleteSubarrays(self, nums):
        count = 0
        distinct = len(set(nums))
        
        for i in range(len(nums)):
            s = set()
            for j in range(i, len(nums)):
                s.add(nums[j])
                if (len(s)==distinct):
                    count += 1
        return count