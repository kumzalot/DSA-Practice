class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        seen = set()

        for n in nums:
            if n in seen:
                ans.append(n)
            seen.add(n)
        return ans