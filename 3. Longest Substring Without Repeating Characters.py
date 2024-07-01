class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        longest = 0
        l = 0
        for r in range(len(s)):
            if s[r] not in seen:
                seen.add(s[r])
                longest = max(longest, r-l + 1)
            else:
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1
                seen.add(s[r])
        return longest
