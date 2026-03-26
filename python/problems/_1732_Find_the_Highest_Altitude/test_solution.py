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
        gain = [-5,1,5,0,-7]
        expected = 1
        assert self.sol.largestAltitude(gain) == expected

    def test_example_2(self):
        # TODO: Add test case
        gain = [-4,-3,-2,-1,4,3,2]
        expected = 0
        assert self.sol.largestAltitude(gain) == expected
    
    # def test_example_3(self):
    #     # TODO: Add test case
    #     pass
