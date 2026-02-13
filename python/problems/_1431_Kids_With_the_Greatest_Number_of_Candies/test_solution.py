import pytest
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

from solution import Solution


class TestSolution:
    def setup_method(self):
        self.sol = Solution()

    def test_example_1(self):
        # TODO: Add test case
        candies = [2,3,5,1,3]
        extraCandies = 3
        assert self.sol.kidsWithCandies(candies, extraCandies) == [True, True, True, False, True]

    def test_example_2(self):
        # TODO: Add test case
        candies = [4,2,1,1,2]
        extraCandies = 1
        assert self.sol.kidsWithCandies(candies, extraCandies) == [True, False, False, False, False]
    
    def test_example_3(self):
        # TODO: Add test case
        candies = [12,1,12]
        extraCandies = 10
        assert self.sol.kidsWithCandies(candies, extraCandies) == [True, False, True]
