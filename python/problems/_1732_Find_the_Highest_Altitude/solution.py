from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        """
        LeetCode 1732. Find the Highest Altitude

        TODO: Implement your solution here
        """
        max = 0
        temp = 0
        for i in gain:
            temp += i
            if temp > max:
                max = temp
        return max
