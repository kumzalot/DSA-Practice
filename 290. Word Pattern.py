class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        wordMap = {}
        words = s.split()
        if len(pattern) != len(words):
            return False
        if len(set(pattern)) != len(set(words)):
            return False    
        for i in range(len(words)):
            if words[i] not in wordMap:
                wordMap[words[i]] = pattern[i]
            elif wordMap[words[i]] != pattern[i]:
                return False
        return True
