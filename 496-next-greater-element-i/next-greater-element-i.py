class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums1)
        index_map = {}
        for i,j in enumerate(nums1):
            index_map[j] = i
        
        stk = []
        for i in range(len(nums2)-1, -1, -1):
            while stk and nums2[stk[-1]] <= nums2[i]:
                stk.pop()
            
            if stk and nums2[i] in index_map:
                res[index_map[nums2[i]]] = nums2[stk[-1]]

            stk.append(i)
        
        return res