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
        nums = [1,2,3,4]
        assert self.sol.productExceptSelf(nums) == [24,12,8,6]

    def test_example_2(self):
        # TODO: Add test case
        nums = [-1,1,0,-3,3]
        assert self.sol.productExceptSelf(nums) == [0,0,9,0,0]
    
    # def test_example_3(self):
    #     # TODO: Add test case
    #     pass
