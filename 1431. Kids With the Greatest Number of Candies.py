class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m = max(candies)
        resArr = []
        for i in range(len(candies)):
            if candies[i] + extraCandies >= m:
                resArr.append(True)
            else:
                resArr.append(False)
        return resArr
