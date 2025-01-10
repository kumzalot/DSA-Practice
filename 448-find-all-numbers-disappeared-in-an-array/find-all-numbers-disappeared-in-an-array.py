class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []

        for n in nums:
            index = abs(n)-1
            nums[index] = -1*abs(nums[index])
        
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i+1)
                
        return res