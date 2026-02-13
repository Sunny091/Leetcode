from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        """
        LeetCode 334. Increasing Triplet Subsequence

        TODO: Implement your solution here
        """
        if len(nums) < 3:
            return False

        first = second = float('inf')

        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True

        return False
