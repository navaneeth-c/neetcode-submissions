class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        max_pile = 0
        for p in piles: 
            max_pile = max(max_pile, p)
        min_speed = max_pile
        l, r = 1, max_pile

        while l <= r: 
            mid = l + ((r - l)//2)
            time_taken = 0
            for p in piles: 
                time_taken += p//mid 
                if p % mid != 0:
                    time_taken+=1
            
            
            if time_taken > h: 
                l = mid + 1
            else: 
                r = mid - 1
                min_speed = min(min_speed, mid)
        
        return min_speed