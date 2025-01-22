class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #creating and populating prefix and postfix product arrays
        n = len(nums)
        prefix, postfix, res = [1]*n, [1]*n, [1]*n
        
        prod = 1
        for i in range(n):
            prefix[i] = nums[i] * prod
            prod = prefix[i]

        prod = 1
        for j in range(n-1, -1, -1):
            postfix[j] = nums[j] * prod
            prod = postfix[j]
        
        #populating result array
        for i in range(n):
            if i == 0:
                res[i] = 1 * postfix[i+1]
            elif i == (n - 1):
                res[i] = prefix[i-1] * 1
            else:
                res[i] = prefix[i-1] * postfix[i+1]
        return res