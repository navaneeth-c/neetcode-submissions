class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, curr_path, total):
            if total == target: 
                res.append(curr_path.copy())
                return 
            elif total > target or i > len(nums) - 1:
                return
            
            curr_path.append(nums[i])

            dfs(i, curr_path, total + nums[i])

            curr_path.pop()
            dfs(i+1, curr_path, total)
    
        dfs(0, [], 0)
        return res