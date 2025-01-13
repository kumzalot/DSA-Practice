class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(x, n):
            if n == 0: return 1
            if x == 0: return 0

            res = power(x, n//2) # O(log n)
            res = res * res

            if n % 2 == 0: # even
                return res
            else: # odd
                return res * x
        
        ans = power(x, abs(n))

        if n >= 0:
            return ans
        else:
            return 1/ans