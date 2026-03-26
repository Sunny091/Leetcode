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
        nums = [1,7,3,6,5,6]
        expected = 3
        assert self.sol.pivotIndex(nums) == expected

    def test_example_2(self):
        # TODO: Add test case
        nums = [1,2,3]
        expected = -1
        assert self.sol.pivotIndex(nums) == expected
    
    def test_example_3(self):
        # TODO: Add test case
        nums = [2,1,-1]
        expected = 0
        assert self.sol.pivotIndex(nums) == expected
    
    def test_example_4(self):
        nums = [-1,-1,-1,-1,-1,0]
        expected = 2
        assert self.sol.pivotIndex(nums) == expected
