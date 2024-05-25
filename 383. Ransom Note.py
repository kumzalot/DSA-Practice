#Quickest Soln
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for c in set(ransomNote):
            if magazine.count(c) < ransomNote.count(c):
                return False
        return True

  ###############################

#Not So Quick Soln
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = {}
        for c in magazine:
            counter[c] = 1 + counter.get(c, 0)
        for l in ransomNote:
            if l not in counter:
                return False
            elif counter[l]==1:
                del counter[l]
            else:
                counter[l] -= 1
        return True
