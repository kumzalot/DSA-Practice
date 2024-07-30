class Solution:
    def climbStairs(self, n: int) -> int:
        arr = [0]*(n+1)
        if n<=1:
            return n
        else:
            arr[1], arr[2] = 1, 2
            for i in range(3,n+1):
                arr[i] = arr[i-2] + arr[i-1]
            return arr[-1]
