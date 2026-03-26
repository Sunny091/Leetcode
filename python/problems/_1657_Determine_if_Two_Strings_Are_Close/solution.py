from typing import List


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        """
        LeetCode 1657. Determine if Two Strings Are Close

        TODO: Implement your solution here
        """
        word1_set = set(word1)
        word2_set = set(word2)
        if word1_set != word2_set:
            return False
        word1_freq = []
        word2_freq = []
        for c in word1_set:
            word1_freq.append(word1.count(c))
        for c in word2_set:
            word2_freq.append(word2.count(c))
        word1_freq_values = sorted(word1_freq)
        word2_freq_values = sorted(word2_freq)
        return word1_freq_values == word2_freq_values
