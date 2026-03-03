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
        height = [1,8,6,2,5,4,8,3,7]
        assert self.sol.maxArea(height) == 49

    def test_example_2(self):
        # TODO: Add test case
        height = [1,1]
        assert self.sol.maxArea(height) == 1
    
    # def test_example_3(self):
    #     # TODO: Add test case
    #     pass
