class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2
        i, j = 0, 0

        curr, prev = 0, 0

        for _ in range(half + 1):
            prev =  curr
            if i < len(nums1) and (j >= len(nums2) or nums1[i] <= nums2[j]):
                curr = nums1[i]
                i += 1
            else: 
                curr = nums2[j]
                j += 1
        
        if total % 2 == 0:
            return (prev+ curr)/2.0
        else:
            return float(curr)