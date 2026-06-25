class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []

        for idx, height in enumerate(heights):
            start = idx
            while stack and stack[-1][1] > height: 
                i, prevHeight = stack.pop()
                area = (idx - i)*prevHeight
                maxArea = max(maxArea, area)
                start = i
            stack.append((start, height))

        while stack: 
            i, h = stack.pop()
            maxArea = max(maxArea,(len(heights) - i) * h)
        return maxArea

