class Solution(object):
    def trap(self, height):
        l, r = 0, len(height)-1
        left_max, right_max = height[l], height[r]
        water = 0

        while(l<r):
            if left_max<right_max:
                l+=1
                left_max = max(left_max, height[l])
                water += left_max - height[l]
            else:
                r-=1
                right_max = max(right_max, height[r])
                water += right_max - height[r]
        return water