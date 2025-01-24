class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'} # O(1) lookup 
        count, max_count = 0, 0

        # inital iteration
        for i in range(k):
            if s[i] in vowels:
                count += 1
        max_count = count
        
        # second iteration till len(s)
        for i in range(k, len(s)):
            if s[i] in vowels:
                count += 1
            if s[i-k] in vowels:
                count -= 1
            max_count = max(max_count, count)

            if max_count == k:
                break
        
        return max_count
