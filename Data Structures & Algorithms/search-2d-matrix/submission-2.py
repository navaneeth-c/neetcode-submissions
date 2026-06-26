class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        rows = len(matrix)
        cols = len(matrix[0])

        l, r = 0, (rows * cols) - 1 

        while l <= r: 
            mid = l + ((r - l) // 2)

            mid_val = matrix[mid//cols][mid%cols]           
            if mid_val == target: 
                return True
            
            elif mid_val < target: 
                l = mid + 1
            else: 
                r = mid - 1
        
        return False