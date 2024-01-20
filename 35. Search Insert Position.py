class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0; r = len(nums)-1
        while l<=r:
            x = (l+r)//2
            if target > nums[x]:
                l = x+1
            elif target < nums[x] :
                r = x-1
            else: 
                return x
        return l #in everycase l will be the index pos, if the target is not found in the entire arr.
