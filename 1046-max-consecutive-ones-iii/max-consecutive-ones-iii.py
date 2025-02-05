class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res, l, changes = 0, 0, 0
        for r in range(len(nums)):
            if nums[r] == 0:
                changes += 1
            while changes > k:
                if nums[l] == 0:
                    changes -= 1
                l += 1
            res = max(res, r-l + 1)
        return res