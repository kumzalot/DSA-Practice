class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0; curVal = 0.1 

        for i in range(len(nums)):
            if nums[i] != curVal:
                nums[k] = nums[i]
                k += 1
                curVal = nums[i]
        return k