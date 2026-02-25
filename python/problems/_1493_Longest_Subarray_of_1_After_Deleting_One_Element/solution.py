from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        """
        LeetCode 1493. Longest Subarray of 1 After Deleting One Element

        TODO: Implement your solution here
        """
        length = len(nums)
        left, right = 0, 0
        max_length = 0
        for i in range(length):
            if nums[i] == 0:
                left = i
                right = i
                while left - 1 >= 0 and nums[left-1] == 1:
                    left -= 1
                while right + 1 < length and nums[right+1] == 1:
                    right += 1
                max_length = max(max_length, right-left)
        if max_length == 0 and 1 in nums:
            return length-1
        return max_length
