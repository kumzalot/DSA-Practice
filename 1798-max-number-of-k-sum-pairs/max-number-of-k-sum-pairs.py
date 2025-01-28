class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        countMap = {}
        count = 0
        for i in nums:
            countMap[i] = 1 + countMap.get(i, 0)
        for j in countMap:
            if (countMap[j] !=0 and (k-j) in countMap):
                if (j != (k-j)):
                    count += min(countMap[j], countMap[k-j])
                    countMap[j] = 0
                    countMap[k-j] = 0
                else:
                    count += (countMap[j]//2)
                    countMap[k-j] = 0
        return count
                