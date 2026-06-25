class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) != len(speed):
            return 0 # invalid input
        

        stack = []
        pairs = zip(position, speed)

        for pos, speed in sorted(pairs, reverse=True):
            time = (target - pos) / speed
            # push elements to stack
            if not stack or time > stack[-1]:
                stack.append(time)
            
        
        return len(stack)
 