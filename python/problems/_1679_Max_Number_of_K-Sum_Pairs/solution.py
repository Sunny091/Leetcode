from collections import Counter
from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        """
        LeetCode 1679. Max Number of K-Sum Pairs

        TODO: Implement your solution here
        """
        
        count = Counter(nums)
        operations = 0
        seen = set()
        for num in count:
            complement = k - num
            if complement in count and num not in seen:
                if num == complement:
                    operations += count[num] // 2
                else:
                    operations += min(count[num], count[complement])
                seen.add(complement)
        return operations