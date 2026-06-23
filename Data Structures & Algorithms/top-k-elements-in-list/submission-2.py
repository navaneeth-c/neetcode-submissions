class Solution:
    # frequency counter map: space: O(n), time: O(nlogn) to sort the map values and return k top or bottom
    # use priority queue. heap size always k. at the end return all values of heap to res. 

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        
        heap = []
        
        for num in count.keys():
            heapq.heappush(heap, (count[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
            
        res = []
        for i in range(len(heap)):
            res.append(heapq.heappop(heap)[1])
        return res
        