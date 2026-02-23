from typing import List


class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        """
        LeetCode 1461. Check If a String Contains All Binary Codes of Size K

        TODO: Implement your solution here
        """
        if len(s) < k:
            return False
        seen = set()
        for i in range(len(s) - k + 1):
            seen.add(s[i:i+k])
        return len(seen) == 2 ** k
