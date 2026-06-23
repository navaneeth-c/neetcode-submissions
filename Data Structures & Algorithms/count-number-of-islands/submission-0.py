class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid: 
            return 0
        
        rows, cols = len(grid), len(grid[0])

        directions = [(1,0),(-1,0), (0,1), (0,-1)]
        isIsland = 0
        visited = set()

        def dfs(r, c):
            if not (r >= 0 and r < rows and c >= 0 and c < cols and grid[r][c] == '1' and (r,c) not in visited):
                return 
            
            visited.add((r,c))

            for dr, dc in directions: 
                dfs(r+dr, c+dc)
        

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    isIsland += 1
                    dfs(r, c)
        
        return isIsland