class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_count = {}
        res = 0
        l = 0
        for r in range(len(s)):
            char_count[s[r]] = 1 + char_count.get(s[r], 0)

            if  (r-l+1) - max(char_count.values()) <= k:
                res = max(res, r-l+1)
                r += 1
            else:
                char_count[s[l]] -= 1
                l += 1
        return res