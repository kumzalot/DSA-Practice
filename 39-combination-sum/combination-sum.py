class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, target, combo):
            if target == 0:
                ans.append(list(combo))
                return
            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    break
                combo.append(candidates[i])
                backtrack(i, target - candidates[i], combo)
                combo.pop()
        candidates.sort()
        ans = []
        backtrack(0, target, [])
        
        return ans