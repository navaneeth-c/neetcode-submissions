class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSet = set(nums)
        longest = 0

        for n in nums:
            if n-1 not in numSet:
                currentLength = 1

                while (n + currentLength) in numSet:
                    currentLength += 1
                
                longest = max (currentLength, longest)
        return longest
             
