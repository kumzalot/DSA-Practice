class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest = 0
        altitudes = [0] * (len(gain) + 1)
        for i in range(1, len(altitudes)):
            altitudes[i] = altitudes[i-1] + gain[i-1]
            highest = max(highest, altitudes[i])
        return highest