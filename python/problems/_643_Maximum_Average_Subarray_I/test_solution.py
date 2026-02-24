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
        nums = [1,12,-5,-6,50,3]
        k = 4
        assert self.sol.findMaxAverage(nums, k) == 12.75000

    def test_example_2(self):
        # TODO: Add test case
        nums = [5]
        k = 1
        assert self.sol.findMaxAverage(nums, k) == 5.00000
    
    # def test_example_3(self):
    #     # TODO: Add test case
    #     pass
