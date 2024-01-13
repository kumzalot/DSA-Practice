class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0; r = len(nums)-1 #declaring left and right pointers

        while(l <= r): #detects end of search
            m = (l+r) // 2
            
            if target > nums[m]:
                l = m+1
            elif target < nums[m]:
                r = m-1
            else:
                return m
        return -1
