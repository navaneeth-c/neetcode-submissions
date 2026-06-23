class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        map = {
            '}' : '{',
            ']' : '[',
            ')' : '('
        }
        for c in s:
            if c not in map:
                stack.append(c)
            else: 
                newChar = stack.pop() if stack else '#'
                if map[c] != newChar:
                    return False

        return len(stack) == 0