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
        arrr = [0,1,2,3,4,5,6,7,8]
        expected = [0,1,2,4,8,3,5,6,7]
        assert self.sol.sortByBits(arrr) == expected

    def test_example_2(self):
        # TODO: Add test case
        arrr = [1024,512,256,128,64,32,16,8,4,2,1]
        expected = [1,2,4,8,16,32,64,128,256,512,1024]
        assert self.sol.sortByBits(arrr) == expected
    
    # def test_example_3(self):
    #     # TODO: Add test case
    #     pass
