class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        maxArea = 0
        start = 0
        end = len(heights) - 1

        while start < end:
            area= (end-start) * min(heights[start], heights[end])
            maxArea = max(maxArea, area)

            if heights[start] < heights[end]:
                start+=1
            else:
                end-=1
        return maxArea