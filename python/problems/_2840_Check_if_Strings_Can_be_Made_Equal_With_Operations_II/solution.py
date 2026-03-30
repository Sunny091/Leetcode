from typing import List
from collections import Counter


class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        """
        LeetCode 2840. Check if Strings Can be Made Equal With Operations II

        TODO: Implement your solution here
        """
        s1_count_odd = Counter(s1[i] for i in range(0, len(s1), 2))
        s1_count_even = Counter(s1[i] for i in range(1, len(s1), 2))
        s2_count_odd = Counter(s2[i] for i in range(0, len(s2), 2))
        s2_count_even = Counter(s2[i] for i in range(1, len(s2), 2))

        return s1_count_odd == s2_count_odd and s1_count_even == s2_count_even
