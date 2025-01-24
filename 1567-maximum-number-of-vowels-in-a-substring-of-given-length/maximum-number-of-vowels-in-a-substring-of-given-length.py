class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        vowels = {'a', 'e', 'i', 'o', 'u'}
        count, max_count = 0, 0
        l = 0

        for r in range(n):
            if (r-l + 1) > k: # ensures window of k length 
                if s[l] in vowels:
                    count -= 1
                l += 1
            if s[r] in vowels: # tracks last seen vowel
               count += 1
            if max_count == k: # reduces iterations after count == k
                break
            max_count = max(max_count, count)
        
        return max_count