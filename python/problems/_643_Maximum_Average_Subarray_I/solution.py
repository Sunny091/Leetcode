from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """
        LeetCode 643. Maximum Average Subarray I

        TODO: Implement your solution here
        """
        length = len(nums)
        max_sum = float('-inf')
        current_sum = sum(nums[:k])
        max_sum = max(max_sum, current_sum)
        for i in range(1, length - k + 1):
            current_sum = current_sum - nums[i-1] + nums[i+k-1]
            max_sum = max(max_sum, current_sum)
        return max_sum / k