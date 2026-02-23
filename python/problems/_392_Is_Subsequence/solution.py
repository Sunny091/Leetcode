from typing import List


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        LeetCode 392. Is Subsequence

        TODO: Implement your solution here
        """
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)
