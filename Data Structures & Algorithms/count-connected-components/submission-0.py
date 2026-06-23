class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i : [] for i in range(n)}
        for a, b in edges: 
            adj[a].append(b)
            adj[b].append(a)
        
        visited = set()
        count = 0

        def dfs(i):
            if i in visited: 
                return 
            
            visited.add(i)
            for nei in adj[i]:
                dfs(nei)
        
        for i in range(n):
            if i not in visited: 
                count +=1 
                dfs(i)
            
        
        return count
