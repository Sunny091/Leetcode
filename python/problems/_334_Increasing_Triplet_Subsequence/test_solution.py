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
        nums = [1,2,3,4,5]
        assert self.sol.increasingTriplet(nums) == True

    def test_example_2(self):
        # TODO: Add test case
        nums = [5,4,3,2,1]
        assert self.sol.increasingTriplet(nums) == False
    
    def test_example_3(self):
        # TODO: Add test case
        nums = [2,1,5,0,4,6]
        assert self.sol.increasingTriplet(nums) == True
