class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        count = 0
        pre_sum = 0
        post_sum = 0
        n = len(nums)

        for i in range(n-1):
            pre_sum += nums[i]
            post_sum = 0
            for j in range(i+1, n):
                post_sum += nums[j]
            if (post_sum - pre_sum)%2 == 0:
                count += 1

        return count