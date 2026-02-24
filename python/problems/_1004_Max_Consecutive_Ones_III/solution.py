from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        LeetCode 1004. Max Consecutive Ones III

        TODO: Implement your solution here
        """
        length = len(nums)
        left = 0
        max_length = 0
        for right in range(length):
            if nums[right] == 0:
                k -= 1
            while k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
            max_length = max(max_length, right - left + 1)
        return max_length
