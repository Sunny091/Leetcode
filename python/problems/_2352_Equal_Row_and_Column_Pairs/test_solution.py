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
        grid = [[3,2,1],[1,7,6],[2,7,7]]
        expected = 1
        assert self.sol.equalPairs(grid) == expected

    def test_example_2(self):
        # TODO: Add test case
        grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
        expected = 3
        assert self.sol.equalPairs(grid) == expected

    # def test_example_3(self):
    #     # TODO: Add test case
    #     pass
