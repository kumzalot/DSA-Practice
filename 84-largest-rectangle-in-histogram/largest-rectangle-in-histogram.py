class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 1. initialize
        max_area = 0
        stack = [] # [height, index]

        # 2. iterate through input and prepare stack for the final iteration
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][0] > h:
                stack_height, stack_index = stack.pop()
                max_area = max(max_area, stack_height * (i - stack_index))
                start = stack_index
            stack.append([h, start])

        # 3. scan the stack and calculate the max_area for the last time.
        for h, i in stack:
            max_area = max(max_area, h * (len(heights) - i))
        
        return max_area