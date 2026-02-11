from typing import List


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
        LeetCode 1768. Merge Strings Alternately

        TODO: Implement your solution here
        """
        i, j = 0, 0
        res = []
        while i < len(word1) and j < len(word2):
            res.append(word1[i])
            res.append(word2[j])
            i += 1
            j += 1
        if i < len(word1):
            res.append(word1[i:])
        if j < len(word2):
            res.append(word2[j:])
        return ''.join(res)
