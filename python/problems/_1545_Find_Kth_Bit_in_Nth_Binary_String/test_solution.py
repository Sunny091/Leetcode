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
        n = 3
        k = 1
        assert self.sol.findKthBit(n, k) == "0"

    def test_example_2(self):
        # TODO: Add test case
        n = 4
        k = 11
        assert self.sol.findKthBit(n, k) == "1"
    
    # def test_example_3(self):
    #     # TODO: Add test case
    #     pass
