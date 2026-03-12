from typing import List


class Solution:
    def bitwiseComplement(self, n: int) -> int:
        """
        LeetCode 1009. Complement of Base 10 Integer

        TODO: Implement your solution here
        """
        if n == 0:
            return 1
        bit_len = n.bit_length()
        mask = (1 << bit_len) - 1
        return n ^ mask
