from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        LeetCode 283. Move Zeroes

        TODO: Implement your solution here
        """
        left = 0
        
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[right], nums[left] = nums[left], nums[right]
            
                left += 1
