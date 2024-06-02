class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        hashmap = {}
        count = 0
        for i in nums:
            hashmap[i] = 1 + hashmap.get(i, 0)
        seen = set()

        for n in hashmap:
            if n not in seen and (k-n) in hashmap:
                if n == (k-n):
                    count += hashmap[n]//2
                else:
                    count += min(hashmap[n], hashmap[k-n])
                seen.add(n)
                seen.add(k-n)
        return count
