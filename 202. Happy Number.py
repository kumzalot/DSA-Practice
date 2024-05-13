class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n not in seen:
            seen.add(n)
            n = self.sumOfSquares(n)
            if n==1:
                return True
        return False

    def sumOfSquares(self, n: int) -> int:
        tot = 0
        while (n!=0):
            rem = n%10
            rem = rem ** 2
            tot += rem
            n = n//10
        return tot
