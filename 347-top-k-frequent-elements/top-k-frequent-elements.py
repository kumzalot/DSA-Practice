class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. populating a count map for the numbers in the input.
        count_map = {}
        for n in nums:
            count_map[n] = count_map.get(n, 0) + 1
        
        # 2. creating a list of lists to store numbers that appear (index) number of times.
        counts = [[] for _ in range(len(nums) + 1)]
        for n,c in count_map.items():
            counts[c].append(n)

        # 3. iterate through the end and return the result
        res = []
        for i in range(len(counts)-1, 0, -1):
            for n in counts[i]:
                res.append(n)
                if len(res) == k:
                    return res