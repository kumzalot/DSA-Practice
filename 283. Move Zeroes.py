class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        z, nz = 0, 0
        for i in range(len(nums)):
            if (nums[i]==0):
                z = i; nz = z
                while(nums[nz] == 0 and nz!=len(nums)-1):
                    nz += 1
                nums[nz], nums[z] = nums[z], nums[nz]
                
