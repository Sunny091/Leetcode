from typing import List


class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        """
        LeetCode 3653. XOR After Range Multiplication Queries I

        TODO: Implement your solution here
        """
        MOD = 10**9 + 7
        for query in queries:
            l, r, k, v = query
            idx = l
            while idx <= r:
                nums[idx] = (nums[idx] * v) % MOD
                idx += k

        answer = nums[0]
        for i in range(1, len(nums)):
            answer ^= nums[i]

        return answer
