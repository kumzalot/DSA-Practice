class Solution(object):
    def maxFrequencyElements(self, nums):
        count_map = Counter(nums)
        count = 0
        max_frequency = 0
        for val in count_map.values():
            if val==max_frequency:
                count += val
            elif val>max_frequency:
                max_frequency = val
                count = val
        return count
        