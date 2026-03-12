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
        n = 5
        expect = 2
        assert self.sol.bitwiseComplement(n) == expect

    def test_example_2(self):
        # TODO: Add test case
        n = 7
        expect = 0
        assert self.sol.bitwiseComplement(n) == expect
    
    def test_example_3(self):
        # TODO: Add test case
        n = 10
        expect = 5
        assert self.sol.bitwiseComplement(n) == expect
