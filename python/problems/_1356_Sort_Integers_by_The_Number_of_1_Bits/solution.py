from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        """
        LeetCode 1356. Sort Integers by The Number of 1 Bits

        TODO: Implement your solution here
        """
        return sorted(arr, key=lambda x: (bin(x).count('1'), x))
