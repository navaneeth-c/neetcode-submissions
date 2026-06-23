class Solution:
    # use set to add values if value does not exist. if a value exist return
    # Complexity: space: O(n) time: o(n)
    def hasDuplicate(self, nums: List[int]) -> bool:
        non_duplicate = set()
        for num in nums: 
            if num not in non_duplicate:
                non_duplicate.add(num)
            else: 
                return True
        return False
        