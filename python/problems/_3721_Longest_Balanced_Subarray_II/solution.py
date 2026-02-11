from typing import List


class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        answer = 0
        length = len(nums)
        has_answer = False
        for i in reversed(range(length)):
            if has_answer:
                break
            for j in range(length-i):
                subarray = set(nums[j:j+i+1])
                balance = 0
                for num in subarray:
                    balance += 1-(num & 1)*2
                if balance == 0:
                    answer = i+1
                    has_answer = True
                    break
        return answer
