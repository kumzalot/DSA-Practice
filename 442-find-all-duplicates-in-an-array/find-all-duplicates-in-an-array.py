class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        
        for n in nums:
            index = abs(n)-1
            if nums[index] < 0:
                ans.append(index+1)
            else:
                nums[index] = -1*abs(nums[index])
        return ans