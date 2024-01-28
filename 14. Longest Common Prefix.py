class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]: #outOfBounds check and char comparison
                    return pre
            pre += strs[0][i] #char found in all strings
        return pre
