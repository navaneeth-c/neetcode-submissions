class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False
        
        fcm = {}
        for c in s:
            if c not in fcm:
                fcm[c] = 0
            fcm[c]+=1
        
        for c in t: 
            if c not in fcm: 
                return False
            else:
                fcm[c]-=1
        
        for val in fcm.values():
            if  val != 0: 
                return False

        return True
