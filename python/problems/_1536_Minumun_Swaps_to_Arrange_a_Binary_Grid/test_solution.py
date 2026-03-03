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
        grid = [[0,0,1],[1,1,0],[1,0,0]]
        expected = 3
        assert self.sol.minSwaps(grid) == expected

    def test_example_2(self):
        # TODO: Add test case
        grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
        expected = -1
        assert self.sol.minSwaps(grid) == expected
    
    def test_example_3(self):
        # TODO: Add test case
        grid = [[1,0,0],[1,1,0],[1,1,1]]
        expected = 0
        assert self.sol.minSwaps(grid) == expected
