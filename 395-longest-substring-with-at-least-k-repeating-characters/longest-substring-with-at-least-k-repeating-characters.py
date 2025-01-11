class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        n = len(s)
        if n < k: return 0
        counts = Counter(s)
        results = []
        for char, freq in counts.items():
            if freq < k:
                substrings = s.split(char)
                for sub in substrings:
                    result = self.longestSubstring(sub, k)
                    results.append(result)
                return max(results)
        return len(s)
