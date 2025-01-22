class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #creating and populating prefix and postfix product arrays
        n = len(nums)
        res = [1] * n
        
        for i in range(1, n):
            res[i] = nums[i-1] * res[i-1]

        post = 1
        for i in range(n-1, -1, -1):
            res[i] *= post
            post *= nums[i] 
        

        return res