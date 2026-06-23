class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r: 
            m = (l + r) // 2

            if nums[m] < target: 
                l = m + 1
            elif nums[m] > target: 
                r = m - 1
            else: 
                return m
        
        return -1 
    
    def search(self, nums: List[int], target: int) -> int: 
        return self.binarySearch(0, len(nums)-1, nums, target)
    
    def binarySearch(self, l: int, r: int, nums: list[int], target:int) -> int:
        if l>r: 
            return -1
        m = (l + r) // 2
        if nums[m] == target: 
            return m
        if nums[m]<target: 
            return self.binarySearch(m+1, r, nums, target)
        return self.binarySearch(l, m-1, nums, target)
        