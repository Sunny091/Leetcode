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
        arr = [1,2,2,1,1,3]
        assert self.sol.uniqueOccurrences(arr) == True

    def test_example_2(self):
        # TODO: Add test case
        arr = [1,2]
        assert self.sol.uniqueOccurrences(arr) == False

    def test_example_3(self):
        # TODO: Add test case
        arr = [-3,0,1,-3,1,1,1,-3,10,0]
        assert self.sol.uniqueOccurrences(arr) == True

