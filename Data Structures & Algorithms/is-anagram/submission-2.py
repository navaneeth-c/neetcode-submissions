class Solution:
    # HMap to count chars and decrease it for string 2
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = defaultdict(int)
        for c in s: 
            count[c] += 1
        for c in t: 
            if count[c] > 0:
                count[c] -= 1
            else: 
                return False
        return True