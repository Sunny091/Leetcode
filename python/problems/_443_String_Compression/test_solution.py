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
        chars = ["a","a","b","b","c","c","c"]
        assert self.sol.compress(chars) == 6

    def test_example_2(self):
        # TODO: Add test case
        chars = ["a"]
        assert self.sol.compress(chars) == 1
    
    def test_example_3(self):
        # TODO: Add test case
        chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
        assert self.sol.compress(chars) == 4
