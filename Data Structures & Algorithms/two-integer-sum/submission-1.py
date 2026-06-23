class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapcounter = {}

        for i in range(len(nums)):
            if (target - nums[i]) in mapcounter:
                return [mapcounter[target-nums[i]], i]
            else: 
                mapcounter[nums[i]] = i
        
        return []