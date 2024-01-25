class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        countMap = {}
        for i in range(n):
            countMap[nums[i]] = 1 + countMap.get(nums[i],0)
            if countMap.get(nums[i],0) > n//2:
                return nums[i]
