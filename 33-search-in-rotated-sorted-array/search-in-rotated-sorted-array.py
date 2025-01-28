class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right = 0, len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            
            if nums[left] <= nums[mid]: #seeing if sorted
                if nums[left] <= target < nums[mid]: #checking if in left half
                    right = mid - 1
                else: # should be in right half
                    left = mid + 1
            else: # possibly right half is sorted
                if nums[mid] < target <= nums[right]: #checking if in right half
                    left = mid + 1
                else: # should be in left half
                    right = mid - 1
        
        return -1 # target not found