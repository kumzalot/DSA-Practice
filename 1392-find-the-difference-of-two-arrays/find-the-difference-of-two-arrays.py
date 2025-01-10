class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans =[[],[]]
        seen1, seen2 = set(), set()

        for n1 in nums1:
            if n1 not in nums2 and n1 not in seen1:
                ans[0].append(n1)
                seen1.add(n1)
        for n2 in nums2:
            if n2 not in nums1 and n2 not in seen2:
                ans[1].append(n2)
                seen2.add(n2)
        return ans