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
        s = "abbac"
        assert self.sol.longestBalanced(s) == 4

    def test_example_2(self):
        # TODO: Add test case
        s = "zzabccy"
        assert self.sol.longestBalanced(s) == 4
    
    def test_example_3(self):
        # TODO: Add test case
        s = "aba"
        assert self.sol.longestBalanced(s) == 2
    
    def test_example_4(self):
        # TODO: Add test case
        s = "ss"
        assert self.sol.longestBalanced(s) == 2
    
    def test_example_5(self):
        # TODO: Add test case
        s = "pqtqt"
        assert self.sol.longestBalanced(s) == 4
