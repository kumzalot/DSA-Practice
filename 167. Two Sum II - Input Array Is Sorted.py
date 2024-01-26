class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = 0; r = len(nums)-1
        while l<r:
            tot = nums[l] + nums[r]

            if tot > target:
                r -= 1
            elif tot < target:
                l += 1
            else:
                res = [l+1,r+1]
                return res
