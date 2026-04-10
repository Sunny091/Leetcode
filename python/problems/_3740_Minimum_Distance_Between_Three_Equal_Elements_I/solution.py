from typing import List


class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        """
        LeetCode 3740. Minimum Distance Between Three Equal Elements I

        TODO: Implement your solution here
        """
        INF = float('inf')
        length = len(nums)
        looked = {}
        record = [[0 for _ in range(length)] for _ in range(101)]
        answer = INF

        if length < 3:
            return -1

        for i in range(length):
            if nums[i] not in looked:
                looked[nums[i]] = 1
                record[nums[i]][0] = i
            else:
                looked[nums[i]] += 1
                record[nums[i]][looked[nums[i]] - 1] = i
                if looked[nums[i]] < 3:
                    continue
                else:
                    answer = min(answer, (record[nums[i]][looked[nums[i]] - 1] - record[nums[i]][looked[nums[i]] - 3]) * 2)

        return answer if answer != INF else -1
