class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [] # letter and count
        for c in s:
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1
            else:
                stack.append([c, 1])
            
            if stack[-1][1] == k:
                stack.pop()

        res = ""
        for letter, count in stack:
            res += (letter * count)
        return res