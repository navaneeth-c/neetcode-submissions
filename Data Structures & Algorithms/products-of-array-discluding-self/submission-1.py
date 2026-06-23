class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # n = len(nums)
        # prefix = [1] * n
        # suffix = [1] * n
        # res = [1] * n

        # prefix[0] = suffix[n-1] = 1

        # for i in range(1, n):
        #     prefix[i] = nums[i-1] * prefix[i-1]
        # for i in range(n-2, -1, -1):
        #     suffix[i] = nums[i+1] * suffix[i+1]
        
        # for i in range(len(nums)):
        #     res[i] =  prefix[i] * suffix[i]
        
        # return res
        
        n = len(nums)
        res = [1] * n

        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
        
        suffix = 1
        for i in range(n-1, -1, -1):
            res[i]*= suffix
            suffix *= nums[i]
        
        return res

      