from typing import List


class Solution:
    def minOperations(self, s: str) -> int:
        """
        LeetCode 1758. Minimum Changes To Make Alternation Binary String
        """
        count = 0
        n = len(s)
        for i in range(n):
            count += int(s[i]) != i % 2

        return min(count, n - count)
