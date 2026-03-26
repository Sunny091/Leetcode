from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        """
        LeetCode 2352. Equal Row and Column Pairs

        TODO: Implement your solution here
        """
        grid_list = list(tuple(row) for row in grid)
        count = 0
        for col in zip(*grid):
            if col in grid_list:
                count += grid_list.count(col)
        return count
