class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, combo, target):
            if target == 0:
                ans.append(list(combo))
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] > target:
                    break
                combo.append(candidates[i])
                backtrack(i+1, combo, target - candidates[i])
                combo.pop()
        candidates.sort()
        ans = []
        backtrack(0, [], target)
        return ans