class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        counts = Counter()
        res = []

        for i in range(1, n+1):
            counts[i] = 1
        
        for n in nums:
            if n in counts:
                counts[n] = 0
        
        for key,val in counts.items():
            if val!=0:
                res.append(key)
                
        return res