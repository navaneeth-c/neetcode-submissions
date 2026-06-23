class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        targetMap = collections.Counter(t)
        windowMap = defaultdict(int)

        need, have = len(targetMap), 0
        res, resLength = [-1, -1], float("infinity")
        l = 0

        for r in range(len(s)):
            #1. add the element to the windowMap and check if need and have met
            windowMap[s[r]]+=1
            if windowMap[s[r]] == targetMap[s[r]]:
                have+=1
                
                #2. Shrink Left
                while need == have: 
                    # compute and store the res variables
                    if r - l + 1 < resLength: 
                        resLength = r - l + 1
                        res = [l, r] 
                    
                    #remove left from the map and move the pointers
                    windowMap[s[l]]-=1
                    
                    
                    # Did the sub string become invalid now
                    if s[l] in targetMap and windowMap[s[l]] < targetMap[s[l]]:
                        have -= 1
                    
                    l+=1
        
        l, r = res
        return s[l:r+1] if resLength != float("infinity") else ""

