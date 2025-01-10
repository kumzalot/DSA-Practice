class Solution(object):
    def findPairs(self, nums, k):
        countMap = Counter(nums)
        count = 0
        
        if (k==0):
            for key,v in countMap.items():
                if v>1:
                    count+=1
        else:
            for key in countMap.keys():
                if (key+k in countMap):
                    count += 1
        return count