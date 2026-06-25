class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = []
        # (temperature, index)

        for idx, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                temp, i = stack.pop()
                res[i] = idx - i
            
            stack.append((t,idx))
        
        return res