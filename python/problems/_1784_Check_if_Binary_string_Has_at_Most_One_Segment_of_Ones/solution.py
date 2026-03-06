from typing import List


class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        """
        LeetCode 1784. Check if Binary string Has at Most One Segment of Ones

        TODO: Implement your solution here
        """
        return "01" not in s
