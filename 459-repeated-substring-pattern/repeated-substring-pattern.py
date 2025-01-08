class Solution(object):
    def repeatedSubstringPattern(self, s):
        s1 = s+s
        if s in s1[1:-1]:
            return True
        else:
            return False