class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_length = 0
        n = len(nums)
        changes = 0
        l = 0

        for r in range(n):
            if nums[r] == 0:
                changes += 1
            while changes > k:
                if nums[l] == 0:
                    changes -= 1
                l += 1
            length = r-l + 1
            max_length = max(max_length, length) 
        return max_length