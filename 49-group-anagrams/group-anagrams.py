class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 1. populate a hashmap with exisitng characters and values with anagrams.
        word_map = {}
        for s in strs:
            if tuple(sorted(s)) in word_map:
                word_map[tuple(sorted(s))].append(s)
            else:
                word_map[tuple(sorted(s))] = [s]

        res = []
        for v in word_map.values():
            res.append(v)
        
        return res