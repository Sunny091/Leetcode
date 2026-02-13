from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        """
        LeetCode 1431. Kids With the Greatest Number of Candies

        TODO: Implement your solution here
        """
        max_candies = max(candies)
        return [candy + extraCandies >= max_candies for candy in candies]
