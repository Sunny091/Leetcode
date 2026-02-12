from typing import List
import math


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """
        LeetCode 605. Can Place Flowers

        TODO: Implement your solution here
        """
        length = len(flowerbed)
        accept = 0
        start_index = 0
        record = False
        low_bound = 0
        up_bound = length
        if flowerbed[0] == 0:
            for i in range(length):
                if flowerbed[i] == 1:
                    low_bound = i + 1
                    accept += math.floor(i / 2)
                    break
                if i == length - 1:
                    return math.ceil(length / 2) >= n

        if flowerbed[-1] == 0:
            for i in reversed(range(length)):
                if flowerbed[i] == 1:
                    up_bound = i + 1
                    accept += math.floor((length - 1 - i) / 2)
                    break

        for i in range(low_bound, up_bound):
            if flowerbed[i] == 0 and not record:
                start_index = i
                record = True
            elif flowerbed[i] == 1 and record:
                record = False
                empty = i - start_index - 2
                accept += math.ceil(empty / 2)

        return accept >= n
