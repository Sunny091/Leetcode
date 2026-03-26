from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        """
        LeetCode 1207. Unique Number of Occurrences

        TODO: Implement your solution here
        """
        arr_set = set(arr)
        count_set = set()
        for num in arr_set:
            count = arr.count(num)
            if count in count_set:
                return False
            count_set.add(count)
        return True
