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
        nums = [1,1,1,0,0,0,1,1,1,1,0]
        k = 2
        assert self.sol.longestOnes(nums, k) == 6

    def test_example_2(self):
        # TODO: Add test case
        nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
        k = 3
        assert self.sol.longestOnes(nums, k) == 10
    
    # def test_example_3(self):
    #     # TODO: Add test case
    #     pass
