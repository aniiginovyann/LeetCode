# Median of Two Sorted Arrays

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums = sorted(nums)
        
        if len(nums) % 2 == 0:
           return (nums[len(nums)//2] + nums[len(nums)//2 - 1])/2
        else:
           return nums[len(nums)//2]
    
obj = Solution()
print(obj.findMedianSortedArrays([1, 3, 4], [2, 5, 6]))
