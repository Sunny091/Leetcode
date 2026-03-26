from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        """
        LeetCode 724. Find Pivot Index

        TODO: Implement your solution here
        """
        nums_sum = sum(nums)
        left_sum = 0
        for i in range(len(nums)):
            if left_sum == nums_sum - nums[i]:
                return i
            left_sum += nums[i]
            nums_sum -= nums[i]
        return -1