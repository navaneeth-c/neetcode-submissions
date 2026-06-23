class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # worst case time complexity m * n. will not be revisiting nodes if we either mutate or keep a visited (m X n Space)
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        islands = 0
        def dfs(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] != '1' or (r,c) in visited:
                return 
            
            visited.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

            return 
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visited and grid[r][c] == '1': 
                    
                    islands += 1
                    dfs(r,c)
                
        return islands