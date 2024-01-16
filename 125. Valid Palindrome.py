class Solution:
    def isPalindrome(self, s: str) -> bool:

        l,r = 0, len(s)-1 
        while l<r:
            while l<r and not self.isANum(s[l]): #checking for non alphanum characters.
                l += 1
            while l<r and not self.isANum(s[r]): #checking for non alphanum characters.
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l,r = l+1, r-1
        return True

    def isANum(self, c): #ord returns the ASCII value of a character.
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
