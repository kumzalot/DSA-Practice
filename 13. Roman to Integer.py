class Solution:
    def romanToInt(self, s: str) -> int:
        romVals = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        num = 0
        for i in range(len(s)):
            if i+1 < len(s) and romVals[s[i]] < romVals[s[i+1]]:
                num = num - romVals[s[i]]
            else:
                num = num + romVals[s[i]]
        return num
