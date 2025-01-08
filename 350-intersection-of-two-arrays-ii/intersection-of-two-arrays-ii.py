class Solution(object):
    def intersect(self, nums1, nums2):
        res = []
        count_map1 = Counter(nums1) 
        count_map2 = Counter(nums2)

        for key in count_map1:
            if key in count_map2:
                freq = min(count_map1[key],count_map2[key])
                for _ in range(freq):
                    res.append(key)
        return res