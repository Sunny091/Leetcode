from typing import List


class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        """
        LeetCode 3719. Longest Balanced Subarray I

        TODO: Implement your solution here
        """
        answer = 0
        for i in range(len(nums)):
            balence = 0
            temp = []
            temp.append(nums[i])
            if nums[i] % 2 == 0:
                balence += 1
            else:
                balence -= 1
            for j in range(i+1, len(nums)):
                if nums[j] in temp:
                    if balence == 0:
                        answer = max(answer, j - i + 1)
                    continue
                temp.append(nums[j])
                if nums[j] % 2 == 0:
                    balence += 1
                else:
                    balence -= 1
                if balence == 0:
                    answer = max(answer, j - i + 1)
        return answer
