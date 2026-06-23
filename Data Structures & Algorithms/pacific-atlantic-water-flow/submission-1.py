class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()
        res = []
        
        def dfs(r, c,visit, prev_heights):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r,c) in visit or heights[r][c] < prev_heights:
                return
            
            visit.add((r, c))
            prev_heights = heights[r][c]
            dfs(r + 1, c, visit, prev_heights)
            dfs(r - 1, c,visit, prev_heights)
            dfs(r, c+1,visit, prev_heights)
            dfs(r, c-1,visit, prev_heights)

        
        # a for loop to create pac set
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS-1, c, atl, heights[ROWS-1][c])
        
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS-1, atl, heights[r][COLS-1])
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r,c])
        
        return res
        
        # a for loop to create atl set

        # then a forloop to just return those who are in both
