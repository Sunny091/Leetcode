from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        LeetCode 238. Product of Array Except Self

        TODO: Implement your solution here
        """
        length = len(nums)
        total = 1
        count_zero = 0
        for num in nums:
            if num == 0 and count_zero == 1:
                return [0] * length
            elif num == 0:
                count_zero += 1
            else:
                total *= num
        if count_zero == 1:
            answer = [0 if num != 0 else total for num in nums]
        else:
            answer = [total // num for num in nums]
        return answer
