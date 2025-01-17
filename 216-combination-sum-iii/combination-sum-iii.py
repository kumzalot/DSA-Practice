class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(start, combo, n):
            if len(combo) == k:
                if n == 0:
                    ans.append(combo.copy())
                return
            if len(combo) > k or n < 0:
                return
            for i in range(start, 10):
                combo.append(i)
                backtrack(i + 1, combo, n - i)
                combo.pop()
        ans = []
        backtrack(1, [], n)

        return ans