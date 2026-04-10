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
        nums = [1,2,1,1,3]
        expected = 6
        assert self.sol.minimumDistance(nums) == expected

    def test_example_2(self):
        # TODO: Add test case
        nums = [1,1,2,3,2,1,2]
        expected = 8
        assert self.sol.minimumDistance(nums) == expected

    def test_example_3(self):
        # TODO: Add test case
        nums = [1]
        expected = -1
        assert self.sol.minimumDistance(nums) == expected
