from typing import List


class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        answer = 0
        temp = set()
        for i in range(len(nums)):
            if i > len(nums)-answer:
                break
            balance = 0
            temp.add(nums[i])
            balance += 1-(nums[i] & 1)*2
            for j in range(i+1, len(nums)):
                if nums[j] in temp:
                    if balance == 0:
                        answer = max(answer, j - i + 1)
                    continue
                temp.add(nums[j])
                balance += 1-(nums[j] & 1)*2
                if balance == 0:
                    answer = max(answer, j - i + 1)
            temp.clear()
        return answer
