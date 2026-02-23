from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        LeetCode 283. Move Zeroes

        TODO: Implement your solution here
        """
        for i in nums:
            if i == 0:
                nums.remove(i)
                nums.append(0)
