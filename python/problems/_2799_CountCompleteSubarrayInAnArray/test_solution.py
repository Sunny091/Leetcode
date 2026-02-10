import pytest
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

from solution import Solution


class TestSolution:
    def setup_method(self):
        self.sol = Solution()

    def test_example_1(self):
        nums = [1, 3, 1, 2, 2]
        assert self.sol.countCompleteSubarrays(nums) == 4

    def test_example_2(self):
        nums = [5, 5, 5, 5]
        assert self.sol.countCompleteSubarrays(nums) == 10
