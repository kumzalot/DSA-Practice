class Solution:
    def sortColors(self, a: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0,0,0]
        for color in a:
            counts[color] += 1
        r,w,b = counts
        a[:r] = [0]*r
        a[r:r+w] = [1]*w
        a[r+w:] = [2]*b
