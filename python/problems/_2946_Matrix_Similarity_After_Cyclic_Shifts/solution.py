from typing import List


class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        """
        LeetCode 2946. Matrix Similarity After Cyclic Shifts

        TODO: Implement your solution here
        """
        length = len(mat[0])
        if k == length:
            return True
        k_new = k % length
        for row in mat:
            if row != row[-k_new:] + row[:-k_new]:
                return False
        return True
