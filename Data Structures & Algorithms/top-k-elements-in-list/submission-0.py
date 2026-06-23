class Solution:
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     count = {}
    #     bucket = [[] for i in range(len(nums) + 1)]

    #     for num in nums:
    #         count[num]  = 1 + count.get(num, 0)
        
    #     for n, c in count.items():
    #         bucket[c].append(n)

    #     res = []
    #     for i in range (len(bucket) -1, 0, -1):
    #         for n in bucket[i]:
    #             res.append(n)
    #             if len(res) == k:
    #                 return res

    def topKFrequent(self, nums: List[int], k: int) -> list[int]:
        count = {}
        for num in nums: 
            count[num] = 1 + count.get(num, 0)

        heap = []

        for n in count:
            heapq.heappush (heap, [count[n], n])
            if len (heap) > k:
                heapq.heappop(heap)
        
        res = []

        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res
        
