from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        """
        LeetCode 2215. Find the Difference of Two Arrays

        TODO: Implement your solution here
        """
        nums1 = set(nums1)
        nums2 = set(nums2)
        return [list(nums1 - nums2), list(nums2 - nums1)]
