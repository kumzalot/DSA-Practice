class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is smaller
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        l, r = 0, m

        while l <= r:
            # Creating partitions
            partition1 = (l + r) // 2
            partition2 = (m + n + 1) // 2 - partition1 

            # Creating max and min boundaries
            maxL1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            minR1 = float('inf') if partition1 == m else nums1[partition1]

            maxL2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            minR2 = float('inf') if partition2 == n else nums2[partition2]

            # Checking if partitions are satisfied
            if maxL1 <= minR2 and maxL2 <= minR1:
                if (m + n) % 2 == 0:  # Even length
                    return (max(maxL1, maxL2) + min(minR1, minR2)) / 2
                else:  # Odd length
                    return max(maxL1, maxL2)
            elif maxL1 > minR2:
                r = partition1 - 1
            else:
                l = partition1 + 1
