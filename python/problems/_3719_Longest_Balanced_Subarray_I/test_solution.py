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
        nums = [2, 5, 4, 3]
        assert self.sol.longestBalanced(nums) == 4

    def test_example_2(self):
        # TODO: Add test case
        nums = [3, 2, 2, 5, 4]
        assert self.sol.longestBalanced(nums) == 5

    def test_example_3(self):
        # TODO: Add test case
        nums = [1, 2, 3, 2]
        assert self.sol.longestBalanced(nums) == 3
