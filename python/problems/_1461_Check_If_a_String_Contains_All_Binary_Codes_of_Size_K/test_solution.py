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
        s = "00110110"
        k = 2
        assert self.sol.hasAllCodes(s, k) == True

    def test_example_2(self):
        # TODO: Add test case
        s = "0110"
        k = 1
        assert self.sol.hasAllCodes(s, k) == True
    

    def test_example_3(self):
        # TODO: Add test case
        s = "0110"
        k = 2
        assert self.sol.hasAllCodes(s, k) == False
