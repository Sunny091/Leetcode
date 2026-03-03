from typing import List
import math


class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        """
        LeetCode 1545. Find Kth Bit in Nth Binary String

        TODO: Implement your solution here
        """
        bound = math.ceil(k ** 0.5)
        s = "0"
        if k == 1:
            return s
        if type(k ** 0.5) == int:
            return "1"
        for i in range(1, bound + 1):
            s = s + "1" + s[::-1].translate(str.maketrans("01", "10"))
            print(s)
            if len(s) >= k:
                return s[k - 1]
