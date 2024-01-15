class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        op = [] #creating output array
        l = len(nums)
        for i in range(l-1):
            for j in range(i+1,l):
                if nums[i] + nums[j] == target:
                    op.append(i)
                    op.append(j)
                    break
        return op
