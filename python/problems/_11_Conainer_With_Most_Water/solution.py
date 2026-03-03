from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        LeetCode 11. Conainer With Most Water

        TODO: Implement your solution here
        """

        left = 0
        right = len(height) - 1
        max_result = 0

        while right > left:
            temp = (right - left) * min(height[left], height[right])
            max_result = max(max_result, temp)

            if height[right] > height[left]:
                now = height[left]
                while left < right and height[left] <= now:
                    left += 1

            elif height[right] < height[left]:
                now = height[right]
                while left < right and height[right] <= now:
                    right -= 1

            else:
                right -= 1
                left += 1

        return max_result
