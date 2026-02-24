from typing import List


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        """
        LeetCode 1456. Maximum Number of Vowels in a Substring of Geven Length

        TODO: Implement your solution here
        """
        vowel = set("aeiou")
        count = 0
        for i in range(k):
            if s[i] in vowel:
                count += 1
        max_count = count
        for i in range(k, len(s)):
            if s[i] in vowel:
                count += 1
            if s[i - k] in vowel:
                count -= 1
            max_count = max(max_count, count)
        return max_count
